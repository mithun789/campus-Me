"""
AI Detector - Analyze AI detection risks and provide transparency
"""

import re
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)


class AIDetector:
    """
    Analyze generated content for AI detection risks and detection patterns.
    """

    def __init__(self):
        """Initialize AI detector."""
        self.ai_indicators = {
            "perfect_structure": r"^(Introduction|Furthermore|Conclusion)$",
            "repeated_phrases": r"(?:It is important|significantly|Therefore|however)",
            "formal_language": r"(?:Furthermore|However|In conclusion|Subsequently)",
            "lack_of_contractions": r"(?<!n't)\s(?:is|are|have|has|do|does|will|would|could|should)\s",
            "generic_transitions": r"\b(Also|Additionally|Moreover|Furthermore)\b",
            "overly_perfect_grammar": r"^[A-Z][a-zA-Z\s.,;:]*[.!?]$",
        }

    def analyze_detection_risk(self, content: str) -> Dict[str, any]:
        """
        Analyze content for AI detection risks.

        Args:
            content: Generated content to analyze

        Returns:
            Dict with detection risk scores and indicators
        """
        risk_score = 0.0
        indicators = {}

        # Check for perfect structure
        structure_risk = self._check_structure(content)
        indicators["structure"] = structure_risk
        risk_score += structure_risk * 0.15

        # Check for repeated phrases
        repeat_risk = self._check_repetition(content)
        indicators["repetition"] = repeat_risk
        risk_score += repeat_risk * 0.15

        # Check formality level
        formality_risk = self._check_formality(content)
        indicators["formality"] = formality_risk
        risk_score += formality_risk * 0.15

        # Check for contractions
        contraction_risk = self._check_contractions(content)
        indicators["contractions"] = contraction_risk
        risk_score += contraction_risk * 0.15

        # Check for transitions
        transition_risk = self._check_transitions(content)
        indicators["transitions"] = transition_risk
        risk_score += transition_risk * 0.15

        # Check sentence variety
        variety_risk = self._check_variety(content)
        indicators["variety"] = variety_risk
        risk_score += variety_risk * 0.15

        # Check for human elements
        human_score = self._check_human_elements(content)
        indicators["human_elements"] = human_score
        risk_score = max(0, risk_score - human_score * 0.1)

        return {
            "risk_score": min(risk_score, 1.0),  # Normalize to 0-1
            "risk_level": self._score_to_level(risk_score),
            "indicators": indicators,
            "recommendation": self._get_recommendation(risk_score),
        }

    def _check_structure(self, content: str) -> float:
        """Check if content has too-perfect structure."""
        lines = content.split("\n")
        structural_elements = 0

        for line in lines:
            if re.match(self.ai_indicators["perfect_structure"], line.strip(), re.IGNORECASE):
                structural_elements += 1

        # Normalize: more structure elements = higher risk
        return min(structural_elements / max(len(lines), 1), 1.0)

    def _check_repetition(self, content: str) -> float:
        """Check for repeated phrases."""
        words = content.lower().split()
        phrase_freq = {}

        # Check 3-word phrases
        for i in range(len(words) - 2):
            phrase = " ".join(words[i : i + 3])
            phrase_freq[phrase] = phrase_freq.get(phrase, 0) + 1

        # Calculate repetition score
        repeated_phrases = sum(1 for freq in phrase_freq.values() if freq > 2)
        return min(repeated_phrases / max(len(phrase_freq), 1), 1.0)

    def _check_formality(self, content: str) -> float:
        """Check for overly formal language."""
        formal_markers = len(re.findall(r"\b(Furthermore|Moreover|Subsequently|In conclusion)\b", content, re.IGNORECASE))
        word_count = len(content.split())

        # High formality can indicate AI generation
        formality_ratio = formal_markers / max(word_count / 100, 1)
        return min(formality_ratio, 1.0)

    def _check_contractions(self, content: str) -> float:
        """Check for lack of contractions (AI trait)."""
        contractions = len(re.findall(r"\b(don't|can't|won't|it's|that's|isn't|aren't|haven't|hasn't)\b", content, re.IGNORECASE))

        # More contractions = more human
        # Lack of contractions = more AI-like
        if len(content.split()) < 100:
            return 0.3  # Short text is hard to judge

        contraction_rate = contractions / len(content.split()) * 100
        # Humans typically use contractions at ~5-15% rate
        if contraction_rate < 2:
            return 0.8  # High risk if no contractions
        elif contraction_rate > 20:
            return 0.3  # Low risk if too many contractions
        else:
            return 0.2  # Normal range

    def _check_transitions(self, content: str) -> float:
        """Check for overuse of transition phrases."""
        transitions = [
            "furthermore",
            "however",
            "therefore",
            "additionally",
            "moreover",
            "subsequently",
            "consequently",
            "as a result",
        ]

        transition_count = 0
        for transition in transitions:
            transition_count += len(re.findall(rf"\b{transition}\b", content, re.IGNORECASE))

        # Normalize: more transitions than reasonable = higher risk
        word_count = len(content.split())
        transition_ratio = transition_count / max(word_count / 100, 1)

        # Humans typically use 1-2 transitions per 100 words
        if transition_ratio > 3:
            return 0.8  # High risk
        elif transition_ratio < 0.5:
            return 0.2  # Low risk
        else:
            return 0.4  # Medium risk

    def _check_variety(self, content: str) -> float:
        """Check sentence variety."""
        sentences = re.split(r"(?<=[.!?])\s+", content)

        if len(sentences) < 3:
            return 0.2  # Can't judge

        sentence_lengths = [len(s.split()) for s in sentences]
        avg_length = sum(sentence_lengths) / len(sentence_lengths)

        # Calculate variance in sentence length
        variance = sum((length - avg_length) ** 2 for length in sentence_lengths) / len(sentence_lengths)
        std_dev = variance ** 0.5

        # High std dev = more variety = more human
        if std_dev < 2:
            return 0.7  # Low variety = higher AI risk
        elif std_dev > 5:
            return 0.2  # High variety = lower AI risk
        else:
            return 0.4  # Medium

    def _check_human_elements(self, content: str) -> float:
        """Check for human elements (typos, informal language, etc.)."""
        score = 0

        # Check for typos (deliberate misspellings)
        typos = len(re.findall(r"\b[a-z]{1,2}\b", content))  # Very short words often indicate typos
        if typos > len(content.split()) * 0.02:
            score += 0.2

        # Check for informal language
        informal = len(re.findall(r"\b(like|really|definitely|totally|basically)\b", content, re.IGNORECASE))
        if informal > 5:
            score += 0.2

        # Check for questions
        questions = len(re.findall(r"\?", content))
        if questions > len(content.split()) / 100:
            score += 0.2

        # Check for exclamations
        exclamations = len(re.findall(r"!", content))
        if exclamations > 0:
            score += 0.1

        # Check for varied punctuation
        if re.search(r"[;:—–]", content):
            score += 0.1

        return min(score, 1.0)

    def _score_to_level(self, score: float) -> str:
        """Convert score to risk level."""
        if score < 0.2:
            return "Very Low"
        elif score < 0.4:
            return "Low"
        elif score < 0.6:
            return "Medium"
        elif score < 0.8:
            return "High"
        else:
            return "Very High"

    def _get_recommendation(self, score: float) -> str:
        """Get recommendation based on risk score."""
        if score < 0.3:
            return "Content appears human-like. Low detection risk."
        elif score < 0.5:
            return "Content has some AI characteristics but is reasonably human-like."
        elif score < 0.7:
            return "Content shows notable AI traits. Recommend humanization."
        else:
            return "Content shows high AI characteristics. Strong humanization needed."

    def get_detection_report(self, content: str) -> str:
        """
        Generate detailed detection report.

        Args:
            content: Content to analyze

        Returns:
            Formatted report
        """
        analysis = self.analyze_detection_risk(content)

        report = f"""
AI DETECTION ANALYSIS REPORT
{'=' * 50}

Overall Risk Score: {analysis['risk_score']:.1%}
Risk Level: {analysis['risk_level']}

DETAILED INDICATORS:
- Structure Formality: {analysis['indicators']['structure']:.1%}
- Phrase Repetition: {analysis['indicators']['repetition']:.1%}
- Excessive Formality: {analysis['indicators']['formality']:.1%}
- Lack of Contractions: {analysis['indicators']['contractions']:.1%}
- Transition Usage: {analysis['indicators']['transitions']:.1%}
- Sentence Variety: {analysis['indicators']['variety']:.1%}
- Human Elements: {analysis['indicators']['human_elements']:.1%}

RECOMMENDATION:
{analysis['recommendation']}

IMPORTANT:
This analysis is for educational purposes only. AI detection tools
are not perfect and can produce false positives/negatives. Using
this tool responsibly and with proper disclosure is essential.
{'=' * 50}
        """

        return report
