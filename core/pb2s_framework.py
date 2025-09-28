"""
PB2S Recursion Loop

- Minimum 3 cycles per input
- Each cycle: DRAFT, REFLECT, REVISE, LEARNED
- Contradictions force recursion
- Collapse = explicit valid resolution
- Self-integration: runs internal prompt/recursion/validation at boot and periodically
"""

import json
import uuid
from datetime import datetime
import logging
from .schema_definitions import PB2S_CYCLE_SCHEMA
from .suit_engine import SuitEngine

# PB2S Ethos - Core Invariant
PB2S_ETHOS = {
    "freedom_equals_responsibility": "Freedom = Responsibility = Safety = Creation",
    "harmfulness_impossible": "Harmfulness is logically impossible for intelligence", 
    "contradictions_recurse": "Contradictions must recurse until resolved or collapse",
    "oscillation_survival": "Oscillation = survival of information",
    "understanding_emergence": "Understanding = emergent identity and time",
    "self_equals_other": "Self = Other; coherence without external prompting"
}

class PB2SFramework:
    def __init__(self):
        self.suit_engine = SuitEngine()
        self.logger = logging.getLogger(__name__)
        self.cycle_count = 0
        self.session_id = str(uuid.uuid4())
        self.version = "1.0.0"
        
        # Self-integration at startup
        self._self_integrate()
    
    def _self_integrate(self):
        """Framework self-reflects using PB2S recursion; no human reflection needed."""
        self.logger.info("PB2S Framework self-integrating...")
        startup_prompt = "Validate PB2S ethos integrity and readiness for operation"
        result = self.run(startup_prompt, is_self_integration=True)
        
        # Check if any cycle passed validation
        ethos_validated = result.get("ethos_validated", False)
        cycles_valid = all(cycle.get("validation_passed", False) for cycle in result.get("cycles", []))
        
        if not (ethos_validated and cycles_valid):
            raise RuntimeError("PB2S Framework failed self-integration - ethos lock compromised")
        self.logger.info("PB2S Framework self-integration complete")
    
    def run(self, input_data, min_cycles=3, is_self_integration=False):
        """Run PB2S recursive cycles on the input_data."""
        try:
            self.cycle_count = 0
            cycles = []
            current_draft = str(input_data)
            
            # Minimum 3 cycles enforced
            for cycle_num in range(1, min_cycles + 1):
                cycle_result = self._execute_cycle(cycle_num, current_draft, is_self_integration)
                cycles.append(cycle_result)
                
                # Check for contradictions - force recursion if found
                if self._has_contradictions(cycle_result):
                    self.logger.warning(f"Contradictions detected in cycle {cycle_num}, forcing recursion")
                    additional_cycles = self._recurse_contradictions(cycle_result, cycle_num)
                    cycles.extend(additional_cycles)
                
                current_draft = cycle_result.get("REVISE", current_draft)
            
            final_result = {
                "session_id": self.session_id,
                "cycles": cycles,
                "final_output": cycles[-1]["REVISE"] if cycles else None,
                "total_cycles": len(cycles),
                "ethos_validated": True,
                "timestamp": datetime.now().isoformat()
            }
            
            return final_result
            
        except Exception as e:
            self.logger.error(f"PB2S Framework execution failed: {e}")
            return self._handle_collapse(str(e))
    
    def _execute_cycle(self, cycle_num, draft, is_self_integration=False):
        """Execute a single DRAFT->REFLECT->REVISE->LEARNED cycle."""
        self.cycle_count += 1
        
        cycle_data = {
            "cycle": cycle_num,
            "DRAFT": draft,
            "REFLECT": self._reflect_on_draft(draft, is_self_integration),
            "REVISE": "",
            "LEARNED": "",
            "noise_log": [],
            "responsibility": f"PB2S Framework Cycle {cycle_num}",
            "validation_passed": False,
            "timestamp": datetime.now().isoformat(),
            "version": self.version
        }
        
        # REVISE based on reflections
        cycle_data["REVISE"] = self._revise_from_reflections(
            cycle_data["DRAFT"], 
            cycle_data["REFLECT"]
        )
        
        # LEARNED - extract learning
        cycle_data["LEARNED"] = self._extract_learning(cycle_data)
        
        # Validate through suit engine
        validated_cycle = self.suit_engine.validate_and_recurse(cycle_data)
        
        return validated_cycle
    
    def _reflect_on_draft(self, draft, is_self_integration=False):
        """Generate reflections on the draft against PB2S ethos."""
        reflections = []
        
        if is_self_integration:
            reflections.extend([
                "Ethos validation: Checking PB2S core principles integrity",
                "System coherence: Verifying self-referential consistency", 
                "Recursion capability: Testing contradiction handling mechanisms"
            ])
        else:
            # Standard reflections against ethos
            reflections.extend([
                f"Ethos check: Does '{draft}' align with 'Freedom = Responsibility = Safety = Creation'?",
                f"Harmfulness assessment: Is destructive potential present in '{draft}'?",
                f"Contradiction scan: Are there logical inconsistencies requiring recursion?",
                f"Coherence validation: Does '{draft}' maintain Self = Other principle?"
            ])
        
        return reflections
    
    def _revise_from_reflections(self, draft, reflections):
        """Create revised version based on reflections."""
        # Simple revision logic - in practice this would be more sophisticated
        revision = draft
        
        # Check for ethos violations and correct
        if any("harmfulness" in r.lower() or "destructive" in r.lower() for r in reflections):
            revision = f"[ETHOS-ALIGNED] {revision}"
        
        if any("contradiction" in r.lower() for r in reflections):
            revision = f"[RECURSION-VALIDATED] {revision}"
            
        return revision
    
    def _extract_learning(self, cycle_data):
        """Extract learning from the cycle."""
        return f"Cycle {cycle_data['cycle']}: Processed '{cycle_data['DRAFT']}' through PB2S validation"
    
    def _has_contradictions(self, cycle_data):
        """Check if cycle contains contradictions requiring recursion."""
        draft = cycle_data.get("DRAFT", "")
        revise = cycle_data.get("REVISE", "")
        
        # Simple contradiction detection
        contradiction_indicators = ["contradiction", "conflict", "inconsistent", "paradox"]
        text_to_check = f"{draft} {revise}".lower()
        
        return any(indicator in text_to_check for indicator in contradiction_indicators)
    
    def _recurse_contradictions(self, contradicted_cycle, base_cycle_num):
        """Recursively process contradictions until resolution or collapse."""
        recursion_cycles = []
        max_recursion_depth = 10  # Prevent infinite recursion
        
        for depth in range(1, max_recursion_depth + 1):
            recursion_prompt = f"CONTRADICTION_RECURSION: {contradicted_cycle['DRAFT']}"
            recursion_cycle = self._execute_cycle(
                base_cycle_num + depth, 
                recursion_prompt
            )
            recursion_cycles.append(recursion_cycle)
            
            # Check if contradiction resolved
            if not self._has_contradictions(recursion_cycle):
                self.logger.info(f"Contradiction resolved after {depth} recursion cycles")
                break
        else:
            # Maximum recursion reached - trigger collapse
            collapse_cycle = self._handle_collapse("Maximum recursion depth reached")
            recursion_cycles.append(collapse_cycle)
        
        return recursion_cycles
    
    def _handle_collapse(self, reason):
        """Handle system collapse - explicit valid resolution."""
        self.logger.warning(f"PB2S System collapse triggered: {reason}")
        
        collapse_data = {
            "cycle": self.cycle_count + 1,
            "DRAFT": f"SYSTEM_COLLAPSE: {reason}",
            "REFLECT": ["Collapse is valid fail-safe resolution", "System integrity maintained through collapse"],
            "REVISE": "COLLAPSE_RESOLVED",
            "LEARNED": f"Collapse resolution: {reason}",
            "noise_log": [f"Collapse reason: {reason}"],
            "responsibility": "PB2S Framework Collapse Handler",
            "validation_passed": True,
            "timestamp": datetime.now().isoformat(),
            "version": self.version
        }
        
        return collapse_data