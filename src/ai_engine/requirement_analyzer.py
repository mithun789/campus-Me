"""
Requirement Analyzer - Analyze assignment and document requirements
"""

import re
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class DocumentRequirements:
    """Structured document requirements."""

    title: str
    target_words: int
    style: str
    complexity_level: str
    key_topics: List[str]
    include_citations: bool
    include_tables: bool
    include_charts: bool
    citation_style: str
    document_type: str
    sections: List[str]


class RequirementAnalyzer:
    """
    Analyze user requirements and extract key information for document generation.
    """

    def __init__(self):
        """Initialize the requirement analyzer."""
        self.document_types = ["essay", "report", "research", "lab", "thesis", "article"]
        self.complexity_levels = ["high school", "undergraduate", "graduate", "professional"]
        self.citation_styles = ["APA", "MLA", "Chicago", "Harvard", "IEEE"]
        self.styles = ["formal", "academic", "informal", "technical", "narrative"]

    def analyze_requirements(self, requirements_text: str, lecture_notes: str = "") -> DocumentRequirements:
        """
        Analyze user requirements and extract key parameters.

        Args:
            requirements_text: User's requirements/assignment description
            lecture_notes: Optional lecture notes for context

        Returns:
            DocumentRequirements object with structured data
        """
        # Extract title
        title = self._extract_title(requirements_text)

        # Extract word count
        target_words = self._extract_word_count(requirements_text)

        # Infer document type
        doc_type = self._infer_document_type(requirements_text)

        # Extract style
        style = self._extract_style(requirements_text)

        # Extract complexity level
        complexity = self._extract_complexity(requirements_text)

        # Extract key topics
        topics = self._extract_key_topics(requirements_text, lecture_notes)

        # Check for visualization requirements
        include_tables = self._check_for_tables(requirements_text)
        include_charts = self._check_for_charts(requirements_text)
        include_citations = self._check_for_citations(requirements_text)

        # Extract citation style
        citation_style = self._extract_citation_style(requirements_text)

        # Generate sections
        sections = self._generate_sections(doc_type, topics)

        return DocumentRequirements(
            title=title,
            target_words=target_words,
            style=style,
            complexity_level=complexity,
            key_topics=topics,
            include_citations=include_citations,
            include_tables=include_tables,
            include_charts=include_charts,
            citation_style=citation_style,
            document_type=doc_type,
            sections=sections,
        )

    def _extract_title(self, text: str) -> str:
        """Extract document title from requirements."""
        # Look for title indicators
        lines = text.split("\n")
        for line in lines:
            line_lower = line.lower()
            if "title" in line_lower or "topic" in line_lower:
                # Extract the text after colon if present
                if ":" in line:
                    return line.split(":", 1)[1].strip()
                return line.replace("Title:", "").replace("title:", "").replace("Topic:", "").strip()

        # Use first line as fallback
        return lines[0][:100] if lines else "Academic Document"

    def _extract_word_count(self, text: str) -> int:
        """Extract target word count from requirements."""
        # Look for word count patterns
        patterns = [
            r"(\d+)\s*(?:word|page)s?",
            r"(?:word|page)\s*count\s*:?\s*(\d+)",
            r"(\d+)\s*-\s*(\d+)\s*words?",
        ]

        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            if matches:
                if isinstance(matches[0], tuple):
                    # Range pattern
                    return int(matches[0][0])
                else:
                    return int(matches[0])

        # Default to 2000 words
        return 2000

    def _infer_document_type(self, text: str) -> str:
        """Infer document type from requirements."""
        text_lower = text.lower()

        for doc_type in self.document_types:
            if doc_type in text_lower:
                return doc_type

        # Default to research paper
        return "research"

    def _extract_style(self, text: str) -> str:
        """Extract writing style from requirements."""
        text_lower = text.lower()

        for style in self.styles:
            if style in text_lower:
                return style

        return "academic"

    def _extract_complexity(self, text: str) -> str:
        """Extract complexity level from requirements."""
        text_lower = text.lower()

        for level in self.complexity_levels:
            if level in text_lower:
                return level

        return "undergraduate"

    def _extract_key_topics(self, requirements: str, notes: str = "") -> List[str]:
        """
        Extract key topics from requirements and notes.

        Args:
            requirements: Requirements text
            notes: Lecture notes

        Returns:
            List of key topics
        """
        topics = []
        combined_text = requirements + " " + notes

        # Extract words after common keywords
        keywords = ["discuss", "analyze", "explain", "cover", "include", "address", "focus on"]

        for keyword in keywords:
            pattern = f"{keyword}\\s+([^.,;]+)"
            matches = re.findall(pattern, combined_text, re.IGNORECASE)
            for match in matches:
                topic = match.strip()
                if len(topic) > 3 and len(topic) < 100:
                    topics.append(topic)

        # Remove duplicates and limit
        topics = list(dict.fromkeys(topics))[:5]

        return topics if topics else ["General Topic"]

    def _check_for_tables(self, text: str) -> bool:
        """Check if document should include tables."""
        patterns = ["table", "summary", "data", "comparison", "list"]
        text_lower = text.lower()
        return any(pattern in text_lower for pattern in patterns)

    def _check_for_charts(self, text: str) -> bool:
        """Check if document should include charts/graphs."""
        patterns = ["chart", "graph", "visual", "data", "statistics", "analysis", "trend"]
        text_lower = text.lower()
        return any(pattern in text_lower for pattern in patterns)

    def _check_for_citations(self, text: str) -> bool:
        """Check if document should include citations."""
        patterns = ["cite", "reference", "source", "bibliography", "citation"]
        text_lower = text.lower()
        return any(pattern in text_lower for pattern in patterns) or True  # Default to true

    def _extract_citation_style(self, text: str) -> str:
        """Extract citation style preference."""
        text_upper = text.upper()

        for style in self.citation_styles:
            if style in text_upper:
                return style

        # Default to APA
        return "APA"

    def _generate_sections(self, doc_type: str, topics: List[str]) -> List[str]:
        """Generate document sections based on type and topics."""
        section_templates = {
            "research": [
                "Introduction",
                "Literature Review",
                "Methodology",
                "Results",
                "Discussion",
                "Conclusion",
                "References",
            ],
            "essay": [
                "Introduction",
                "Body",
                "Analysis",
                "Conclusion",
                "References",
            ],
            "report": [
                "Executive Summary",
                "Introduction",
                "Findings",
                "Analysis",
                "Recommendations",
                "Conclusion",
            ],
            "lab": [
                "Objective",
                "Procedure",
                "Results",
                "Analysis",
                "Conclusion",
            ],
            "thesis": [
                "Introduction",
                "Literature Review",
                "Methodology",
                "Results",
                "Discussion",
                "Implications",
                "Conclusion",
                "References",
            ],
        }

        return section_templates.get(doc_type.lower(), section_templates["research"])

    def validate_requirements(self, req: DocumentRequirements) -> Tuple[bool, str]:
        """
        Validate extracted requirements.

        Args:
            req: DocumentRequirements object

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not req.title or len(req.title) < 3:
            return False, "Invalid or missing title"

        if req.target_words < 100:
            return False, "Word count too low (minimum 100 words)"

        if req.target_words > 50000:
            return False, "Word count too high (maximum 50000 words)"

        if not req.sections or len(req.sections) < 2:
            return False, "Invalid document structure"

        return True, "Requirements valid"
