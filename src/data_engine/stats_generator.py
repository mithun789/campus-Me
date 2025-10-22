"""
Stats Generator - Generate statistical analysis and reports
"""

from typing import List, Dict
import statistics


class StatsGenerator:
    """Generate statistical analysis and reports."""

    def generate_summary_statistics(self, data: List[float]) -> str:
        """Generate summary statistics report."""
        if not data:
            return "No data available"

        analysis = {
            "Count": len(data),
            "Mean": f"{statistics.mean(data):.2f}",
            "Median": f"{statistics.median(data):.2f}",
            "Std Dev": f"{statistics.stdev(data):.2f}" if len(data) > 1 else "N/A",
            "Min": f"{min(data):.2f}",
            "Max": f"{max(data):.2f}",
        }

        report = "STATISTICAL SUMMARY\n" + "=" * 30 + "\n\n"
        for key, value in analysis.items():
            report += f"{key:.<20} {value:>10}\n"

        return report

    def generate_correlation_analysis(self, data_x: List[float], data_y: List[float]) -> str:
        """Generate correlation analysis."""
        if len(data_x) != len(data_y) or len(data_x) < 2:
            return "Invalid data for correlation"

        mean_x = statistics.mean(data_x)
        mean_y = statistics.mean(data_y)

        numerator = sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(len(data_x)))
        denom_x = sum((x - mean_x) ** 2 for x in data_x) ** 0.5
        denom_y = sum((y - mean_y) ** 2 for y in data_y) ** 0.5

        correlation = numerator / (denom_x * denom_y) if denom_x * denom_y != 0 else 0

        return f"Correlation Coefficient: {correlation:.3f}"
