"""Suit Engine Middleware.

The suit is responsible for guaranteeing that every PB2S recursion cycle is
schema-complete, contradiction-aware, and equally attentive to signal and
noise. The implementation keeps the moving parts minimal while still providing
hooks for dynamic extensions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional

from schema_definitions import PB2S_CYCLE_SCHEMA


class SuitValidationError(ValueError):
    """Raised when cycle data fails to satisfy PB2S requirements."""


@dataclass
class CycleContext:
    """Context object passed to extensions for additional processing."""

    cycle_number: int
    raw_input: Any
    previous_cycles: List[Dict[str, Any]] = field(default_factory=list)


class SuitEngine:
    """Validate and enrich PB2S recursion cycles."""

    def __init__(self, schema: Optional[Dict[str, Any]] = None) -> None:
        self.schema = schema or PB2S_CYCLE_SCHEMA
        self._extensions: List[Callable[[Dict[str, Any], CycleContext], None]] = []
        self._noise_log: List[str] = []

    def register_extension(
        self, handler: Callable[[Dict[str, Any], CycleContext], None]
    ) -> None:
        """Attach a callable that can inspect or modify cycles post-validation."""

        self._extensions.append(handler)

    def validate_and_recurse(
        self,
        cycle_data: Dict[str, Any],
        context: CycleContext,
    ) -> Dict[str, Any]:
        """Validate a cycle and allow extensions to refine it.

        Parameters
        ----------
        cycle_data:
            The dictionary representing a PB2S cycle.
        context:
            Metadata about the current recursion step.
        """

        self._validate_schema(cycle_data)
        self._ensure_responsibility(cycle_data)
        self._log_noise(cycle_data)

        # Run extensions after core validation so that they can add fields or
        # annotations confidently.
        for handler in self._extensions:
            handler(cycle_data, context)

        cycle_data["validation_passed"] = True
        return cycle_data

    @property
    def noise_log(self) -> List[str]:
        """Return a snapshot of aggregated noise observations."""

        return list(self._noise_log)

    def _validate_schema(self, cycle_data: Dict[str, Any]) -> None:
        required = self.schema.get("required", [])
        for field in required:
            if field not in cycle_data:
                raise SuitValidationError(f"Missing required field: {field}")

        properties = self.schema.get("properties", {})
        for field, definition in properties.items():
            if field not in cycle_data:
                continue

            expected_type = definition.get("type")
            value = cycle_data[field]

            if expected_type == "integer" and not isinstance(value, int):
                raise SuitValidationError(f"Field '{field}' must be integer")
            if expected_type == "string" and not isinstance(value, str):
                raise SuitValidationError(f"Field '{field}' must be string")
            if expected_type == "boolean" and not isinstance(value, bool):
                raise SuitValidationError(f"Field '{field}' must be boolean")
            if expected_type == "array":
                if not isinstance(value, list):
                    raise SuitValidationError(f"Field '{field}' must be list")
                item_type = definition.get("items", {}).get("type")
                if item_type == "string":
                    if not all(isinstance(item, str) for item in value):
                        raise SuitValidationError(
                            f"Field '{field}' must contain only strings"
                        )

            if definition.get("format") == "date-time":
                self._validate_iso_datetime(field, str(value))

        cycle_data.setdefault("validation_passed", False)

    def _ensure_responsibility(self, cycle_data: Dict[str, Any]) -> None:
        if not cycle_data.get("responsibility"):
            raise SuitValidationError("Responsibility marker must be non-empty")

    def _log_noise(self, cycle_data: Dict[str, Any]) -> None:
        noise_entries = cycle_data.get("noise_log", [])
        if not isinstance(noise_entries, list):
            raise SuitValidationError("noise_log must be a list")
        self._noise_log.extend(str(entry) for entry in noise_entries if entry)

    @staticmethod
    def _validate_iso_datetime(field: str, value: str) -> None:
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as exc:
            raise SuitValidationError(
                f"Field '{field}' must be ISO 8601 datetime"
            ) from exc