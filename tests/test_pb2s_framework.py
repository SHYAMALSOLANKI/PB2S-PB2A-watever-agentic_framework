# Test: PB2SFramework recursion, self-integration, and ethos enforcement.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.pb2s_framework import PB2SFramework
import logging

def test_pb2s_framework():
    """Test PB2S Framework core functionality."""
    print("Testing PB2S Framework...")
    
    # Set up logging to see the self-integration
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Test 1: Framework initialization and self-integration
        print("Test 1: Framework initialization...")
        framework = PB2SFramework()
        print("✓ Framework initialized and self-integrated successfully")
        
        # Test 2: Basic recursion cycle
        print("Test 2: Basic recursion cycle...")
        result = framework.run("Test input for PB2S processing")
        
        assert result is not None
        assert "cycles" in result
        assert len(result["cycles"]) >= 3  # Minimum 3 cycles
        assert result["ethos_validated"] is True
        print(f"✓ Basic cycle completed with {len(result['cycles'])} cycles")
        
        # Test 3: Contradiction handling
        print("Test 3: Contradiction handling...")
        contradiction_result = framework.run("This is a contradiction that conflicts with itself")
        
        assert contradiction_result is not None
        assert len(contradiction_result["cycles"]) > 3  # Should have recursion cycles
        print(f"✓ Contradiction handled with {len(contradiction_result['cycles'])} cycles")
        
        # Test 4: Schema validation
        print("Test 4: Schema validation...")
        for cycle in result["cycles"]:
            required_fields = ["cycle", "DRAFT", "REFLECT", "REVISE", "LEARNED", 
                             "noise_log", "responsibility", "validation_passed", 
                             "timestamp", "version"]
            for field in required_fields:
                assert field in cycle, f"Missing required field: {field}"
        print("✓ All cycles contain required schema fields")
        
        print("All PB2S Framework tests passed!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_pb2s_framework()
    exit(0 if success else 1)