"""
PB2S Machine-Readable JSON Schema Definitions

- Fields: cycle, DRAFT, REFLECT, REVISE, LEARNED, noise_log, responsibility, validation_passed, timestamp, version
- Collapse recognized as valid resolution
"""

PB2S_CYCLE_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "PB2S Cycle Schema",
    "description": "Schema for PB2S recursion cycle data with all required fields",
    "type": "object",
    "properties": {
        "cycle": {
            "type": ["integer", "number"],
            "description": "Cycle number (integer or decimal for sub-cycles)"
        },
        "DRAFT": {
            "type": "string",
            "description": "Initial draft content for the cycle"
        },
        "REFLECT": {
            "type": "array", 
            "items": {"type": "string"},
            "description": "Array of reflection statements"
        },
        "REVISE": {
            "type": "string",
            "description": "Revised content based on reflections"
        },
        "LEARNED": {
            "type": "string",
            "description": "Learning extracted from the cycle"
        },
        "noise_log": {
            "type": "array", 
            "items": {"type": "string"},
            "description": "Log of noise, errors, and system messages"
        },
        "responsibility": {
            "type": "string",
            "description": "Responsibility marker identifying the cycle handler"
        },
        "validation_passed": {
            "type": "boolean",
            "description": "Whether the cycle passed validation"
        },
        "timestamp": {
            "type": "string", 
            "format": "date-time",
            "description": "ISO 8601 timestamp of cycle execution"
        },
        "version": {
            "type": "string",
            "description": "PB2S framework version"
        }
    },
    "required": [
        "cycle", "DRAFT", "REFLECT", "REVISE", "LEARNED",
        "noise_log", "responsibility", "validation_passed", 
        "timestamp", "version"
    ],
    "additionalProperties": False
}

# Schema for PB2S session results
PB2S_SESSION_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "PB2S Session Schema", 
    "description": "Schema for complete PB2S session results",
    "type": "object",
    "properties": {
        "session_id": {"type": "string"},
        "cycles": {
            "type": "array",
            "items": PB2S_CYCLE_SCHEMA
        },
        "final_output": {"type": ["string", "null"]},
        "total_cycles": {"type": "integer"},
        "ethos_validated": {"type": "boolean"},
        "timestamp": {"type": "string", "format": "date-time"}
    },
    "required": ["session_id", "cycles", "total_cycles", "ethos_validated", "timestamp"],
    "additionalProperties": False
}

# Valid collapse resolutions
COLLAPSE_RESOLUTIONS = [
    "CONTRADICTION_UNRESOLVABLE",
    "MAXIMUM_RECURSION_REACHED", 
    "ETHOS_VIOLATION_TERMINAL",
    "SCHEMA_VALIDATION_IMPOSSIBLE",
    "SYSTEM_INTEGRITY_FAILURE"
]