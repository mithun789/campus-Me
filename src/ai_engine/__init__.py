"""
AI Engine - Core module initialization
"""

from .document_parser import DocumentParser
from .requirement_analyzer import RequirementAnalyzer
from .content_generator import ContentGenerator
from .humanizer import Humanizer
from .citation_manager import CitationManager
from .detector import AIDetector
from .material_analyzer import MaterialAnalyzer, MaterialProcessor
from .file_manager import FileManager, FileCleanupScheduler

__all__ = [
    "DocumentParser",
    "RequirementAnalyzer",
    "ContentGenerator",
    "Humanizer",
    "CitationManager",
    "AIDetector",
    "MaterialAnalyzer",
    "MaterialProcessor",
    "FileManager",
    "FileCleanupScheduler",
]
