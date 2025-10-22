"""
Citation Formats - Citation style definitions
"""


class CitationFormats:
    """Citation format templates for various styles."""

    APA = {
        "name": "APA (American Psychological Association)",
        "template": "{authors} ({year}). {title}. {publication}.",
        "description": "Commonly used in social sciences",
    }

    MLA = {
        "name": "MLA (Modern Language Association)",
        "template": '{authors}. "{title}." {publication}, {year}.',
        "description": "Commonly used in humanities",
    }

    CHICAGO = {
        "name": "Chicago Manual of Style",
        "template": '{authors}. "{title}." {publication} {year}.',
        "description": "Used in history and some social sciences",
    }

    HARVARD = {
        "name": "Harvard Referencing",
        "template": "{authors} {year}, {title}, {publication}.",
        "description": "Used in UK universities",
    }

    IEEE = {
        "name": "IEEE (Institute of Electrical and Electronics Engineers)",
        "template": "[#] {authors}, \"{title},\" {publication}, {year}.",
        "description": "Used in engineering and computer science",
    }

    @staticmethod
    def get_all_formats() -> dict:
        """Get all available citation formats."""
        return {
            "APA": CitationFormats.APA,
            "MLA": CitationFormats.MLA,
            "Chicago": CitationFormats.CHICAGO,
            "Harvard": CitationFormats.HARVARD,
            "IEEE": CitationFormats.IEEE,
        }

    @staticmethod
    def get_format_description(style: str) -> str:
        """Get description for citation style."""
        formats = CitationFormats.get_all_formats()
        return formats.get(style, {}).get("description", "Unknown format")
