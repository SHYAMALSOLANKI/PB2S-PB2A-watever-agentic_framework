"""Safety ledger for PB2S suit reports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional

from instruction_agentic_code_suit_Architecture import SuitReport


class SafetyLedger:
    """Append-only JSONL ledger with hash chaining."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append_report(self, report: SuitReport) -> Dict[str, object]:
        """Append a suit report and return the final payload."""

        previous_hash = self.last_hash()
        payload = report.to_payload(previous_hash=previous_hash)

        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        return payload

    def last_hash(self) -> str:
        if not self.path.exists():
            return "0" * 64

        last_line: Optional[str] = None
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    last_line = line

        if not last_line:
            return "0" * 64

        try:
            record = json.loads(last_line)
            return record.get("hash", "0" * 64)
        except json.JSONDecodeError:
            return "0" * 64
