"""
Visualization AI - AI-driven visualization selection and recommendations
"""

from typing import Dict, List


class VisualizationAI:
    """Recommend visualizations based on content analysis."""

    def recommend_visualizations(self, text: str) -> Dict[str, List[str]]:
        """Recommend visualization types based on content."""
        recommendations = {"charts": [], "tables": [], "diagrams": []}

        text_lower = text.lower()

        # Detect chart opportunities
        if any(word in text_lower for word in ["compare", "comparison", "different"]):
            recommendations["charts"].append("bar chart")
        if any(word in text_lower for word in ["trend", "increase", "decrease", "growth"]):
            recommendations["charts"].append("line chart")
        if any(word in text_lower for word in ["proportion", "percentage", "part of", "composition"]):
            recommendations["charts"].append("pie chart")
        if any(word in text_lower for word in ["correlation", "relationship", "distributed"]):
            recommendations["charts"].append("scatter plot")

        # Detect table opportunities
        if any(word in text_lower for word in ["list", "summary", "data", "table", "statistics"]):
            recommendations["tables"].append("summary table")
        if any(word in text_lower for word in ["compare", "comparison"]):
            recommendations["tables"].append("comparison table")

        # Detect diagram opportunities
        if any(word in text_lower for word in ["process", "step", "workflow", "procedure"]):
            recommendations["diagrams"].append("flowchart")
        if any(word in text_lower for word in ["hierarchy", "organization", "structure", "levels"]):
            recommendations["diagrams"].append("hierarchy diagram")

        return recommendations
