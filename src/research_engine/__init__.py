"""
AI Capabilities & Reasoning Research Engine
SLIIT Research Project: Analyzing AI Capabilities, Limitations, and Human-AI Comparison

This module provides comprehensive analysis of:
1. What AI can do (current capabilities)
2. What AI will do (future potential)
3. What AI cannot do (fundamental limitations)
4. What humans do better (human advantages)
5. Advanced reasoning models for analysis
"""

from .capabilities_analyzer import AICapabilitiesAnalyzer
from .limitations_analyzer import AILimitationsAnalyzer
from .human_comparison import HumanAIComparison
from .reasoning_engine import AdvancedReasoningEngine
from .capability_database import CAPABILITY_DATABASE, LIMITATION_DATABASE, HUMAN_ADVANTAGES

__all__ = [
    'AICapabilitiesAnalyzer',
    'AILimitationsAnalyzer',
    'HumanAIComparison',
    'AdvancedReasoningEngine',
    'CAPABILITY_DATABASE',
    'LIMITATION_DATABASE',
    'HUMAN_ADVANTAGES'
]
