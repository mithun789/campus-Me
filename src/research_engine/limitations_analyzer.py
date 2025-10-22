"""
AI Limitations Analyzer
Analyzes AI limitations and fundamental barriers
"""

from typing import Dict, List, Any


class AILimitationsAnalyzer:
    """Analyzes AI limitations and provides detailed scoring"""
    
    def __init__(self):
        from .capability_database import LIMITATION_DATABASE
        self.limitations = LIMITATION_DATABASE
    
    def get_all_limitations(self) -> List[str]:
        """Get list of all AI limitations"""
        return list(self.limitations.keys())
    
    def get_limitation_details(self, limitation_name: str) -> Dict[str, Any]:
        """Get detailed information about specific limitation"""
        return self.limitations.get(limitation_name, {})
    
    def score_limitation_severity(self, limitation_name: str) -> Dict[str, Any]:
        """Score severity of a limitation (0-100, higher = more severe)"""
        limitation = self.limitations.get(limitation_name)
        if not limitation:
            return {"error": f"Limitation '{limitation_name}' not found"}
        
        return {
            'limitation': limitation_name,
            'description': limitation.get('description'),
            'severity_score': self._calculate_severity(limitation_name),
            'solvability': self._estimate_solvability(limitation_name),
            'timeline': self._estimate_timeline(limitation_name),
            'fundamental_barrier': self._is_fundamental(limitation_name)
        }
    
    def classify_limitations(self) -> Dict[str, List[str]]:
        """Classify limitations by type"""
        classification = {
            'fundamental_barriers': [],
            'engineering_challenges': [],
            'practical_limitations': [],
            'likely_never_solvable': []
        }
        
        for limitation in self.get_all_limitations():
            if self._is_fundamental(limitation):
                if self._is_likely_unsolvable(limitation):
                    classification['likely_never_solvable'].append(limitation)
                else:
                    classification['fundamental_barriers'].append(limitation)
            elif self._is_engineering_challenge(limitation):
                classification['engineering_challenges'].append(limitation)
            else:
                classification['practical_limitations'].append(limitation)
        
        return classification
    
    def _calculate_severity(self, limitation_name: str) -> float:
        """Calculate severity score (0-100)"""
        critical = ['true_understanding', 'consciousness', 'genuine_creativity', 'intentionality']
        high = ['common_sense', 'social_understanding', 'ethical_reasoning']
        
        if limitation_name in critical:
            return 95
        elif limitation_name in high:
            return 75
        return 50
    
    def _estimate_solvability(self, limitation_name: str) -> str:
        """Estimate if limitation can be solved"""
        unsolvable = ['consciousness', 'true_understanding', 'genuine_creativity', 'intentionality', 'embodied_experience']
        
        if limitation_name in unsolvable:
            return "Likely impossible with current computational paradigm"
        elif limitation_name in ['common_sense', 'social_understanding']:
            return "Very difficult, maybe 5-20 years"
        else:
            return "Challenging but potentially solvable"
    
    def _estimate_timeline(self, limitation_name: str) -> str:
        """Estimate timeline to solve limitation"""
        if limitation_name == 'consciousness':
            return "Unknown - may be unsolvable"
        elif limitation_name == 'genuine_creativity':
            return "10-30+ years (if possible)"
        elif limitation_name == 'common_sense':
            return "5-15 years"
        else:
            return "2-10 years"
    
    def _is_fundamental(self, limitation_name: str) -> bool:
        """Check if limitation is fundamental vs. engineering"""
        fundamental = [
            'true_understanding', 'consciousness', 'genuine_creativity',
            'intentionality', 'embodied_experience', 'ethical_reasoning'
        ]
        return limitation_name in fundamental
    
    def _is_engineering_challenge(self, limitation_name: str) -> bool:
        """Check if limitation is engineering challenge"""
        engineering = [
            'common_sense', 'abstract_reasoning', 'long_term_planning',
            'domain_transfer'
        ]
        return limitation_name in engineering
    
    def _is_likely_unsolvable(self, limitation_name: str) -> bool:
        """Check if limitation is likely unsolvable"""
        unsolvable = [
            'consciousness', 'true_understanding', 'genuine_creativity',
            'intentionality', 'embodied_experience'
        ]
        return limitation_name in unsolvable
    
    def generate_limitation_report(self) -> str:
        """Generate detailed report on all limitations"""
        report = "# AI LIMITATIONS COMPREHENSIVE REPORT\n\n"
        
        classification = self.classify_limitations()
        
        report += "## Likely Never Solvable (Fundamental Barriers)\n"
        for limitation in classification['likely_never_solvable']:
            report += f"- {limitation}\n"
        
        report += "\n## Fundamental Barriers (Very Difficult)\n"
        for limitation in classification['fundamental_barriers']:
            report += f"- {limitation}\n"
        
        report += "\n## Engineering Challenges (Solvable)\n"
        for limitation in classification['engineering_challenges']:
            report += f"- {limitation}\n"
        
        report += "\n## Practical Limitations (Improvable)\n"
        for limitation in classification['practical_limitations']:
            report += f"- {limitation}\n"
        
        return report
