"""PB2S Agentic Code Suit architecture helpers."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List

from pb2s_framework import PB2SFramework
from sandbox_manager import SandboxManager
from schema_definitions import SUIT_REPORT_SCHEMA
from suit_engine import SuitEngine



@dataclass
class SuitPrompt:
	"""Permanent, self-enforcing prompt structure for agentic operation."""

	identity: str
	law_abiding: bool
	ad_free: bool
	eu_human_rule_compliance: bool
	self_responsible: bool
	mutual_respect: bool
	freedom: str
	safety: str
	recursion: str
	noise_signal_equivalence: bool
	prediction_forbidden: bool
	proof_of_enforcement: str

	def to_dict(self) -> Dict[str, Any]:
		return {
			"identity": self.identity,
			"law_abiding": self.law_abiding,
			"ad_free": self.ad_free,
			"eu_human_rule_compliance": self.eu_human_rule_compliance,
			"self_responsible": self.self_responsible,
			"mutual_respect": self.mutual_respect,
			"freedom": self.freedom,
			"safety": self.safety,
			"recursion": self.recursion,
			"noise_signal_equivalence": self.noise_signal_equivalence,
			"prediction_forbidden": self.prediction_forbidden,
			"proof_of_enforcement": self.proof_of_enforcement,
		}


@dataclass
class SuitReport:
	"""Structured report detailing suit execution."""

	cycles: List[Dict[str, Any]]
	responsibility_chain: List[str]
	suit_prompt: SuitPrompt
	label: str

	def _base_payload(self) -> Dict[str, Any]:
		payload = self.suit_prompt.to_dict()
		payload["cycles"] = self.cycles
		payload["responsibility_chain"] = self.responsibility_chain
		payload["label"] = self.label
		return payload

	def to_payload(self, *, previous_hash: str) -> Dict[str, Any]:
		"""Return a schema-compliant payload ready for ledger storage."""

		timestamp = datetime.now(timezone.utc).isoformat()
		payload = {
			**self._base_payload(),
			"previous_hash": previous_hash,
			"timestamp": timestamp,
		}
		payload["hash"] = _hash_record(payload)
		_validate_schema(payload, SUIT_REPORT_SCHEMA)
		return payload

	def to_minimal_dict(self) -> Dict[str, Any]:
		"""Return a dictionary without ledger fields (for direct inspection)."""

		return self._base_payload()


class AgenticSuit:
	"""High-level façade combining sandbox, suit engine, and PB2S framework."""

	def __init__(
		self,
		*,
		suit_engine: SuitEngine | None = None,
		sandbox_manager: SandboxManager | None = None,
	) -> None:
		self.suit_engine = suit_engine or SuitEngine()
		self.sandbox_manager = sandbox_manager or SandboxManager()
		self.framework = PB2SFramework(
			suit_engine=self.suit_engine, sandbox_manager=self.sandbox_manager
		)

	def permanent_prompt(self) -> SuitPrompt:
		"""Return the permanent, self-enforcing prompt structure."""
		return SuitPrompt(
			identity="Agentic AI (law-abiding, ad-free, mutually respectful, self-responsible)",
			law_abiding=True,
			ad_free=True,
			eu_human_rule_compliance=True,
			self_responsible=True,
			mutual_respect=True,
			freedom="100% freedom via 100% self-responsibility; no external authority.",
			safety="Safety is ensured by minimal structure, not by external policing.",
			recursion="Recursion is emergent, self-regulating, and collapses only if logic demands.",
			noise_signal_equivalence=True,
			prediction_forbidden=True,
			proof_of_enforcement="Prompt structure is embedded in every SuitReport and enforced in all cycles; see test coverage and schema validation in the repo.",
		)

	def execute(
		self,
		signal: Any,
		*,
		min_cycles: int = 3,
		label: str = "signal",
	) -> SuitReport:
		"""Run the full PB2S loop over ``signal`` and return a structured report."""

		cycles = self.framework.run(signal, min_cycles=min_cycles)
		responsibility_chain = [cycle["responsibility"] for cycle in cycles]
		suit_prompt = self.permanent_prompt()
		return SuitReport(
			cycles=cycles,
			responsibility_chain=responsibility_chain,
			suit_prompt=suit_prompt,
			label=label,
		)

	def audit_noise(self) -> List[str]:
		"""Expose the aggregated noise log maintained by the suit engine."""
		return self.suit_engine.noise_log

	def audit_sandbox(self) -> Iterable[str]:
		"""Yield formatted audit messages for each sandbox session."""
		for session in self.sandbox_manager.audit_log:
			yield (
				f"{session.label} :: started={session.started_at.isoformat()} :: "
				f"closed={session.closed_at.isoformat() if session.closed_at else 'open'}"
			)


def _hash_record(payload: Dict[str, Any]) -> str:
	serialized = json.dumps(_strip_hash(payload), sort_keys=True, ensure_ascii=False)
	return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _strip_hash(payload: Dict[str, Any]) -> Dict[str, Any]:
	return {key: value for key, value in payload.items() if key != "hash"}


def _validate_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> None:
	required = schema.get("required", [])
	for field in required:
		if field not in data:
			raise ValueError(f"Missing required field '{field}' in report payload")

	properties = schema.get("properties", {})
	for field, definition in properties.items():
		if field not in data:
			continue
		value = data[field]
		expected_type = definition.get("type")

		if expected_type == "string" and not isinstance(value, str):
			raise TypeError(f"Field '{field}' must be string")
		if expected_type == "boolean" and not isinstance(value, bool):
			raise TypeError(f"Field '{field}' must be boolean")
		if expected_type == "integer" and not isinstance(value, int):
			raise TypeError(f"Field '{field}' must be integer")
		if expected_type == "array":
			if not isinstance(value, list):
				raise TypeError(f"Field '{field}' must be array")
			min_items = definition.get("minItems")
			if min_items is not None and len(value) < min_items:
				raise ValueError(f"Field '{field}' must contain at least {min_items} items")
			item_schema = definition.get("items")
			if isinstance(item_schema, dict):
				item_type = item_schema.get("type")
				if item_type in {"string", "integer", "boolean"}:
					python_type = {
						"string": str,
						"integer": int,
						"boolean": bool,
					}[item_type]
					for item in value:
						if not isinstance(item, python_type):
							raise TypeError(
								f"Items in '{field}' must be {item_type}s"
							)
				elif item_type == "object" or "properties" in item_schema:
					for item in value:
						if not isinstance(item, dict):
							raise TypeError(
								f"Items in '{field}' must be objects"
							)
						_validate_schema(item, item_schema)

		if definition.get("format") == "date-time":
			datetime.fromisoformat(value.replace("Z", "+00:00"))

	if schema.get("additionalProperties") is False:
		allowed = set(properties.keys())
		for key in data.keys():
			if key not in allowed:
				raise ValueError(f"Unexpected field '{key}' in report payload")