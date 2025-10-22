"""
Data Analyzer - Analyze data patterns and statistics
"""

import re
from typing import List, Dict, Tuple
import statistics


class DataAnalyzer:
    """Analyze data patterns and statistics from text or datasets."""

    def extract_numbers(self, text: str) -> List[float]:
        """Extract numeric values from text."""
        pattern = r"-?\d+\.?\d*"
        matches = re.findall(pattern, text)
        return [float(m) for m in matches if m]

    def analyze_numeric_data(self, data: List[float]) -> Dict:
        """Analyze numeric data."""
        if not data:
            return {}

        return {
            "count": len(data),
            "sum": sum(data),
            "mean": statistics.mean(data),
            "median": statistics.median(data),
            "mode": statistics.mode(data) if len(set(data)) < len(data) else None,
            "stdev": statistics.stdev(data) if len(data) > 1 else 0,
            "min": min(data),
            "max": max(data),
            "range": max(data) - min(data),
        }

    def detect_patterns(self, data: List[float]) -> Dict[str, str]:
        """Detect patterns in data."""
        if len(data) < 2:
            return {}

        diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
        avg_diff = sum(diffs) / len(diffs)

        patterns = {}
        
        if abs(avg_diff) < 0.001:
            patterns["trend"] = "flat"
        elif avg_diff > 0:
            patterns["trend"] = "increasing"
        else:
            patterns["trend"] = "decreasing"

        return patterns

    def find_outliers(self, data: List[float], std_threshold: float = 2) -> List[float]:
        """Find outliers using standard deviation."""
        if len(data) < 2:
            return []

        mean = statistics.mean(data)
        stdev = statistics.stdev(data)

        return [x for x in data if abs((x - mean) / stdev) > std_threshold]
