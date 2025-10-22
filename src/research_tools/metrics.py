"""
Quality Metrics - Measure document quality and relevance
"""

from typing import Dict
import statistics


class QualityMetrics:
    """Calculate quality metrics for documents."""

    def calculate_readability_score(self, text: str) -> float:
        """Calculate readability score (0-100)."""
        words = text.split()
        sentences = text.count('.') + text.count('!') + text.count('?')
        
        if not words or not sentences:
            return 0

        avg_word_length = sum(len(w) for w in words) / len(words)
        avg_sentence_length = len(words) / sentences

        # Flesch Reading Ease formula
        score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_word_length / 1000)
        return max(0, min(100, score))

    def calculate_coherence_score(self, text: str) -> float:
        """Calculate text coherence (0-100)."""
        # Simplified coherence based on transition words
        transitions = len([w for w in text.lower().split() if w in ["however", "therefore", "furthermore", "moreover"]])
        words = len(text.split())
        
        transition_density = transitions / (words / 100) if words else 0
        coherence = min(transition_density * 20, 100)
        
        return coherence

    def calculate_originality_score(self, text: str) -> float:
        """Estimate originality (very rough approximation)."""
        unique_words = len(set(text.lower().split()))
        total_words = len(text.split())
        
        if total_words == 0:
            return 0
        
        return (unique_words / total_words) * 100

    def get_quality_report(self, text: str) -> Dict:
        """Get comprehensive quality report."""
        return {
            "readability": round(self.calculate_readability_score(text), 1),
            "coherence": round(self.calculate_coherence_score(text), 1),
            "originality": round(self.calculate_originality_score(text), 1),
            "word_count": len(text.split()),
            "sentence_count": text.count('.') + text.count('!') + text.count('?'),
        }
