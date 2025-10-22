"""
Word Styles - Word document styling templates
"""


class WordStyles:
    """Word document styling constants and templates."""

    # Pre-defined styles
    HEADING_STYLES = {
        "Heading 1": {
            "size": 28,
            "bold": True,
            "color": "1a73e8",
        },
        "Heading 2": {
            "size": 22,
            "bold": True,
            "color": "34a853",
        },
        "Heading 3": {
            "size": 16,
            "bold": True,
            "color": "333333",
        },
    }

    BODY_STYLE = {
        "size": 11,
        "font": "Calibri",
        "line_spacing": 1.5,
    }

    # Paragraph styles
    PARAGRAPH_STYLES = {
        "normal": {
            "alignment": "left",
            "spacing_before": 0,
            "spacing_after": 12,
        },
        "centered": {
            "alignment": "center",
            "spacing_before": 0,
            "spacing_after": 12,
        },
        "quote": {
            "alignment": "left",
            "left_indent": 0.5,
            "spacing_before": 12,
            "spacing_after": 12,
        },
    }

    @staticmethod
    def get_style(style_name: str) -> dict:
        """Get predefined style."""
        all_styles = {
            **WordStyles.HEADING_STYLES,
            **{"body": WordStyles.BODY_STYLE},
        }
        return all_styles.get(style_name, {})
