"""
Layout Manager - Manage document layout and professional design
"""

from typing import Dict, List, Optional, Tuple


class LayoutManager:
    """
    Manage professional document layouts, spacing, and design.
    """

    def __init__(self):
        """Initialize layout manager."""
        self.page_width = 8.5  # inches (letter size)
        self.page_height = 11.0
        self.margin_top = 1.0
        self.margin_bottom = 1.0
        self.margin_left = 1.0
        self.margin_right = 1.0

    def calculate_usable_area(self) -> Tuple[float, float]:
        """
        Calculate usable page area (excluding margins).

        Returns:
            Tuple of (width, height) in inches
        """
        width = self.page_width - self.margin_left - self.margin_right
        height = self.page_height - self.margin_top - self.margin_bottom

        return (width, height)

    def create_two_column_layout(
        self, left_width_percent: float = 50
    ) -> Dict[str, Dict[str, float]]:
        """
        Create two-column layout specification.

        Args:
            left_width_percent: Width percentage of left column

        Returns:
            Layout specification dictionary
        """
        usable_width, usable_height = self.calculate_usable_area()

        left_width = (usable_width * left_width_percent) / 100
        right_width = usable_width - left_width
        gutter = 0.25  # Space between columns

        return {
            "left_column": {
                "x": self.margin_left,
                "y": self.margin_top,
                "width": left_width - gutter / 2,
                "height": usable_height,
            },
            "right_column": {
                "x": self.margin_left + left_width + gutter / 2,
                "y": self.margin_top,
                "width": right_width - gutter / 2,
                "height": usable_height,
            },
        }

    def create_three_column_layout(self) -> Dict[str, Dict[str, float]]:
        """
        Create three-column layout specification.

        Returns:
            Layout specification dictionary
        """
        usable_width, usable_height = self.calculate_usable_area()

        col_width = (usable_width - 0.5) / 3
        gutter = 0.25

        return {
            "left_column": {
                "x": self.margin_left,
                "y": self.margin_top,
                "width": col_width - gutter / 2,
                "height": usable_height,
            },
            "center_column": {
                "x": self.margin_left + col_width + gutter,
                "y": self.margin_top,
                "width": col_width - gutter,
                "height": usable_height,
            },
            "right_column": {
                "x": self.margin_left + 2 * col_width + 2 * gutter,
                "y": self.margin_top,
                "width": col_width - gutter / 2,
                "height": usable_height,
            },
        }

    def get_heading_styles(self) -> Dict[str, Dict]:
        """
        Get professional heading styles.

        Returns:
            Dictionary of heading style specifications
        """
        return {
            "h1": {
                "font_size": 28,
                "font_weight": "bold",
                "color": "#000000",
                "spacing_before": 24,
                "spacing_after": 12,
            },
            "h2": {
                "font_size": 22,
                "font_weight": "bold",
                "color": "#1a1a1a",
                "spacing_before": 18,
                "spacing_after": 10,
            },
            "h3": {
                "font_size": 16,
                "font_weight": "bold",
                "color": "#333333",
                "spacing_before": 12,
                "spacing_after": 6,
            },
            "body": {
                "font_size": 11,
                "font_weight": "normal",
                "color": "#000000",
                "line_height": 1.5,
                "spacing_after": 12,
            },
        }

    def get_color_palette(self, theme: str = "professional") -> Dict[str, str]:
        """
        Get color palette for theme.

        Args:
            theme: Theme name (professional, academic, modern, classic)

        Returns:
            Dictionary of color definitions
        """
        palettes = {
            "professional": {
                "primary": "#1a73e8",
                "secondary": "#34a853",
                "accent": "#f57c00",
                "text": "#202124",
                "light_bg": "#f8f9fa",
                "border": "#dadce0",
            },
            "academic": {
                "primary": "#003366",
                "secondary": "#006699",
                "accent": "#cc0000",
                "text": "#000000",
                "light_bg": "#f5f5f5",
                "border": "#cccccc",
            },
            "modern": {
                "primary": "#6200ea",
                "secondary": "#03dac6",
                "accent": "#ff0266",
                "text": "#1f1f1f",
                "light_bg": "#fafafa",
                "border": "#e0e0e0",
            },
            "classic": {
                "primary": "#2c3e50",
                "secondary": "#3498db",
                "accent": "#e74c3c",
                "text": "#2c3e50",
                "light_bg": "#ecf0f1",
                "border": "#bdc3c7",
            },
        }

        return palettes.get(theme, palettes["professional"])

    def get_spacing_rules(self) -> Dict[str, float]:
        """
        Get spacing rules (in inches).

        Returns:
            Dictionary of spacing values
        """
        return {
            "extra_small": 0.125,
            "small": 0.25,
            "medium": 0.5,
            "large": 0.75,
            "extra_large": 1.0,
            "section_break": 1.5,
            "page_break": self.page_height,
        }

    def create_sidebar_layout(
        self, sidebar_width_percent: float = 25
    ) -> Dict[str, Dict[str, float]]:
        """
        Create sidebar layout specification.

        Args:
            sidebar_width_percent: Width percentage of sidebar

        Returns:
            Layout specification dictionary
        """
        usable_width, usable_height = self.calculate_usable_area()

        sidebar_width = (usable_width * sidebar_width_percent) / 100
        content_width = usable_width - sidebar_width
        gutter = 0.25

        return {
            "sidebar": {
                "x": self.margin_left,
                "y": self.margin_top,
                "width": sidebar_width - gutter / 2,
                "height": usable_height,
            },
            "main_content": {
                "x": self.margin_left + sidebar_width + gutter,
                "y": self.margin_top,
                "width": content_width - gutter / 2,
                "height": usable_height,
            },
        }

    def calculate_text_wrap(self, text: str, column_width: float, chars_per_inch: float = 10) -> List[str]:
        """
        Calculate text wrapping for column width.

        Args:
            text: Text to wrap
            column_width: Column width in inches
            chars_per_inch: Characters per inch (depending on font)

        Returns:
            List of wrapped lines
        """
        max_chars_per_line = int(column_width * chars_per_inch)
        words = text.split()

        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                current_line += word + " "
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

        return lines

    def get_professional_margins(self, format_type: str = "A4") -> Dict[str, float]:
        """
        Get professional margin settings for different formats.

        Args:
            format_type: Format type (A4, Letter, etc.)

        Returns:
            Dictionary of margin values
        """
        formats = {
            "A4": {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0},
            "Letter": {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0},
            "Narrow": {"top": 0.5, "bottom": 0.5, "left": 0.5, "right": 0.5},
            "Wide": {"top": 1.5, "bottom": 1.5, "left": 1.5, "right": 1.5},
        }

        return formats.get(format_type, formats["A4"])

    def get_typography_settings(self) -> Dict[str, any]:
        """
        Get professional typography settings.

        Returns:
            Dictionary of typography settings
        """
        return {
            "font_family": "Calibri, Arial, sans-serif",
            "base_font_size": 11,
            "line_height": 1.5,
            "letter_spacing": 0,
            "paragraph_spacing": 12,
            "heading_font": "Calibri, Arial, sans-serif",
            "heading_weight": "bold",
            "body_weight": "normal",
            "emphasis_style": "italic",
        }

    def create_title_page_layout(self) -> Dict[str, any]:
        """
        Create title page layout specification.

        Returns:
            Title page layout dictionary
        """
        usable_width, usable_height = self.calculate_usable_area()

        return {
            "title": {
                "y": usable_height * 0.25,
                "font_size": 36,
                "alignment": "center",
                "spacing_after": 24,
            },
            "subtitle": {
                "y": usable_height * 0.35,
                "font_size": 18,
                "alignment": "center",
                "spacing_after": 60,
            },
            "author": {
                "y": usable_height * 0.6,
                "font_size": 12,
                "alignment": "center",
                "spacing_after": 12,
            },
            "date": {
                "y": usable_height * 0.65,
                "font_size": 12,
                "alignment": "center",
                "spacing_after": 0,
            },
        }
