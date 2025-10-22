"""
PDF Styles - PDF styling templates
"""


class PDFStyles:
    """PDF styling constants and templates."""

    # Color palette
    COLORS = {
        "primary": "#1a73e8",
        "secondary": "#34a853",
        "accent": "#f57c00",
        "text": "#202124",
        "light_bg": "#f8f9fa",
        "border": "#dadce0",
    }

    # Typography
    FONTS = {
        "heading": ("Helvetica-Bold", 16),
        "subheading": ("Helvetica-Bold", 14),
        "body": ("Helvetica", 11),
        "small": ("Helvetica", 9),
    }

    # Spacing (in points)
    SPACING = {
        "xs": 5,
        "sm": 10,
        "md": 15,
        "lg": 20,
        "xl": 30,
    }

    # Margins (in inches)
    MARGINS = {
        "top": 1.0,
        "bottom": 1.0,
        "left": 1.0,
        "right": 1.0,
    }

    @staticmethod
    def get_heading_style(level: int = 1) -> tuple:
        """Get heading style by level."""
        styles = {
            1: ("Helvetica-Bold", 18),
            2: ("Helvetica-Bold", 16),
            3: ("Helvetica-Bold", 14),
            4: ("Helvetica", 12),
        }
        return styles.get(level, styles[4])

    @staticmethod
    def get_page_style(style_name: str = "default") -> dict:
        """Get pre-defined page style."""
        styles = {
            "default": {
                "font": ("Helvetica", 11),
                "line_spacing": 1.5,
                "margins": PDFStyles.MARGINS,
            },
            "academic": {
                "font": ("Times-Roman", 12),
                "line_spacing": 2.0,
                "margins": {"top": 1.0, "bottom": 1.0, "left": 1.25, "right": 1.25},
            },
            "modern": {
                "font": ("Helvetica", 11),
                "line_spacing": 1.5,
                "margins": PDFStyles.MARGINS,
            },
        }
        return styles.get(style_name, styles["default"])
