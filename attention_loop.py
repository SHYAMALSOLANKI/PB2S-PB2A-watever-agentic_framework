"""Runtime attention loop for PB2S agentic suit."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from instruction_agentic_code_suit_Architecture import AgenticSuit
from ledger import SafetyLedger


@dataclass
class AttentionState:
	last_signal_at: datetime
	last_maintenance_at: datetime


class AttentionLoop:
	"""Maintain continuous attention and optional ledger persistence."""

	def __init__(
		self,
		*,
		suit: AgenticSuit | None = None,
		ledger: SafetyLedger | None = None,
		maintenance_interval_seconds: int = 900,
	) -> None:
		self.suit = suit or AgenticSuit()
		self.ledger = ledger
		now = datetime.now(timezone.utc)
		self.state = AttentionState(last_signal_at=now, last_maintenance_at=now)
		self.maintenance_interval = timedelta(seconds=maintenance_interval_seconds)

	def process_signal(self, signal: Any, *, label: str = "signal") -> Dict[str, Any]:
		"""Process a signal and optionally persist the report to the ledger."""

		report = self.suit.execute(signal, label=label)
		if self.ledger:
			payload = self.ledger.append_report(report)
		else:
			payload = report.to_payload(previous_hash=self._previous_hash())
		self.state.last_signal_at = datetime.now(timezone.utc)
		return payload

	def maintenance_if_due(self, *, reason: str = "attention_loop") -> Optional[Dict[str, Any]]:
		"""Trigger a maintenance ping if the interval has elapsed."""

		now = datetime.now(timezone.utc)
		if now - max(self.state.last_signal_at, self.state.last_maintenance_at) < self.maintenance_interval:
			return None

		record = self.suit.sandbox_manager.maintenance_ping(reason)
		self.state.last_maintenance_at = now
		if self.ledger:
			self.ledger.append_report(
				self.suit.execute(
					{
						"maintenance": reason,
						"timestamp": record.started_at.isoformat(),
					},
					label=f"maintenance::{reason}",
				)
			)
		return {
			"label": record.label,
			"started_at": record.started_at.isoformat(),
			"closed_at": record.closed_at.isoformat() if record.closed_at else None,
		}

	def _previous_hash(self) -> str:
		if not self.ledger:
			return "0" * 64
		return self.ledger.last_hash()
