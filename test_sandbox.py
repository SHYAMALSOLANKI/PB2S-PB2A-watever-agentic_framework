"""Tests for sandbox manager behaviour."""

import unittest
from datetime import datetime

from sandbox_manager import SandboxManager, SandboxViolation


class SandboxManagerTests(unittest.TestCase):
    def test_sandbox_context_enforces_single_session(self) -> None:
        sandbox = SandboxManager()

        with sandbox.enforce_runtime("primary"):
            self.assertTrue(sandbox.is_active)
            with self.assertRaises(SandboxViolation):
                with sandbox.enforce_runtime("secondary"):
                    pass

        self.assertFalse(sandbox.is_active)
        self.assertEqual(len(sandbox.audit_log), 1)

    def test_maintenance_ping_records_session(self) -> None:
        sandbox = SandboxManager()
        record = sandbox.maintenance_ping("heartbeat")

        self.assertIsInstance(record.started_at, datetime)
        self.assertEqual(record.label, "maintenance::heartbeat")
        self.assertEqual(len(sandbox.audit_log), 1)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()