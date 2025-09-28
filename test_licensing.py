#!/usr/bin/env python3
"""
Test to validate the dual licensing setup for the PB2S-PB2A Agentic Framework.
Tests that required license files are present and contain expected content.
"""
import os
import sys
from datetime import datetime

def test_license_files_exist():
    """Test that all required license files exist."""
    required_files = ['LICENSE', 'LICENSE-COLLECTIVE', 'NOTICE']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"ERROR: Missing license files: {missing_files}")
        return False
    
    print("✓ All required license files present")
    return True

def test_collective_license_content():
    """Test that the collective license contains required content."""
    with open('LICENSE-COLLECTIVE', 'r') as f:
        content = f.read()
    
    required_terms = [
        'April 8, 2025',
        'COMMON COLLECTIVE LICENSE',
        'derivative',
        'structural use',
        'past, present',
        'future'
    ]
    
    missing_terms = []
    for term in required_terms:
        if term.lower() not in content.lower():
            missing_terms.append(term)
    
    if missing_terms:
        print(f"ERROR: Collective license missing required terms: {missing_terms}")
        return False
    
    print("✓ Collective license contains all required terms")
    return True

def test_notice_file_content():
    """Test that the NOTICE file mentions dual licensing."""
    with open('NOTICE', 'r') as f:
        content = f.read()
    
    required_elements = [
        'dual-licensed',
        'Apache License 2.0',
        'Common Collective License',
        'April 8, 2025'
    ]
    
    missing_elements = []
    for element in required_elements:
        if element not in content:
            missing_elements.append(element)
    
    if missing_elements:
        print(f"ERROR: NOTICE file missing required elements: {missing_elements}")
        return False
    
    print("✓ NOTICE file contains all required elements")
    return True

def test_readme_updated():
    """Test that README mentions the dual licensing."""
    with open('README.md', 'r') as f:
        content = f.read()
    
    if 'Licensing' not in content or 'dual-licensed' not in content:
        print("ERROR: README does not mention dual licensing")
        return False
    
    print("✓ README properly updated with licensing information")
    return True

def main():
    """Run all license validation tests."""
    print("Running license validation tests...")
    print("=" * 50)
    
    tests = [
        test_license_files_exist,
        test_collective_license_content,
        test_notice_file_content,
        test_readme_updated
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"ERROR in {test.__name__}: {e}")
            failed += 1
    
    print("=" * 50)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")
    
    if failed == 0:
        print("✓ All license validation tests passed!")
        return 0
    else:
        print("✗ Some license validation tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())