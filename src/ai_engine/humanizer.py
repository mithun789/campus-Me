"""
Humanizer - Improve AI-generated content to be more natural and human-like
"""

import re
from typing import Dict, List
import random


class Humanizer:
    """
    Improve AI-generated content to be more natural and human-like.
    """

    def __init__(self):
        """Initialize humanizer."""
        self.formal_phrases = {
            "However": ["Though", "Yet", "Still", "Nevertheless", "In contrast"],
            "Therefore": ["As a result", "Consequently", "Thus", "Hence", "For this reason"],
            "Additionally": ["Moreover", "Furthermore", "In addition", "Also", "Besides"],
            "Subsequently": ["After that", "Then", "Following this", "Afterward"],
        }

        self.transition_words = [
            "Interestingly,",
            "Notably,",
            "Importantly,",
            "Significantly,",
            "Remarkably,",
            "Importantly,",
        ]

    def humanize_content(self, content: str, style: str = "academic") -> str:
        """
        Humanize AI-generated content.

        Args:
            content: AI-generated content
            style: Writing style (academic, formal, informal, etc.)

        Returns:
            Humanized content
        """
        content = self._vary_transitions(content)
        content = self._improve_sentence_variety(content)
        content = self._add_examples(content)
        content = self._improve_tone(content, style)

        return content

    def _vary_transitions(self, text: str) -> str:
        """Add variety to transition words."""
        for formal, alternatives in self.formal_phrases.items():
            pattern = rf"\b{formal}\b"
            matches = list(re.finditer(pattern, text, re.IGNORECASE))

            # Vary transitions throughout the text
            for i, match in enumerate(matches):
                if i % 2 == 0:  # Every other occurrence
                    replacement = random.choice(alternatives)
                    text = text[: match.start()] + replacement + text[match.end() :]

        return text

    def _improve_sentence_variety(self, text: str) -> str:
        """Vary sentence structure and length."""
        sentences = re.split(r"(?<=[.!?])\s+", text)
        varied_sentences = []

        for i, sent in enumerate(sentences):
            if i % 3 == 0 and len(sent) > 20:
                # Add variety by restructuring some sentences
                sent = self._restructure_sentence(sent)

            varied_sentences.append(sent)

        return " ".join(varied_sentences)

    def _restructure_sentence(self, sentence: str) -> str:
        """Restructure a sentence for variety."""
        # This is a simple example - more complex NLP would be better
        if sentence.startswith("The "):
            # Try to move "The" for variety
            rest = sentence[4:]
            if "," in rest:
                parts = rest.split(",", 1)
                return f"{parts[0]}, the {parts[1].strip()}"

        return sentence

    def _add_examples(self, text: str) -> str:
        """Suggest adding examples (marked for user addition)."""
        # Find generic statements that could use examples
        generic_patterns = [
            r"This is important",
            r"This is significant",
            r"This is relevant",
            r"There are several reasons",
            r"Multiple factors",
        ]

        for pattern in generic_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                # Mark where examples could be added
                text = re.sub(pattern, f"{pattern} (example: ...)", text, flags=re.IGNORECASE)

        return text

    def _improve_tone(self, text: str, style: str) -> str:
        """Adjust tone based on style."""
        if style == "informal":
            text = self._make_more_conversational(text)
        elif style == "formal":
            text = self._make_more_formal(text)
        elif style == "technical":
            text = self._make_more_technical(text)

        return text

    def _make_more_conversational(self, text: str) -> str:
        """Make text more conversational."""
        text = text.replace("It is evident that", "Clearly")
        text = text.replace("One could argue that", "You could say that")
        text = text.replace("The data suggests", "The evidence points to")
        text = text.replace("It appears that", "It seems like")

        return text

    def _make_more_formal(self, text: str) -> str:
        """Make text more formal."""
        text = text.replace("Clearly", "It is evident that")
        text = text.replace("really", "significantly")
        text = text.replace("very", "considerably")
        text = text.replace("got", "obtained")
        text = text.replace("it seems like", "the evidence suggests")

        return text

    def _make_more_technical(self, text: str) -> str:
        """Make text more technical."""
        text = text.replace("shows", "demonstrates")
        text = text.replace("found", "identified")
        text = text.replace("is", "manifests as")
        text = text.replace("results in", "precipitates")

        return text

    def remove_ai_artifacts(self, text: str) -> str:
        """
        Remove common AI generation artifacts.

        Args:
            text: Generated text

        Returns:
            Cleaned text
        """
        # Remove common AI patterns
        text = re.sub(r"\[.*?\]", "", text)  # Remove [bracketed content]
        text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
        text = re.sub(r"\{.*?\}", "", text)  # Remove {braced content}

        # Fix repeated phrases
        text = re.sub(r"(\b\w+\b)(\s+\1)+", r"\1", text)  # Remove word repetition

        # Clean up extra whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def improve_readability(self, text: str) -> str:
        """
        Improve text readability.

        Args:
            text: Original text

        Returns:
            More readable text
        """
        # Break up long paragraphs
        paragraphs = text.split("\n\n")
        improved_paragraphs = []

        for para in paragraphs:
            if len(para.split()) > 200:  # Very long paragraph
                # Split into smaller paragraphs
                sentences = re.split(r"(?<=[.!?])\s+", para)
                half = len(sentences) // 2

                improved_paragraphs.append(" ".join(sentences[:half]))
                improved_paragraphs.append(" ".join(sentences[half:]))
            else:
                improved_paragraphs.append(para)

        return "\n\n".join(improved_paragraphs)

    def score_humanness(self, text: str) -> float:
        """
        Score text for how human-like it is (0-1 scale).

        Args:
            text: Text to score

        Returns:
            Humanness score
        """
        score = 0.0

        # Check for variety in transitions
        transitions = len(re.findall(r"\b(However|Therefore|Additionally)\b", text))
        if transitions < len(text.split()) / 100:
            score += 0.2

        # Check for variety in sentence structure
        sentences = re.split(r"(?<=[.!?])\s+", text)
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        if 10 < avg_length < 30:  # Natural length range
            score += 0.2

        # Check for lack of repetition
        words = text.lower().split()
        unique_ratio = len(set(words)) / len(words) if words else 0
        if unique_ratio > 0.6:
            score += 0.2

        # Check for contractions (more human)
        contractions = len(re.findall(r"\b(don't|can't|won't|it's|that's)\b", text))
        if contractions > 0:
            score += 0.2

        # Check for no AI markers
        ai_markers = len(re.findall(r"\[(note|example|etc)\]", text, re.IGNORECASE))
        if ai_markers == 0:
            score += 0.2

        return min(score, 1.0)
