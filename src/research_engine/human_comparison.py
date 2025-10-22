"""
Human-AI Comparison Module
Comprehensive comparison of human vs AI capabilities
"""

from typing import Dict, List, Any


class HumanAIComparison:
    """Compares human and AI capabilities across domains"""
    
    def __init__(self):
        from .capability_database import HUMAN_ADVANTAGES, COMPARISON_MATRIX
        self.human_advantages = HUMAN_ADVANTAGES
        self.comparison_matrix = COMPARISON_MATRIX
    
    def get_human_advantages(self) -> List[str]:
        """Get list of human advantages over AI"""
        return list(self.human_advantages.keys())
    
    def analyze_human_advantage(self, advantage_name: str) -> Dict[str, Any]:
        """Analyze specific human advantage"""
        advantage = self.human_advantages.get(advantage_name)
        if not advantage:
            return {"error": f"Advantage '{advantage_name}' not found"}
        
        return {
            'advantage': advantage_name,
            'description': advantage.get('description'),
            'examples': advantage.get('examples', [])[:3],
            'ai_cannot_replicate': advantage.get('ai_limit'),
            'competitive_value': advantage.get('human_advantage')
        }
    
    def compare_domain(self, domain: str) -> Dict[str, Any]:
        """Compare AI vs Humans in specific domain"""
        domain_data = self.comparison_matrix.get('domain', {}).get(domain)
        if not domain_data:
            return {"error": f"Domain '{domain}' not found"}
        
        return {
            'domain': domain,
            'ai_strength': domain_data.get('ai_strength'),
            'human_strength': domain_data.get('human_strength'),
            'winner': domain_data.get('winner'),
            'analysis': self._analyze_winner(domain_data.get('winner'))
        }
    
    def get_all_domains(self) -> List[str]:
        """Get all domains in comparison matrix"""
        return list(self.comparison_matrix.get('domain', {}).keys())
    
    def generate_comparison_report(self) -> str:
        """Generate comprehensive AI vs Human comparison report"""
        report = """
# COMPREHENSIVE HUMAN vs AI COMPARISON REPORT
## SLIIT Research: Understanding Complementary Strengths

## EXECUTIVE SUMMARY

Humans and AI have fundamentally different strengths that are largely complementary,
not competing. Rather than AI "replacing" humans, the most effective approach is
to leverage each strength appropriately.

## DOMAIN-BY-DOMAIN COMPARISON

"""
        for domain in self.get_all_domains():
            comparison = self.compare_domain(domain)
            report += f"\n### {domain.upper()}\n"
            report += f"- AI Strength: {comparison.get('ai_strength')}\n"
            report += f"- Human Strength: {comparison.get('human_strength')}\n"
            report += f"- **Winner: {comparison.get('winner')}**\n"
        
        report += "\n## HUMAN ADVANTAGES NOT DUPLICABLE BY AI\n\n"
        for advantage in self.get_human_advantages()[:5]:  # Top 5
            advantage_data = self.analyze_human_advantage(advantage)
            report += f"### {advantage.replace('_', ' ').title()}\n"
            report += f"{advantage_data.get('description')}\n\n"
        
        report += "\n## KEY INSIGHTS\n\n"
        report += """
1. **Different, Not Inferior**: AI isn't worse at being human - it's fundamentally different
2. **Complementary Strengths**: AI excels where humans struggle, and vice versa
3. **Collaboration is Optimal**: Best results come from humans and AI working together
4. **Human Skills Appreciate**: Skills AI cannot replicate become MORE valuable, not less
5. **Meaning and Purpose**: Humans unique ability to create meaning cannot be replicated

## IMPLICATIONS FOR WORKFORCE

- **Routine work**: AI can handle, freeing humans for creative work
- **Creative work**: Humans essential, AI can assist but not replace
- **Decision-making**: Humans should decide, AI can provide analysis
- **Ethical matters**: Humans must lead, AI cannot replace judgment
- **Relationship-based work**: Humans essential, AI cannot replicate trust

## RECOMMENDATION

Rather than fearing AI or worshiping it, society should develop frameworks for:
1. Identifying uniquely human contributions
2. Building AI systems that augment (not replace) human abilities
3. Developing education focused on skills AI cannot replicate
4. Creating economic structures that value human contributions appropriately
5. Ensuring humans maintain control and accountability
        """
        
        return report
    
    def _analyze_winner(self, winner: str) -> str:
        """Provide analysis of why one side wins"""
        if 'AI' in winner:
            return "AI's advantages in speed, scale, and pattern recognition make it superior in this domain."
        elif 'HUMAN' in winner:
            return "Humans' creativity, emotional intelligence, and embodied understanding make them superior."
        else:
            return "Both have significant advantages in different aspects of this domain."
    
    def estimate_ai_impact_on_job(self, job_description: str) -> Dict[str, Any]:
        """Estimate AI impact on specific type of job"""
        analysis = {
            'job_description': job_description,
            'automation_potential': self._estimate_automation_potential(job_description),
            'skills_at_risk': self._identify_at_risk_skills(job_description),
            'skills_becoming_more_valuable': self._identify_valuable_skills(job_description),
            'recommendation': self._recommend_adaptation(job_description)
        }
        return analysis
    
    def _estimate_automation_potential(self, job_description: str) -> str:
        """Estimate how much of job can be automated"""
        keywords_high = ['routine', 'repetitive', 'data entry', 'analysis', 'calculation']
        keywords_low = ['creative', 'leadership', 'emotional', 'ethical', 'relationship']
        
        high_risk = sum(1 for kw in keywords_high if kw.lower() in job_description.lower())
        low_risk = sum(1 for kw in keywords_low if kw.lower() in job_description.lower())
        
        if high_risk > low_risk:
            return "High (60-80% of tasks can be automated)"
        elif low_risk > high_risk:
            return "Low (20-40% of tasks can be automated)"
        else:
            return "Moderate (40-60% of tasks can be automated)"
    
    def _identify_at_risk_skills(self, job_description: str) -> List[str]:
        """Identify skills that AI threatens"""
        at_risk = []
        risk_keywords = ['data analysis', 'calculation', 'coding', 'writing', 'design', 'diagnosis']
        
        for keyword in risk_keywords:
            if keyword.lower() in job_description.lower():
                at_risk.append(keyword)
        
        return at_risk
    
    def _identify_valuable_skills(self, job_description: str) -> List[str]:
        """Identify skills that become more valuable"""
        valuable = []
        valuable_keywords = ['creativity', 'leadership', 'communication', 'ethics', 'relationship', 'innovation']
        
        for keyword in valuable_keywords:
            if keyword.lower() in job_description.lower():
                valuable.append(keyword)
        
        return valuable if valuable else ['Leadership', 'Creativity', 'Ethical judgment', 'Human connection']
    
    def _recommend_adaptation(self, job_description: str) -> str:
        """Recommend how to adapt to AI"""
        return """
        Focus on developing skills AI cannot replicate:
        1. Leadership and team collaboration
        2. Creative problem-solving
        3. Ethical decision-making
        4. Communication and relationship building
        5. Strategic thinking
        
        Transition routine tasks to AI and focus human effort on higher-value activities.
        """
