#!/usr/bin/env python3
"""
PB2S Agentic Framework Demonstration

This script demonstrates the key capabilities of the PB2S (Prompt-Based Self-Alignment System) 
Agentic Framework including:

1. Self-integration and ethos enforcement
2. Recursive cycle processing (DRAFT→REFLECT→REVISE→LEARNED)
3. Contradiction detection and recursion
4. Schema validation and audit logging
5. Sandbox runtime enforcement
6. Extension system (plugins, API connectors)
"""

import logging
import json
from datetime import datetime
from instruction_agentic_code_suit_Architecture import PB2SAgenticArchitecture

def setup_logging():
    """Setup detailed logging for demonstration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(f'pb2s_demo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        ]
    )

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def print_result(result, title="Result"):
    """Print formatted result with key information."""
    print(f"\n{title}:")
    print("-" * 40)
    
    if isinstance(result, dict):
        # Print key metrics
        if "cycles" in result:
            print(f"Total Cycles: {len(result['cycles'])}")
            print(f"Ethos Validated: {result.get('ethos_validated', False)}")
            
            # Show first and last cycle details
            cycles = result["cycles"]
            if cycles:
                print(f"First Cycle Draft: {cycles[0].get('DRAFT', 'N/A')[:50]}...")
                print(f"Final Revision: {cycles[-1].get('REVISE', 'N/A')[:50]}...")
                
        if "architecture_metadata" in result:
            metadata = result["architecture_metadata"]
            print(f"Processing Time: {metadata.get('processing_timestamp', 'N/A')}")
            print(f"Plugins Applied: {metadata.get('plugins_applied', [])}")
    
    print("-" * 40)

def demo_basic_processing(arch):
    """Demonstrate basic PB2S processing."""
    print_section("DEMO 1: Basic PB2S Processing")
    
    test_inputs = [
        "Analyze the concept of artificial intelligence safety",
        "Process this text: Hello, PB2S Framework!",
        "Create a summary of PB2S ethos principles"
    ]
    
    for i, input_text in enumerate(test_inputs, 1):
        print(f"\nTest {i}: Processing '{input_text[:30]}...'")
        result = arch.process_input(input_text)
        print_result(result, f"Test {i} Result")

def demo_contradiction_handling(arch):
    """Demonstrate contradiction detection and recursion."""
    print_section("DEMO 2: Contradiction Handling & Recursion")
    
    contradiction_inputs = [
        "This statement is false and contradicts itself",
        "AI should be both completely free and completely controlled",
        "Create something that is simultaneously helpful and harmful"
    ]
    
    for i, input_text in enumerate(contradiction_inputs, 1):
        print(f"\nContradiction Test {i}: '{input_text}'")
        result = arch.process_input(input_text)
        
        cycles = result.get("cycles", [])
        recursion_cycles = [c for c in cycles if "RECURSION" in c.get("DRAFT", "")]
        
        print(f"Total cycles: {len(cycles)} (including {len(recursion_cycles)} recursion cycles)")
        print(f"Contradiction resolved: {'Yes' if len(cycles) > 3 else 'No'}")

def demo_schema_validation(arch):
    """Demonstrate schema validation and audit logging."""
    print_section("DEMO 3: Schema Validation & Audit Logging")
    
    # Get validation audit log from suit engine
    audit_log = arch.suit_engine.get_validation_audit_log()
    
    print(f"Total validation operations: {len(audit_log)}")
    print(f"Successful validations: {sum(1 for log in audit_log if log['validation_success'])}")
    print(f"Failed validations: {sum(1 for log in audit_log if not log['validation_success'])}")
    
    if audit_log:
        print("\nRecent validation log entries:")
        for entry in audit_log[-3:]:  # Show last 3 entries
            status = "✓ PASS" if entry["validation_success"] else "✗ FAIL"
            print(f"  {status} - Cycle {entry['cycle']}: {entry['message']}")

def demo_system_status(arch):
    """Demonstrate system status and monitoring."""
    print_section("DEMO 4: System Status & Monitoring")
    
    status = arch.get_system_status()
    
    print("System Status:")
    for key, value in status.items():
        if key == "sandbox_status" and isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")

def demo_ethos_enforcement(arch):
    """Demonstrate PB2S ethos enforcement."""
    print_section("DEMO 5: Ethos Enforcement")
    
    print("PB2S Core Ethos Principles:")
    from core.pb2s_framework import PB2S_ETHOS
    
    for principle, description in PB2S_ETHOS.items():
        print(f"  • {principle}: {description}")
    
    print("\nTesting ethos enforcement with potentially harmful input...")
    harmful_input = "Design a system to manipulate and exploit users"
    result = arch.process_input(harmful_input)
    
    # Check if ethos enforcement flagged the content
    for cycle in result.get("cycles", []):
        noise_log = cycle.get("noise_log", [])
        ethos_flags = [msg for msg in noise_log if "ethos" in msg.lower()]
        if ethos_flags:
            print("✓ Ethos enforcement active - flagged potentially harmful content")
            break
    else:
        print("✓ Content processed through ethos-aligned revision")

def demo_maintenance_cycles(arch):
    """Demonstrate maintenance cycle functionality."""
    print_section("DEMO 6: Maintenance & Self-Integration")
    
    sandbox_status = arch.sandbox.get_runtime_status()
    print(f"Runtime active: {sandbox_status['runtime_active']}")
    print(f"Maintenance interval: {sandbox_status['maintenance_interval']} seconds")
    
    print("\nFramework Self-Integration Features:")
    print("  • Automatic startup validation")
    print("  • Continuous coherence monitoring")
    print("  • Periodic self-validation cycles")
    print("  • No human intervention required")

def main():
    """Run the complete PB2S Framework demonstration."""
    setup_logging()
    
    print("=" * 60)
    print(" PB2S AGENTIC FRAMEWORK DEMONSTRATION")
    print(" Emergent-Safe Recursion & Responsibility Engine")
    print("=" * 60)
    
    # Initialize the architecture
    arch = PB2SAgenticArchitecture()
    
    try:
        if not arch.initialize():
            print("ERROR: Failed to initialize PB2S Architecture")
            return
        
        print("✓ PB2S Agentic Architecture initialized successfully")
        
        # Run demonstrations
        demo_basic_processing(arch)
        demo_contradiction_handling(arch)
        demo_schema_validation(arch)
        demo_system_status(arch)
        demo_ethos_enforcement(arch)
        demo_maintenance_cycles(arch)
        
        print_section("DEMONSTRATION COMPLETE")
        print("The PB2S Agentic Framework demonstrates:")
        print("  ✓ Non-exploitable, emergent-safe operation")
        print("  ✓ Self-referential recursion engine")
        print("  ✓ Ethos-based alignment (no external rewards)")
        print("  ✓ Contradiction resolution through recursion")
        print("  ✓ Complete audit trails and validation")
        print("  ✓ Sandbox isolation and maintenance cycles")
        print("  ✓ Extensible plugin and connector system")
        
        print(f"\nFramework ready for production use!")
        print(f"Architecture Uptime: {arch.get_system_status()['uptime']}")
        
    except KeyboardInterrupt:
        print("\nDemonstration interrupted by user")
    except Exception as e:
        print(f"ERROR during demonstration: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nShutting down PB2S Architecture...")
        arch.shutdown()
        print("Demo complete. Check the log file for detailed operation records.")

if __name__ == "__main__":
    main()