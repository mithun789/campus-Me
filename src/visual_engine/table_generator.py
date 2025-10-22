"""
Table Generator - Generate tables from text data
"""

import re
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class TableGenerator:
    """
    Automatically generate tables from text content.
    """

    def __init__(self):
        """Initialize table generator."""
        pass

    def extract_table_data(self, text: str) -> List[List[str]]:
        """
        Extract potential table data from text.

        Args:
            text: Input text

        Returns:
            List of rows (each row is list of cells)
        """
        # Look for tabular patterns or lists
        lines = text.split("\n")
        table_data = []

        for line in lines:
            # Split by multiple spaces or commas
            cells = re.split(r"\s{2,}|,\s*", line.strip())
            if len(cells) > 1 and all(cell.strip() for cell in cells):
                table_data.append([cell.strip() for cell in cells])

        return table_data if table_data else self._create_default_table()

    def _create_default_table(self) -> List[List[str]]:
        """Create a default example table."""
        return [
            ["Item", "Description", "Value"],
            ["Example 1", "Sample data", "100"],
            ["Example 2", "Sample data", "200"],
        ]

    def generate_summary_table(self, text: str) -> List[List[str]]:
        """
        Generate summary table from text content.

        Args:
            text: Text to summarize in table format

        Returns:
            Table data
        """
        # Extract key points and create summary table
        sentences = re.split(r"(?<=[.!?])\s+", text)[:5]  # First 5 sentences

        table = [["Point", "Description"]]

        for i, sentence in enumerate(sentences, 1):
            # Truncate long sentences
            desc = sentence[:50] + "..." if len(sentence) > 50 else sentence
            table.append([f"Point {i}", desc])

        return table

    def generate_comparison_table(self, items: List[str], attributes: List[str], data: Dict) -> List[List[str]]:
        """
        Generate comparison table.

        Args:
            items: Items to compare
            attributes: Comparison attributes
            data: Data dictionary {item: {attribute: value}}

        Returns:
            Comparison table
        """
        table = [["Item"] + attributes]

        for item in items:
            row = [item]
            for attr in attributes:
                value = data.get(item, {}).get(attr, "-")
                row.append(str(value))
            table.append(row)

        return table

    def generate_statistics_table(self, data_points: List[float]) -> List[List[str]]:
        """
        Generate statistics summary table.

        Args:
            data_points: List of numerical data points

        Returns:
            Statistics table
        """
        if not data_points:
            return [["Metric", "Value"], ["Average", "N/A"], ["Min", "N/A"], ["Max", "N/A"]]

        avg = sum(data_points) / len(data_points)
        min_val = min(data_points)
        max_val = max(data_points)
        med_val = sorted(data_points)[len(data_points) // 2]

        return [
            ["Metric", "Value"],
            ["Count", str(len(data_points))],
            ["Average", f"{avg:.2f}"],
            ["Minimum", f"{min_val:.2f}"],
            ["Maximum", f"{max_val:.2f}"],
            ["Median", f"{med_val:.2f}"],
        ]

    def format_as_markdown(self, table: List[List[str]]) -> str:
        """
        Format table as Markdown.

        Args:
            table: Table data

        Returns:
            Markdown table string
        """
        if not table:
            return ""

        # Create header
        md_table = "| " + " | ".join(table[0]) + " |\n"
        md_table += "|" + "|".join(["---" for _ in table[0]]) + "|\n"

        # Add rows
        for row in table[1:]:
            md_table += "| " + " | ".join(str(cell) for cell in row) + " |\n"

        return md_table

    def format_as_html(self, table: List[List[str]]) -> str:
        """
        Format table as HTML.

        Args:
            table: Table data

        Returns:
            HTML table string
        """
        if not table:
            return "<table></table>"

        html = "<table border='1' cellpadding='10'>\n"

        # Header row
        html += "<thead><tr>"
        for cell in table[0]:
            html += f"<th>{cell}</th>"
        html += "</tr></thead>\n"

        # Body rows
        html += "<tbody>\n"
        for row in table[1:]:
            html += "<tr>"
            for cell in row:
                html += f"<td>{cell}</td>"
            html += "</tr>\n"
        html += "</tbody>\n"

        html += "</table>"

        return html

    def format_as_csv(self, table: List[List[str]]) -> str:
        """
        Format table as CSV.

        Args:
            table: Table data

        Returns:
            CSV string
        """
        import csv
        import io

        output = io.StringIO()
        writer = csv.writer(output)

        for row in table:
            writer.writerow(row)

        return output.getvalue()

    def generate_from_dataframe(self, df_dict: Dict) -> List[List[str]]:
        """
        Generate table from dataframe-like dictionary.

        Args:
            df_dict: Dictionary with column names as keys and data lists as values

        Returns:
            Table data
        """
        if not df_dict:
            return []

        # Create header
        headers = list(df_dict.keys())
        table = [headers]

        # Get number of rows
        num_rows = max(len(v) for v in df_dict.values()) if df_dict.values() else 0

        # Create rows
        for i in range(num_rows):
            row = []
            for col_name in headers:
                value = df_dict[col_name][i] if i < len(df_dict[col_name]) else "-"
                row.append(str(value))
            table.append(row)

        return table
