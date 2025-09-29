"""Tests for PB2SFramework recursion."""

import unittest

from pb2s_framework import PB2SFramework


class PB2SFrameworkTests(unittest.TestCase):
    def test_framework_runs_minimum_cycles(self) -> None:
        framework = PB2SFramework()
        result = framework.run(
            {
                "objective": "Validate PB2S recursion",
                "concerns": "Risk of drift, need for responsibility markers",
            }
        )

        self.assertGreaterEqual(len(result), 3)
        for cycle in result:
            self.assertGreaterEqual(cycle["cycle"], 1)
            self.assertTrue(cycle["validation_passed"])

        final_cycle = result[-1]
        self.assertIn("resolved", final_cycle["LEARNED"].lower())
        self.assertIn("responsibility", final_cycle["LEARNED"].lower())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()