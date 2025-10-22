"""
Formatters - Text formatting utilities
"""

import re


class TextFormatter:
    """Format text for various purposes."""

    @staticmethod
    def truncate(text: str, max_length: int, suffix: str = "...") -> str:
        """Truncate text to max length."""
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix

    @staticmethod
    def capitalize_sentences(text: str) -> str:
        """Capitalize first letter of sentences."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        capitalized = [s[0].upper() + s[1:] if s else "" for s in sentences]
        return ' '.join(capitalized)

    @staticmethod
    def remove_extra_whitespace(text: str) -> str:
        """Remove extra whitespace."""
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def convert_to_slug(text: str) -> str:
        """Convert text to URL-friendly slug."""
        slug = text.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        return slug.strip('-')

    @staticmethod
    def word_count(text: str) -> int:
        """Count words in text."""
        return len(text.split())

    @staticmethod
    def estimate_reading_time(text: str, words_per_minute: int = 200) -> int:
        """Estimate reading time in minutes."""
        word_count = TextFormatter.word_count(text)
        return max(1, word_count // words_per_minute)
