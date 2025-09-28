"""
PB2S Agentic Framework

Purpose-Behavior-State-Synthesis (PB2S) Ethos Framework for emergent-safe recursion,
attentiveness, responsibility, and safe integration under all conditions.

Fully independent of external prompter once initialized.
"""

__version__ = "1.0.0"
__author__ = "PB2S Framework Team"
__description__ = "PB2S Ethos Framework for emergent-safe recursive AI systems"

# Import main framework components
try:
    from .core import PB2SFramework, SuitEngine, PB2S_CYCLE_SCHEMA, SandboxManager
except ImportError:
    # Fallback for direct execution
    from core import PB2SFramework, SuitEngine, PB2S_CYCLE_SCHEMA, SandboxManager

__all__ = [
    "PB2SFramework",
    "SuitEngine", 
    "PB2S_CYCLE_SCHEMA",
    "SandboxManager"
]