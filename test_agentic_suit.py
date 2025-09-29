"""Integration tests for agentic suit utilities."""

import json
import tempfile
import unittest
from pathlib import Path

from attention_loop import AttentionLoop
from instruction_agentic_code_suit_Architecture import AgenticSuit
from ledger import SafetyLedger


class AgenticSuitTests(unittest.TestCase):
    def test_suit_report_payload_matches_schema(self) -> None:
        suit = AgenticSuit()
        report = suit.execute(
            {
                "objective": "Demonstrate schema compliance",
                "notes": "Ensure ledger payload includes required fields",
            },
            label="demo",
        )
        payload = report.to_payload(previous_hash="0" * 64)

        for field in (
            "identity",
            "law_abiding",
            "ad_free",
            "cycles",
            "responsibility_chain",
            "hash",
            "previous_hash",
            "timestamp",
            "label",
        ):
            self.assertIn(field, payload)

    def test_safety_ledger_chains_hashes(self) -> None:
        suit = AgenticSuit()
        with tempfile.TemporaryDirectory() as tmp:
            ledger_path = Path(tmp) / "ledger.jsonl"
            ledger = SafetyLedger(ledger_path)

            first_payload = ledger.append_report(
                suit.execute("first signal", label="first")
            )
            second_payload = ledger.append_report(
                suit.execute("second signal", label="second")
            )

            self.assertNotEqual(first_payload["hash"], second_payload["hash"])
            self.assertEqual(second_payload["previous_hash"], first_payload["hash"])

            contents = ledger_path.read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(contents), 2)
            for line in contents:
                json.loads(line)

    def test_attention_loop_process_signal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger_path = Path(tmp) / "ledger.jsonl"
            ledger = SafetyLedger(ledger_path)
            loop = AttentionLoop(suit=AgenticSuit(), ledger=ledger, maintenance_interval_seconds=0)

            payload = loop.process_signal("loop signal", label="loop")
            self.assertEqual(payload["label"], "loop")
            self.assertTrue(Path(ledger_path).exists())

            maintenance = loop.maintenance_if_due(reason="test")
            self.assertIsNotNone(maintenance)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
