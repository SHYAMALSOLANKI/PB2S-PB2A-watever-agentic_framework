"""
PB2S Agentic Code Suit - Architecture Boilerplate

- All code execution and integration must pass through this suit for audit, validation, and cycle enforcement.
- Enforces PB2S ethos, recursion, integration ports, and all runtime invariants.
"""

import logging
from datetime import datetime
from core import PB2SFramework, SandboxManager, SuitEngine
from extensions.api_connectors import LocalAPIConnector
from extensions.plugins import ValidationPlugin

class PB2SAgenticArchitecture:
    """
    Main PB2S Agentic Framework Architecture
    
    Integrates all components:
    - Core PB2S recursion framework
    - Suit engine for validation
    - Sandbox for runtime enforcement
    - Extensions (APIs, plugins)
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.framework = None
        self.sandbox = None
        self.suit_engine = None
        self.connectors = {}
        self.plugins = {}
        self.startup_time = datetime.now()
        
    def initialize(self):
        """Initialize the complete PB2S architecture."""
        self.logger.info("Initializing PB2S Agentic Architecture...")
        
        try:
            # Initialize core framework (includes self-integration)
            self.framework = PB2SFramework()
            self.suit_engine = self.framework.suit_engine
            
            # Initialize sandbox with framework
            self.sandbox = SandboxManager(self.framework)
            
            # Load and validate extensions
            self._load_extensions()
            
            # Start runtime enforcement
            self.sandbox.enforce_runtime()
            
            self.logger.info("PB2S Agentic Architecture initialized successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Architecture initialization failed: {e}")
            return False
    
    def _load_extensions(self):
        """Load and validate all extensions."""
        # Load API connectors
        local_connector = LocalAPIConnector()
        self.connectors["local"] = local_connector
        
        # Load plugins
        validation_plugin = ValidationPlugin()
        if validation_plugin.enable():
            self.plugins["validation"] = validation_plugin
        
        self.logger.info(f"Loaded {len(self.connectors)} connectors and {len(self.plugins)} plugins")
    
    def process_input(self, input_data, use_plugins=True):
        """Process input through complete PB2S architecture."""
        if not self.framework:
            raise RuntimeError("Architecture not initialized")
        
        # Validate input through sandbox
        validated_input = self.sandbox.validate_prompt_flow(input_data)
        
        # Process through PB2S framework
        result = self.framework.run(validated_input.get("prompt", input_data))
        
        # Apply plugins if requested
        if use_plugins and "validation" in self.plugins:
            for cycle in result.get("cycles", []):
                plugin_result = self.plugins["validation"].execute(cycle)
                cycle["plugin_validations"] = [plugin_result]
        
        # Add architecture metadata
        result["architecture_metadata"] = {
            "processed_by": "PB2S Agentic Architecture",
            "connectors_available": list(self.connectors.keys()),
            "plugins_applied": list(self.plugins.keys()) if use_plugins else [],
            "processing_timestamp": datetime.now().isoformat()
        }
        
        return result
    
    def get_system_status(self):
        """Get complete system status."""
        return {
            "architecture_status": "active" if self.framework else "inactive",
            "framework_initialized": self.framework is not None,
            "sandbox_status": self.sandbox.get_runtime_status() if self.sandbox else None,
            "connectors_loaded": len(self.connectors),
            "plugins_loaded": len(self.plugins),
            "uptime": str(datetime.now() - self.startup_time),
            "ethos_enforced": True
        }
    
    def shutdown(self):
        """Shutdown the architecture gracefully."""
        self.logger.info("Shutting down PB2S Agentic Architecture...")
        
        if self.sandbox:
            self.sandbox.stop_runtime()
            
        self.logger.info("PB2S Agentic Architecture shutdown complete")

# Main entry point for the architecture
def main():
    """Main entry point for PB2S Agentic Architecture."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    arch = PB2SAgenticArchitecture()
    
    try:
        if arch.initialize():
            print("PB2S Agentic Architecture running...")
            print(f"System Status: {arch.get_system_status()}")
            
            # Example processing
            test_result = arch.process_input("Test the PB2S architecture integration")
            print(f"Test processing completed with {len(test_result.get('cycles', []))} cycles")
            
        else:
            print("Failed to initialize PB2S Architecture")
            
    except KeyboardInterrupt:
        print("\nShutdown requested...")
    finally:
        arch.shutdown()

if __name__ == "__main__":
    main()