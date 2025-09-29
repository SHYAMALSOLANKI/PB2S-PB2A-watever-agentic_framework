"""Agentic Window Runtime Enforcement.

The sandbox models a zero-egress execution window. It does not perform
operating-system level isolation (that responsibility lives with the host),
but it *does* guarantee:

- Single active session at a time (prevents uncontrolled concurrency).
- Explicit lifecycle timestamps for auditability.
- Structured logging of every entry/exit and maintenance check.
- Clear violation signalling if a caller attempts to run outside the guarded
  context.

This module intentionally keeps the runtime surface minimal so PB2S can remain
self-responsible while still offering hooks for deeper containment layers.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Generator, List, Optional


class SandboxViolation(RuntimeError):
    """Raised when sandbox guarantees are broken."""


@dataclass(frozen=True)
class SandboxSession:
    """Immutable record describing a sandbox session lifecycle."""

    label: str
    started_at: datetime
    closed_at: Optional[datetime]


class SandboxManager:
    """Minimal supervisory layer for PB2S runtime isolation."""

    def __init__(self) -> None:
        self._active_label: Optional[str] = None
        self._audit_log: List[Dict[str, datetime]] = []

    @contextmanager
    def enforce_runtime(self, label: str) -> Generator[Dict[str, datetime], None, None]:
        """Context manager that enforces a single active sandbox session.

        Parameters
        ----------
        label:
            Developer-provided identifier for tracing the supervised action.
        """

        if self._active_label is not None:
            raise SandboxViolation(
                f"Sandbox already active with label '{self._active_label}'."
            )

        self._active_label = label
        entry = {
            "label": label,
            "started_at": datetime.now(timezone.utc),
            "closed_at": None,
        }
        self._audit_log.append(entry)

        try:
            yield entry
        finally:
            entry["closed_at"] = datetime.now(timezone.utc)
            self._active_label = None

    def maintenance_ping(self, reason: str) -> SandboxSession:
        """Register a maintenance cycle.

        Maintenance keeps the sandbox self-aware even when no external calls
        occur. Each ping is returned as a ``SandboxSession`` for structured
        downstream logging.
        """

        record = SandboxSession(
            label=f"maintenance::{reason}",
            started_at=datetime.now(timezone.utc),
            closed_at=datetime.now(timezone.utc),
        )
        self._audit_log.append(
            {
                "label": record.label,
                "started_at": record.started_at,
                "closed_at": record.closed_at,
            }
        )
        return record

    @property
    def is_active(self) -> bool:
        """Indicate whether the sandbox currently supervises an operation."""

        return self._active_label is not None

    @property
    def audit_log(self) -> List[SandboxSession]:
        """Return immutable views over recorded sessions."""

        sessions: List[SandboxSession] = []
        for entry in self._audit_log:
            sessions.append(
                SandboxSession(
                    label=entry["label"],
                    started_at=entry["started_at"],
                    closed_at=entry["closed_at"],
                )
            )
        return sessions