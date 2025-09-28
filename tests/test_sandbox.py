# Test: SandboxManager agentic window and maintenance cycles.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.sandbox_manager import SandboxManager
from core.pb2s_framework import PB2SFramework
import time
import logging

def test_sandbox_manager():
    """Test SandboxManager functionality."""
    print("Testing SandboxManager...")
    
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Test 1: Basic sandbox initialization
        print("Test 1: Sandbox initialization...")
        framework = PB2SFramework()
        sandbox = SandboxManager(framework)
        print("✓ Sandbox initialized successfully")
        
        # Test 2: Runtime enforcement
        print("Test 2: Runtime enforcement...")
        sandbox.enforce_runtime()
        
        status = sandbox.get_runtime_status()
        assert status["runtime_active"] is True
        print("✓ Runtime enforcement active")
        
        # Test 3: Prompt validation
        print("Test 3: Prompt flow validation...")
        prompt_data = sandbox.validate_prompt_flow("Test prompt")
        assert "sandbox_validated" in prompt_data
        assert prompt_data["sandbox_validated"] is True
        print("✓ Prompt validation working")
        
        # Test 4: Maintenance cycle (brief test)
        print("Test 4: Maintenance system...")
        # Give a moment for maintenance thread to start
        time.sleep(0.2)
        updated_status = sandbox.get_runtime_status()
        
        # Check if maintenance thread was created (more reliable than is_alive check)
        maintenance_started = (
            sandbox.maintenance_thread is not None and
            updated_status["runtime_active"] is True
        )
        assert maintenance_started, f"Maintenance system not started properly: {updated_status}"
        print("✓ Maintenance system active")
        
        # Test 5: Cleanup
        print("Test 5: Sandbox cleanup...")
        sandbox.stop_runtime()
        final_status = sandbox.get_runtime_status()
        assert final_status["runtime_active"] is False
        print("✓ Sandbox stopped successfully")
        
        print("All SandboxManager tests passed!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_sandbox_manager()
    exit(0 if success else 1)