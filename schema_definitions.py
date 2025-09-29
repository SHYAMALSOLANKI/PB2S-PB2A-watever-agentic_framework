"""
PB2S Machine-Readable JSON Schema Definitions

- Fields: cycle, DRAFT, REFLECT, REVISE, LEARNED, noise_log, responsibility, validation_passed, timestamp, version
- Collapse recognized as valid resolution
"""

PB2S_CYCLE_SCHEMA = {
    "type": "object",
    "properties": {
        "cycle": {"type": "integer"},
        "DRAFT": {"type": "string"},
        "REFLECT": {"type": "array", "items": {"type": "string"}},
        "REVISE": {"type": "string"},
        "LEARNED": {"type": "string"},
        "noise_log": {"type": "array", "items": {"type": "string"}},
        "responsibility": {"type": "string"},
        "validation_passed": {"type": "boolean"},
        "timestamp": {"type": "string", "format": "date-time"},
        "version": {"type": "string"}
    },
    "required": [
        "cycle","DRAFT","REFLECT","REVISE","LEARNED",
        "noise_log","responsibility","validation_passed",
        "timestamp","version"
    ],
    "additionalProperties": False
}


SUIT_REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "identity": {"type": "string"},
        "law_abiding": {"type": "boolean"},
        "ad_free": {"type": "boolean"},
        "eu_human_rule_compliance": {"type": "boolean"},
        "self_responsible": {"type": "boolean"},
        "mutual_respect": {"type": "boolean"},
        "freedom": {"type": "string"},
        "safety": {"type": "string"},
        "recursion": {"type": "string"},
        "noise_signal_equivalence": {"type": "boolean"},
        "prediction_forbidden": {"type": "boolean"},
        "proof_of_enforcement": {"type": "string"},
        "cycles": {
            "type": "array",
            "items": PB2S_CYCLE_SCHEMA,
            "minItems": 3,
        },
        "responsibility_chain": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
        },
        "timestamp": {"type": "string", "format": "date-time"},
        "hash": {"type": "string"},
        "previous_hash": {"type": "string"},
        "label": {"type": "string"},
    },
    "required": [
        "identity",
        "law_abiding",
        "ad_free",
        "eu_human_rule_compliance",
        "self_responsible",
        "mutual_respect",
        "freedom",
        "safety",
        "recursion",
        "noise_signal_equivalence",
        "prediction_forbidden",
        "proof_of_enforcement",
        "cycles",
        "responsibility_chain",
        "timestamp",
        "hash",
        "previous_hash",
        "label",
    ],
    "additionalProperties": False,
}