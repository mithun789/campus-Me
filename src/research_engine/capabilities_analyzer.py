"""
AI Capabilities Analyzer
Analyzes and scores AI capabilities across domains
"""

from typing import Dict, List, Any, Tuple
import json


class AICapabilitiesAnalyzer:
    """Analyzes AI capabilities and provides detailed scoring"""
    
    def __init__(self):
        from .capability_database import CAPABILITY_DATABASE
        self.capabilities = CAPABILITY_DATABASE
    
    def get_all_capabilities(self) -> List[str]:
        """Get list of all AI capabilities"""
        return list(self.capabilities.keys())
    
    def get_capability_details(self, capability_name: str) -> Dict[str, Any]:
        """Get detailed information about specific capability"""
        return self.capabilities.get(capability_name, {})
    
    def score_capability(self, capability_name: str) -> Dict[str, Any]:
        """Score a capability on multiple dimensions"""
        capability = self.capabilities.get(capability_name)
        if not capability:
            return {"error": f"Capability '{capability_name}' not found"}
        
        return {
            'capability': capability_name,
            'description': capability.get('description'),
            'maturity_score': self._calculate_maturity(capability_name),
            'reliability_score': self._calculate_reliability(capability_name),
            'scalability_score': self._calculate_scalability(capability_name),
            'real_world_impact': self._assess_impact(capability_name),
            'examples': capability.get('examples', [])[:3]
        }
    
    def compare_capabilities(self, cap1: str, cap2: str) -> Dict[str, Any]:
        """Compare two capabilities"""
        return {
            'capability_1': self.score_capability(cap1),
            'capability_2': self.score_capability(cap2),
            'comparison': {
                'more_mature': cap1 if self._calculate_maturity(cap1) > self._calculate_maturity(cap2) else cap2,
                'more_reliable': cap1 if self._calculate_reliability(cap1) > self._calculate_reliability(cap2) else cap2,
                'more_impactful': cap1 if self._assess_impact(cap1) > self._assess_impact(cap2) else cap2
            }
        }
    
    def _calculate_maturity(self, capability_name: str) -> float:
        """Score maturity (0-100)"""
        mature = ['pattern_recognition', 'data_analysis', 'task_automation', 'computer_vision']
        if capability_name in mature:
            return 95
        return 70
    
    def _calculate_reliability(self, capability_name: str) -> float:
        """Score reliability (0-100)"""
        reliable = ['data_analysis', 'logical_reasoning', 'task_automation']
        if capability_name in reliable:
            return 95
        return 75
    
    def _calculate_scalability(self, capability_name: str) -> float:
        """Score scalability (0-100)"""
        return 90  # Most AI capabilities scale well
    
    def _assess_impact(self, capability_name: str) -> float:
        """Assess real-world impact (0-100)"""
        high_impact = ['computer_vision', 'task_automation', 'content_generation']
        if capability_name in high_impact:
            return 85
        return 70
