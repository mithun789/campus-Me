"""
File Handlers - File I/O operations
"""

import os
import tempfile
from typing import BinaryIO, Optional


class FileHandler:
    """Handle file operations."""

    @staticmethod
    def save_file(content: bytes, filename: str, temp: bool = True) -> str:
        """Save content to file."""
        if temp:
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1]) as f:
                f.write(content)
                return f.name
        else:
            with open(filename, 'wb') as f:
                f.write(content)
            return filename

    @staticmethod
    def read_file(filepath: str) -> bytes:
        """Read file content."""
        with open(filepath, 'rb') as f:
            return f.read()

    @staticmethod
    def delete_file(filepath: str) -> bool:
        """Delete file safely."""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
            return True
        except:
            return False

    @staticmethod
    def get_file_size(filepath: str) -> int:
        """Get file size in bytes."""
        return os.path.getsize(filepath) if os.path.exists(filepath) else 0
