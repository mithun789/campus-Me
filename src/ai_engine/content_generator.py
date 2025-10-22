"""
Content Generator - Generate academic content using AI models
"""

import re
from typing import Dict, List, Optional, Any
from textwrap import dedent
import logging

logger = logging.getLogger(__name__)


class ContentGenerator:
    """
    Generate academic content using Hugging Face models.
    """

    def __init__(self, model_name: str = "HuggingFaceH4/zephyr-7b-beta"):
        """
        Initialize content generator.

        Args:
            model_name: Hugging Face model identifier
        """
        self.model_name = model_name
        self.pipeline = None
        self._init_model()

    def _init_model(self):
        """Initialize the language model."""
        try:
            from transformers import pipeline

            self.pipeline = pipeline(
                "text-generation",
                model=self.model_name,
                device=-1,  # Use CPU
                torch_dtype="auto",
            )
            logger.info(f"Model {self.model_name} loaded successfully")
        except Exception as e:
            logger.warning(f"Model loading failed: {e}. Using fallback generation.")
            self.pipeline = None

    def generate_section(
        self,
        title: str,
        context: str = "",
        topic: str = "",
        word_count: int = 300,
        style: str = "academic",
    ) -> str:
        """
        Generate a single document section.

        Args:
            title: Section title
            context: Additional context for generation
            topic: Main topic of the section
            word_count: Target word count
            style: Writing style (academic, formal, informal, etc.)

        Returns:
            Generated section content
        """
        prompt = self._create_prompt(title, context, topic, style, word_count)

        if self.pipeline:
            return self._generate_with_model(prompt, word_count)
        else:
            return self._generate_fallback(title, topic, word_count)

    def _create_prompt(
        self, title: str, context: str, topic: str, style: str, word_count: int
    ) -> str:
        """Create generation prompt."""
        prompt = dedent(
            f"""
        Write a {style} section titled "{title}" about {topic}.
        Context: {context}
        
        Requirements:
        - Approximately {word_count} words
        - Professional {style} tone
        - Well-structured with clear paragraphs
        - Informative and engaging
        
        Section Content:
        """
        )
        return prompt

    def _generate_with_model(self, prompt: str, word_count: int) -> str:
        """Generate using the loaded model."""
        try:
            max_tokens = min(word_count // 4 + 100, 512)  # Rough estimation: 4 chars per word

            result = self.pipeline(
                prompt,
                max_length=max_tokens,
                num_return_sequences=1,
                temperature=0.7,
                top_p=0.95,
                do_sample=True,
            )

            if result and len(result) > 0:
                generated_text = result[0]["generated_text"]
                # Extract only the new content after the prompt
                content = generated_text[len(prompt) :].strip()
                return content if content else self._generate_fallback("Content", "", word_count)

            return self._generate_fallback("Content", "", word_count)

        except Exception as e:
            logger.warning(f"Generation failed: {e}. Using fallback.")
            return self._generate_fallback("Content", "", word_count)

    def _generate_fallback(self, title: str, topic: str, word_count: int) -> str:
        """Generate content using fallback method when model is unavailable."""
        templates = {
            "introduction": "This section introduces the key concepts and provides context. ",
            "methodology": "This section describes the methods and approaches used. ",
            "results": "This section presents the key findings and outcomes. ",
            "discussion": "This section analyzes the implications and significance. ",
            "conclusion": "This section summarizes the main points and conclusions. ",
            "literature review": "This section reviews relevant existing research and scholarship. ",
        }

        title_lower = title.lower()
        base_text = templates.get(title_lower, f"This section discusses {topic}. ")

        # Generate paragraphs to reach target word count
        paragraphs = []
        target_words = word_count

        while len(" ".join(paragraphs)) < target_words:
            paragraph = (
                f"{base_text} "
                f"The significance of {topic} cannot be overstated in the context of modern {title.lower()}. "
                f"Through careful analysis and consideration, we find that multiple factors contribute to this outcome. "
                f"Furthermore, the evidence suggests that continued research and investigation in this area will yield valuable insights. "
                f"In conclusion, this aspect merits further attention from researchers and practitioners alike."
            )
            paragraphs.append(paragraph)

        return " ".join(paragraphs)[: word_count * 4]  # Rough character limit

    def generate_document_sections(
        self,
        sections: List[str],
        context: str = "",
        topics: List[str] = None,
        style: str = "academic",
        total_words: int = 2000,
    ) -> Dict[str, str]:
        """
        Generate multiple sections for a complete document.

        Args:
            sections: List of section titles
            context: Document context
            topics: Topic for each section
            style: Writing style
            total_words: Target total word count

        Returns:
            Dictionary of section_title: content
        """
        if topics is None:
            topics = [f"aspect {i}" for i in range(len(sections))]

        # Distribute words across sections
        words_per_section = total_words // len(sections)

        content = {}
        for section, topic in zip(sections, topics):
            section_content = self.generate_section(
                title=section,
                context=context,
                topic=topic,
                word_count=words_per_section,
                style=style,
            )
            content[section] = section_content

        return content

    def improve_content(self, content: str) -> str:
        """
        Improve existing content for better readability and flow.

        Args:
            content: Original content

        Returns:
            Improved content
        """
        # Simple improvements without model
        improved = self._improve_sentences(content)
        improved = self._fix_grammar_basic(improved)
        improved = self._improve_flow(improved)

        return improved

    def _improve_sentences(self, text: str) -> str:
        """Improve sentence structure."""
        # Break up overly long sentences
        sentences = re.split(r"(?<=[.!?])\s+", text)
        improved_sentences = []

        for sent in sentences:
            if len(sent) > 200:  # Split very long sentences
                parts = sent.split(",")
                if len(parts) > 2:
                    improved_sentences.extend(parts)
                else:
                    improved_sentences.append(sent)
            else:
                improved_sentences.append(sent)

        return " ".join(improved_sentences)

    def _fix_grammar_basic(self, text: str) -> str:
        """Apply basic grammar improvements."""
        # Fix common issues
        text = re.sub(r"\b(a)\s+([aeiou])", r"an \2", text)  # a -> an
        text = re.sub(r"\s+", " ", text)  # Remove extra spaces
        text = re.sub(r"\s([.,;:])", r"\1", text)  # Fix spacing before punctuation

        return text

    def _improve_flow(self, text: str) -> str:
        """Improve text flow and transitions."""
        transitions = {
            r"^Therefore": "As a result",
            r"^However": "Nevertheless",
            r"^Also": "Additionally",
            r"^Finally": "In conclusion",
        }

        for pattern, replacement in transitions.items():
            text = re.sub(pattern, replacement, text, flags=re.MULTILINE)

        return text

    def generate_outline(self, topic: str, sections: List[str]) -> Dict[str, List[str]]:
        """
        Generate detailed outline for document.

        Args:
            topic: Main topic
            sections: Section titles

        Returns:
            Outline with key points per section
        """
        outline = {}

        for section in sections:
            # Generate key points for each section
            key_points = [
                f"Overview of {section.lower()}",
                f"Key aspects of {section.lower()}",
                f"Implications for {topic}",
                f"Current trends in {section.lower()}",
                f"Future directions for {section.lower()}",
            ]

            outline[section] = key_points[:3]  # Select 3 key points per section

        return outline

    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for text.

        Args:
            text: Input text

        Returns:
            Estimated token count
        """
        # Rough estimation: 1 token ≈ 4 characters
        return len(text) // 4
