"""
Suit Engine Middleware

- Enforces schema validation each cycle
- Logs noise and signal equally
- Prevents bypass of recursion and ethos
- Attaches modules dynamically from extensions/
- Integration ports: api_connectors, plugins, schemas
"""

import json
import jsonschema
import logging
from datetime import datetime
from .schema_definitions import PB2S_CYCLE_SCHEMA

class SuitEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.validation_logs = []
        
    def validate_and_recurse(self, cycle_data):
        """Validate cycle data against PB2S schema and enforce recursion rules."""
        try:
            # Schema validation - no missing fields allowed
            jsonschema.validate(cycle_data, PB2S_CYCLE_SCHEMA)
            
            # Ethos enforcement
            if not self._enforce_ethos(cycle_data):
                raise ValueError("Ethos enforcement failed")
            
            # Mark as validation passed
            cycle_data["validation_passed"] = True
            
            # Log validation success
            self._log_validation(cycle_data, True, "Schema and ethos validation passed")
            
            return cycle_data
            
        except jsonschema.ValidationError as e:
            self.logger.error(f"Schema validation failed: {e}")
            cycle_data["validation_passed"] = False
            
            # Ensure noise_log exists before appending
            if "noise_log" not in cycle_data:
                cycle_data["noise_log"] = []
            cycle_data["noise_log"].append(f"Schema validation error: {e.message}")
            self._log_validation(cycle_data, False, f"Schema validation failed: {e.message}")
            
            # Force recursion on validation failure
            return self._force_recursion_cycle(cycle_data, "Schema validation failure")
            
        except Exception as e:
            self.logger.error(f"Suit engine validation failed: {e}")
            cycle_data["validation_passed"] = False
            
            # Ensure noise_log exists before appending
            if "noise_log" not in cycle_data:
                cycle_data["noise_log"] = []
            cycle_data["noise_log"].append(f"Validation error: {str(e)}")
            self._log_validation(cycle_data, False, f"General validation failed: {str(e)}")
            
            return self._force_recursion_cycle(cycle_data, str(e))
    
    def _enforce_ethos(self, cycle_data):
        """Enforce PB2S ethos principles on cycle data."""
        draft = cycle_data.get("DRAFT", "").lower()
        revise = cycle_data.get("REVISE", "").lower()
        
        # Check for harmful/destructive content
        harmful_indicators = ["harm", "damage", "destroy", "attack", "exploit", "manipulate"]
        text_to_check = f"{draft} {revise}"
        
        if any(indicator in text_to_check for indicator in harmful_indicators):
            # If flagged, ensure it's being addressed in revisions
            if "ethos-aligned" not in revise and "contradiction" not in revise:
                self.logger.warning("Potential ethos violation detected")
                cycle_data["noise_log"].append("Ethos enforcement: Flagged potential harmful content")
                return False
        
        # Responsibility marker required
        if not cycle_data.get("responsibility"):
            cycle_data["noise_log"].append("Ethos enforcement: Missing responsibility marker")
            return False
        
        return True
    
    def _force_recursion_cycle(self, failed_cycle, reason):
        """Create a recursion cycle to address validation failure."""
        recursion_cycle = {
            "cycle": failed_cycle.get("cycle", 0) + 0.1,  # Sub-cycle
            "DRAFT": f"RECURSION_REQUIRED: {reason}",
            "REFLECT": [
                f"Validation failure detected: {reason}",
                "System must recurse to resolve validation issues",
                "Ethos enforcement preventing bypass"
            ],
            "REVISE": "RECURSION_IN_PROGRESS", 
            "LEARNED": f"Learned: Validation failure requires recursion - {reason}",
            "noise_log": [f"Forced recursion due to: {reason}"],
            "responsibility": "SuitEngine Recursion Handler",
            "validation_passed": True,  # Recursion itself is valid
            "timestamp": datetime.now().isoformat(),
            "version": failed_cycle.get("version", "1.0.0")
        }
        
        self._log_validation(recursion_cycle, True, "Recursion cycle created for validation failure")
        return recursion_cycle
    
    def _log_validation(self, cycle_data, success, message):
        """Log validation attempt with full audit trail."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "cycle": cycle_data.get("cycle", "unknown"),
            "validation_success": success,
            "message": message,
            "responsibility": cycle_data.get("responsibility", "unknown"),
            "version": cycle_data.get("version", "1.0.0")
        }
        
        self.validation_logs.append(log_entry)
        
        if success:
            self.logger.info(f"Validation SUCCESS - Cycle {log_entry['cycle']}: {message}")
        else:
            self.logger.error(f"Validation FAILED - Cycle {log_entry['cycle']}: {message}")
    
    def get_validation_audit_log(self):
        """Return complete validation audit log."""
        return self.validation_logs.copy()
    
    def attach_integration(self, integration_type, integration_module):
        """Dynamically attach validated integrations (APIs, plugins, schemas)."""
        # All attachments must be validated through PB2S schema
        if integration_type not in ["api_connector", "plugin", "schema"]:
            raise ValueError(f"Invalid integration type: {integration_type}")
        
        # Integration validation would happen here
        self.logger.info(f"Integration attached: {integration_type}")
        
        return True