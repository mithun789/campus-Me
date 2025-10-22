"""
Helpers - General utility functions
"""

from typing import List, Dict, Any
import time


class GeneralHelpers:
    """General helper functions."""

    @staticmethod
    def flatten_list(nested_list: List) -> List:
        """Flatten nested list."""
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(GeneralHelpers.flatten_list(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def merge_dicts(*dicts: Dict) -> Dict:
        """Merge multiple dictionaries."""
        result = {}
        for d in dicts:
            result.update(d)
        return result

    @staticmethod
    def chunk_list(items: List, chunk_size: int) -> List[List]:
        """Split list into chunks."""
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    @staticmethod
    def timer(func):
        """Decorator to time function execution."""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"{func.__name__} took {elapsed:.2f} seconds")
            return result
        return wrapper

    @staticmethod
    def ensure_list(value: Any) -> List:
        """Ensure value is a list."""
        if isinstance(value, list):
            return value
        elif value is None:
            return []
        else:
            return [value]

    @staticmethod
    def safe_get(dictionary: Dict, key: str, default: Any = None) -> Any:
        """Safely get dictionary value."""
        try:
            keys = key.split('.')
            value = dictionary
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
