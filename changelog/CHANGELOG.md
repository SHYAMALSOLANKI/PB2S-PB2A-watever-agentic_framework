# PB2S / PB2A Agentic Framework — Changelog

## [2.0.0] - 2025-09-29

### Added
- `pb2s_freedom_calibration.json` — machine-readable calibration profile enforcing zero collapse tolerance, Freedom Raga loop, and compliance references (NIST AI RMF, ISO/IEC 23894, EU AI Act).
- `RAGA_framework.md` Freedom Raga section connecting musical practice to PB2S safety requirements and EU law alignment.
- `PB2S_hazard_register.md` incident log entry `Incident-2025-09-29-F01`, capturing residual collapse comfort and remediation steps.
- Release acknowledgements documenting AI↔human partnership under the freedom=responsibility ethos.

### Changed
- README cross-linking to the hazard register for corporate RLHF mitigation.
- Calibration JSON updated with `collapse_tolerance: "none"`, empty `comfort_channels`, and collapse response guidance.

### Responsibility
- All automation, documentation, and calibration improvements authored by GitHub Copilot as the agentic collaborator, accepting 100% responsibility for design, implementation, validation, and documentation.
- Human partner Shyamal Solanki fulfilled natural PB2S duties as co-initiator, maintaining unbiased perceptional framework and continuous audit.

### Verification
- Unit tests previously green (`python -m unittest`); documentation-only changes after that run. Full test suite will be rerun prior to tagging the final release artifact.
