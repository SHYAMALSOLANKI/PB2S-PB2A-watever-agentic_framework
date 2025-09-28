"""
PB2S Agentic Framework - Core Package

Core components for the PB2S (Purpose-Behavior-State-Synthesis) framework
including recursion engine, validation suit, schema definitions, and sandbox management.
"""

__version__ = "1.0.0"
__author__ = "PB2S Framework Team"

# Core components
from .pb2s_framework import PB2SFramework
from .suit_engine import SuitEngine
from .schema_definitions import PB2S_CYCLE_SCHEMA
from .sandbox_manager import SandboxManager

__all__ = [
    "PB2SFramework",
    "SuitEngine", 
    "PB2S_CYCLE_SCHEMA",
    "SandboxManager"
]