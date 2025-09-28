# Test: SuitEngine validation, recursion, and integration port logic.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.suit_engine import SuitEngine
from datetime import datetime
import logging

def test_suit_engine():
    """Test SuitEngine validation and recursion functionality."""
    print("Testing SuitEngine...")
    
    logging.basicConfig(level=logging.INFO)
    engine = SuitEngine()
    
    try:
        # Test 1: Valid cycle validation
        print("Test 1: Valid cycle validation...")
        valid_cycle = {
            "cycle": 1,
            "DRAFT": "Test draft content",
            "REFLECT": ["Reflection 1", "Reflection 2"],
            "REVISE": "Revised content",
            "LEARNED": "Test learning",
            "noise_log": [],
            "responsibility": "Test Suite",
            "validation_passed": False,  # Will be set by engine
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        }
        
        validated = engine.validate_and_recurse(valid_cycle)
        assert validated["validation_passed"] is True
        print("✓ Valid cycle passed validation")
        
        # Test 2: Invalid cycle (missing field)
        print("Test 2: Invalid cycle handling...")
        invalid_cycle = {
            "cycle": 1,
            "DRAFT": "Test draft",
            "REFLECT": ["Reflection"],
            # Missing required fields
            "responsibility": "Test Suite"
        }
        
        result = engine.validate_and_recurse(invalid_cycle)
        # Should create a recursion cycle
        assert "RECURSION" in result["DRAFT"]
        print("✓ Invalid cycle triggered recursion")
        
        # Test 3: Audit log
        print("Test 3: Audit log functionality...")
        audit_log = engine.get_validation_audit_log()
        assert len(audit_log) > 0
        print(f"✓ Audit log contains {len(audit_log)} entries")
        
        # Test 4: Integration attachment
        print("Test 4: Integration attachment...")
        success = engine.attach_integration("plugin", {"name": "test_plugin"})
        assert success is True
        print("✓ Integration attachment successful")
        
        print("All SuitEngine tests passed!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_suit_engine()
    exit(0 if success else 1)