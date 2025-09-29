"""Tests for SuitEngine validation behaviour."""

import unittest

from suit_engine import CycleContext, SuitEngine, SuitValidationError


def _valid_cycle() -> dict:
    return {
        "cycle": 1,
        "DRAFT": "Draft",
        "REFLECT": ["Reflect"],
        "REVISE": "Revise",
        "LEARNED": "Learned",
        "noise_log": ["noise"],
        "responsibility": "tester",
        "validation_passed": False,
        "timestamp": "2025-01-01T00:00:00+00:00",
        "version": "1.0.0",
    }


class SuitEngineTests(unittest.TestCase):
    def test_suit_engine_validates_cycle(self) -> None:
        engine = SuitEngine()
        cycle = _valid_cycle()
        context = CycleContext(cycle_number=1, raw_input="signal")

        validated = engine.validate_and_recurse(cycle, context)

        self.assertTrue(validated["validation_passed"])

    def test_suit_engine_rejects_missing_field(self) -> None:
        engine = SuitEngine()
        cycle = _valid_cycle()
        del cycle["responsibility"]
        context = CycleContext(cycle_number=1, raw_input="signal")

        with self.assertRaises(SuitValidationError):
            engine.validate_and_recurse(cycle, context)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()