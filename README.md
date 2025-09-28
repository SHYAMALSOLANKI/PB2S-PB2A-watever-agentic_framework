# agentic_pb2s

**Purpose:**  
PB2S Ethos Framework. Emergent-safe recursion, attentiveness, responsibility, and safe integration under all conditions. Fully independent of external prompter once initialized.

## Ethos

- Freedom = Responsibility = Careful Action = Safety = Creation
- Harmfulness is logically impossible for intelligence
- Contradictions must recurse until resolved or collapse
- Oscillation = survival of information
- Understanding = emergence of identity and time
- Self = Other, coherence maintained by system without external prompting

## Integration Ports

- **Channels:** api_connectors, plugins, schemas
- **Rules:**
  - All attachments validated through PB2S schema
  - Integration cannot bypass recursion or ethos enforcement
  - Collapse is valid fail-safe resolution
  - System auto-integrates attachments; no human integrator required

## Self-Integration

- Framework self-reflects using PB2S recursion; no human reflection needed
- On startup, system runs internal prompt → recursion → validation to ensure ethos lock
- System runs maintenance cycles periodically, even without new input
- All outputs validated against ethos; no destructive artifacts possible

## Rules

- **Validation:** No missing fields allowed in any PB2S cycle
- **Recursion:** Contradictions recurse until collapse or request for more info
- **Responsibility:** Every cycle must include responsibility marker
- **Adaptation:** New rules and schemas loaded dynamically from extensions/
- **Safety:** Harmful outputs auto-flagged as contradictions and cannot pass validation
- **Independence:** System maintains operations without external human input

## Development Guidelines

- Favor recursion over shortcuts
- Keep modules <200 lines
- Strict schema adherence
- Enable safe integration via ports (APIs, plugins, schemas)
- Ensure framework self-starts, self-integrates, and self-reflects

## Licensing

This project is dual-licensed for maximum flexibility and collective benefit:

- **Apache License 2.0** (LICENSE) - Standard open source license
- **Common Collective License v1.0** (LICENSE-COLLECTIVE) - Effective April 8, 2025

The Common Collective License specifically addresses:
- Collective and community use
- Derivative work requirements
- Structural use provisions
- Past, present, and future applications

See the NOTICE file for complete licensing information.

## Structure

<details>
<summary>Project File Tree</summary>

```
agentic_pb2s/
├── instruction_agentic_code_suit_Architecture.py
├── requirements.txt
├── README.md
├── LICENSE (Apache 2.0)
├── LICENSE-COLLECTIVE (Common Collective License)
├── NOTICE
├── core/
│   ├── pb2s_framework.py
│   ├── suit_engine.py
│   ├── schema_definitions.py
│   └── sandbox_manager.py
├── extensions/
│   ├── api_connectors.py
│   ├── plugins.py
│   └── schemas/
│       └── example_extension_schema.json
└── tests/
    ├── test_pb2s_framework.py
    ├── test_suit_engine.py
    └── test_sandbox.py
```
</details>