"""
Citation Manager - Generate citations in multiple formats
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Citation:
    """Represents a single citation."""

    authors: List[str]
    title: str
    publication: str
    year: int
    url: Optional[str] = None
    doi: Optional[str] = None
    pages: Optional[str] = None


class CitationManager:
    """
    Generate citations in multiple formats (APA, MLA, Chicago, Harvard, IEEE).
    """

    def __init__(self):
        """Initialize citation manager."""
        self.supported_styles = ["APA", "MLA", "Chicago", "Harvard", "IEEE"]

    def generate_citation(
        self,
        authors: List[str],
        title: str,
        publication: str,
        year: int,
        style: str = "APA",
        url: Optional[str] = None,
        doi: Optional[str] = None,
        pages: Optional[str] = None,
    ) -> str:
        """
        Generate a formatted citation.

        Args:
            authors: List of author names
            title: Publication title
            publication: Publication name/journal
            year: Publication year
            style: Citation style (APA, MLA, Chicago, Harvard, IEEE)
            url: Optional URL
            doi: Optional DOI
            pages: Optional page numbers

        Returns:
            Formatted citation string
        """
        citation = Citation(
            authors=authors,
            title=title,
            publication=publication,
            year=year,
            url=url,
            doi=doi,
            pages=pages,
        )

        if style.upper() == "APA":
            return self._format_apa(citation)
        elif style.upper() == "MLA":
            return self._format_mla(citation)
        elif style.upper() == "CHICAGO":
            return self._format_chicago(citation)
        elif style.upper() == "HARVARD":
            return self._format_harvard(citation)
        elif style.upper() == "IEEE":
            return self._format_ieee(citation)
        else:
            return self._format_apa(citation)  # Default to APA

    def _format_apa(self, citation: Citation) -> str:
        """Format citation in APA style."""
        authors_str = self._format_authors_apa(citation.authors)
        citation_str = (
            f"{authors_str} ({citation.year}). {citation.title}. {citation.publication}."
        )

        if citation.doi:
            citation_str += f" https://doi.org/{citation.doi}"
        elif citation.url:
            citation_str += f" Retrieved from {citation.url}"

        return citation_str

    def _format_mla(self, citation: Citation) -> str:
        """Format citation in MLA style."""
        authors_str = self._format_authors_mla(citation.authors)
        citation_str = (
            f'{authors_str}. "{citation.title}." {citation.publication}, {citation.year}.'
        )

        if citation.pages:
            citation_str += f" pp. {citation.pages}."

        if citation.url:
            citation_str += f" Web. {citation.url}."

        return citation_str

    def _format_chicago(self, citation: Citation) -> str:
        """Format citation in Chicago style."""
        authors_str = self._format_authors_chicago(citation.authors)
        citation_str = f'{authors_str}. "{citation.title}." {citation.publication} {citation.year}.'

        if citation.pages:
            citation_str += f" Pages {citation.pages}."

        return citation_str

    def _format_harvard(self, citation: Citation) -> str:
        """Format citation in Harvard style."""
        authors_str = self._format_authors_harvard(citation.authors)
        citation_str = (
            f"{authors_str} {citation.year}, {citation.title}, {citation.publication}."
        )

        if citation.url:
            citation_str += f" Available at: {citation.url}"

        return citation_str

    def _format_ieee(self, citation: Citation) -> str:
        """Format citation in IEEE style."""
        authors_str = self._format_authors_ieee(citation.authors)
        citation_str = f'[#] {authors_str}, "{citation.title}," {citation.publication}, {citation.year}.'

        return citation_str

    def _format_authors_apa(self, authors: List[str]) -> str:
        """Format authors for APA style."""
        if not authors:
            return "Unknown"
        if len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return f"{authors[0]} & {authors[1]}"
        else:
            return f"{authors[0]}, {authors[1]}, & {authors[2]}"

    def _format_authors_mla(self, authors: List[str]) -> str:
        """Format authors for MLA style."""
        if not authors:
            return "Unknown"
        if len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return f"{authors[0]}, and {authors[1]}"
        else:
            return f"{authors[0]}, {authors[1]}, and {authors[2]}"

    def _format_authors_chicago(self, authors: List[str]) -> str:
        """Format authors for Chicago style."""
        if not authors:
            return "Unknown"
        return self._format_authors_mla(authors)

    def _format_authors_harvard(self, authors: List[str]) -> str:
        """Format authors for Harvard style."""
        if not authors:
            return "Unknown"
        if len(authors) == 1:
            return authors[0]
        elif len(authors) == 2:
            return f"{authors[0]} and {authors[1]}"
        else:
            return f"{authors[0]} et al."

    def _format_authors_ieee(self, authors: List[str]) -> str:
        """Format authors for IEEE style."""
        if not authors:
            return "Unknown"
        if len(authors) == 1:
            return authors[0]
        elif len(authors) <= 6:
            return ", ".join(authors)
        else:
            return f"{authors[0]} et al."

    def generate_bibliography(self, citations: List[Citation], style: str = "APA") -> str:
        """
        Generate formatted bibliography from multiple citations.

        Args:
            citations: List of Citation objects
            style: Citation style

        Returns:
            Formatted bibliography
        """
        formatted_citations = [self.generate_citation(c.authors, c.title, c.publication, c.year, style, c.url, c.doi, c.pages) for c in citations]

        # Sort alphabetically by first author
        formatted_citations.sort()

        bibliography = "Bibliography\n" + "=" * 20 + "\n\n"
        for i, citation in enumerate(formatted_citations, 1):
            bibliography += f"{i}. {citation}\n\n"

        return bibliography

    def extract_citations_from_text(self, text: str) -> List[Tuple[str, int]]:
        """
        Extract potential citations from text.

        Args:
            text: Text containing citations

        Returns:
            List of (citation_text, page_number)
        """
        citations = []

        # Look for patterns like (Author, Year)
        pattern = r"\(([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s*(\d{4})\)"
        matches = re.finditer(pattern, text)

        for match in matches:
            author = match.group(1)
            year = match.group(2)
            citations.append((f"{author} {year}", 1))  # Page 1 as default

        return citations

    def generate_in_text_citation(self, author: str, year: int, style: str = "APA") -> str:
        """
        Generate in-text citation.

        Args:
            author: Author name
            year: Publication year
            style: Citation style

        Returns:
            In-text citation
        """
        if style.upper() == "APA":
            return f"({author}, {year})"
        elif style.upper() == "MLA":
            return f"({author} {year})"
        elif style.upper() == "CHICAGO":
            return f"({author} {year})"
        elif style.upper() == "HARVARD":
            return f"({author} {year})"
        elif style.upper() == "IEEE":
            return "[#]"  # IEEE uses numbered citations
        else:
            return f"({author}, {year})"

    def parse_citation_string(self, citation_str: str) -> Optional[Citation]:
        """
        Parse a citation string into components.

        Args:
            citation_str: Citation string to parse

        Returns:
            Citation object or None if parsing fails
        """
        try:
            # Very basic parsing - in production, would be more sophisticated
            parts = citation_str.split("|")

            if len(parts) >= 4:
                return Citation(
                    authors=[parts[0].strip()],
                    title=parts[1].strip(),
                    publication=parts[2].strip(),
                    year=int(parts[3].strip()),
                    url=parts[4].strip() if len(parts) > 4 else None,
                )
        except:
            pass

        return None

    def validate_citation(self, citation: Citation) -> Tuple[bool, str]:
        """
        Validate citation data.

        Args:
            citation: Citation object

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not citation.authors or not citation.authors[0]:
            return False, "At least one author required"

        if not citation.title:
            return False, "Title is required"

        if not citation.publication:
            return False, "Publication is required"

        if citation.year < 1000 or citation.year > datetime.now().year + 1:
            return False, f"Invalid year: {citation.year}"

        return True, "Valid"
