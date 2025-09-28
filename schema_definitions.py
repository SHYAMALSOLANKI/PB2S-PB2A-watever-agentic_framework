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