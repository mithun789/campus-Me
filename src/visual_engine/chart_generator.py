"""
Chart Generator - Generate charts and graphs
"""

import io
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class ChartGenerator:
    """
    Generate various types of charts and graphs.
    """

    def __init__(self):
        """Initialize chart generator."""
        self.chart_types = ["bar", "line", "pie", "scatter", "histogram"]

    def generate_bar_chart(
        self,
        labels: List[str],
        values: List[float],
        title: str = "Bar Chart",
        xlabel: str = "Categories",
        ylabel: str = "Values",
    ) -> bytes:
        """
        Generate bar chart.

        Args:
            labels: Category labels
            values: Category values
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.bar(labels, values, color="steelblue")
            plt.title(title, fontsize=16, fontweight="bold")
            plt.xlabel(xlabel, fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_line_chart(
        self,
        x_data: List[float],
        y_data: List[float],
        title: str = "Line Chart",
        xlabel: str = "X",
        ylabel: str = "Y",
    ) -> bytes:
        """
        Generate line chart.

        Args:
            x_data: X-axis data
            y_data: Y-axis data
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.plot(x_data, y_data, marker="o", linestyle="-", color="steelblue", linewidth=2)
            plt.title(title, fontsize=16, fontweight="bold")
            plt.xlabel(xlabel, fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_pie_chart(
        self, labels: List[str], values: List[float], title: str = "Pie Chart"
    ) -> bytes:
        """
        Generate pie chart.

        Args:
            labels: Slice labels
            values: Slice values
            title: Chart title

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 8))
            plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
            plt.title(title, fontsize=16, fontweight="bold")
            plt.axis("equal")
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_scatter_plot(
        self,
        x_data: List[float],
        y_data: List[float],
        title: str = "Scatter Plot",
        xlabel: str = "X",
        ylabel: str = "Y",
    ) -> bytes:
        """
        Generate scatter plot.

        Args:
            x_data: X-axis data
            y_data: Y-axis data
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.scatter(x_data, y_data, color="steelblue", s=100, alpha=0.6)
            plt.title(title, fontsize=16, fontweight="bold")
            plt.xlabel(xlabel, fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_histogram(
        self, data: List[float], title: str = "Histogram", xlabel: str = "Values", bins: int = 10
    ) -> bytes:
        """
        Generate histogram.

        Args:
            data: Data values
            title: Chart title
            xlabel: X-axis label
            bins: Number of bins

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.hist(data, bins=bins, color="steelblue", edgecolor="black")
            plt.title(title, fontsize=16, fontweight="bold")
            plt.xlabel(xlabel, fontsize=12)
            plt.ylabel("Frequency", fontsize=12)
            plt.grid(True, alpha=0.3, axis="y")
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_multi_line_chart(
        self,
        data: Dict[str, List[float]],
        x_labels: List[str] = None,
        title: str = "Multi-Line Chart",
        xlabel: str = "X",
        ylabel: str = "Y",
    ) -> bytes:
        """
        Generate multi-line chart.

        Args:
            data: Dictionary of {series_name: values_list}
            x_labels: X-axis labels
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label

        Returns:
            Chart image bytes
        """
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(12, 6))

            for series_name, values in data.items():
                if x_labels:
                    plt.plot(x_labels, values, marker="o", label=series_name, linewidth=2)
                else:
                    plt.plot(values, marker="o", label=series_name, linewidth=2)

            plt.title(title, fontsize=16, fontweight="bold")
            plt.xlabel(xlabel, fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            # Save to bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            buffer.seek(0)
            plt.close()

            return buffer.getvalue()

        except ImportError:
            logger.warning("matplotlib not available")
            return b"Chart generation failed"

    def generate_chart_html_embed(self, chart_bytes: bytes, alt_text: str = "Chart") -> str:
        """
        Generate HTML embed code for chart.

        Args:
            chart_bytes: Chart image bytes
            alt_text: Alternative text for image

        Returns:
            HTML embed code
        """
        import base64

        encoded = base64.b64encode(chart_bytes).decode("utf-8")
        return f'<img src="data:image/png;base64,{encoded}" alt="{alt_text}" style="max-width: 100%;">'
