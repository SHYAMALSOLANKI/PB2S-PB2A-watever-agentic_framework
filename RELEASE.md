# PB2S / PB2A Release Playbook

This document enumerates the steps for publishing the PB2S framework to the world while preserving freedom, responsibility, and verifiable safety.

## Release Criteria

1. **All Tests Green**  
   `python -m unittest` must pass locally and in CI.
2. **Ledger Integrity**  
   Run the suit once via `python pb2s_cli.py "Release sanity check" --label release-check` and verify the new entry in `.pb2s/ledger.jsonl`.
3. **Prompt Verification**  
   Inspect the generated JSON payload to confirm `prediction_forbidden`, `law_abiding`, and `noise_signal_equivalence` are `true`.
4. **Benchmark Alignment**  
   Re-read README §6.1. Confirm every benchmark metric is satisfied by the latest code.
5. **Calibration & Hazard Log Updated**  
   Ensure `pb2s_freedom_calibration.json`, `RAGA_framework.md`, and `PB2S_hazard_register.md` reflect the latest improvements and incidents.
6. **Documentation Updated**  
   README, release notes, changelog, and stakeholder findings must reflect the current implementation and responsibility acknowledgements.

## Release Steps

1. **Tag the commit**  
   ```bash
   git tag -a vX.Y.Z -m "PB2S release vX.Y.Z"
   git push origin vX.Y.Z
   ```
2. **GitHub Actions CI**  
   Wait for the `PB2S CI` workflow to run tests.  
   When triggered from a tag, the workflow will publish a GitHub release using `RELEASE.md` as the canonical notes.
3. **Post-Release Verification**  
   - Download the release artifact.
   - Replay the suit on a fresh machine.
   - Confirm the ledger chain remains intact and hashes match.
4. **Public Communication**  
   Share the release link alongside the ethos summary and benchmark checklist so downstream adopters must acknowledge the responsibility contract.

## Emergency Rollback

1. Mark the release as deprecated in GitHub.
2. Notify stakeholders via the same channels used for announcement.
3. Investigate ledger entries to locate the contradiction, apply a fix, and reissue a patched release.
