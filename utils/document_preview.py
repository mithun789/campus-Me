"""
Document Preview & Download Manager
Handles displaying generated documents with preview and download capabilities
"""

import os
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import base64
import json
import logging

logger = logging.getLogger(__name__)


class DocumentPreviewManager:
    """
    Manage document preview and download for generated documents.
    """

    def __init__(self, output_dir: str = "generated_documents"):
        """
        Initialize preview manager.

        Args:
            output_dir: Directory to store generated documents
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.documents_registry: Dict[str, Dict[str, Any]] = {}

    def register_document(
        self,
        title: str,
        file_paths: Dict[str, str],
        content_preview: str = "",
        metadata: Dict[str, Any] = None
    ) -> str:
        """
        Register a generated document for preview/download.

        Args:
            title: Document title
            file_paths: Dict of format -> file_path (e.g., {"PDF": "/path/to/file.pdf"})
            content_preview: Text preview of content
            metadata: Additional metadata

        Returns:
            Document ID
        """
        import uuid
        from datetime import datetime

        doc_id = str(uuid.uuid4())[:8]

        self.documents_registry[doc_id] = {
            "title": title,
            "file_paths": file_paths,
            "content_preview": content_preview,
            "created_at": datetime.now().isoformat(),
            "metadata": metadata or {},
            "access_count": 0
        }

        logger.info(f"Document registered: {doc_id} - {title}")
        return doc_id

    def get_document_info(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Get information about a registered document."""
        if doc_id in self.documents_registry:
            self.documents_registry[doc_id]["access_count"] += 1
            return self.documents_registry[doc_id]
        return None

    def get_download_link(self, doc_id: str, format_type: str) -> Optional[str]:
        """
        Get download link for a specific format.

        Args:
            doc_id: Document ID
            format_type: Format (PDF, Word, Markdown, HTML)

        Returns:
            File path or None
        """
        doc_info = self.get_document_info(doc_id)
        if doc_info:
            return doc_info["file_paths"].get(format_type.upper())
        return None

    def get_preview_html(self, doc_id: str) -> str:
        """
        Get HTML preview of document.

        Args:
            doc_id: Document ID

        Returns:
            HTML content for preview
        """
        doc_info = self.get_document_info(doc_id)
        if not doc_info:
            return "<p>Document not found</p>"

        title = doc_info["title"]
        preview = doc_info["content_preview"]
        formats = list(doc_info["file_paths"].keys())

        # Generate HTML with download buttons
        html = f"""
        <div style="padding: 20px; background: #f8f9fa; border-radius: 8px;">
            <h2>{title}</h2>
            <p>{preview[:500]}...</p>
            <div style="margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap;">
        """

        for fmt in formats:
            html += f'<button style="padding: 8px 16px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">{fmt}</button>'

        html += """
            </div>
        </div>
        """

        return html

    def get_formats_available(self, doc_id: str) -> List[str]:
        """Get available formats for a document."""
        doc_info = self.get_document_info(doc_id)
        if doc_info:
            return list(doc_info["file_paths"].keys())
        return []

    def get_all_documents(self) -> Dict[str, Dict[str, Any]]:
        """Get all registered documents."""
        return self.documents_registry.copy()

    def generate_download_interface(self, doc_id: str) -> str:
        """
        Generate a user-friendly download interface string.

        Args:
            doc_id: Document ID

        Returns:
            Formatted string with download options
        """
        doc_info = self.get_document_info(doc_id)
        if not doc_info:
            return "❌ Document not found"

        title = doc_info["title"]
        file_paths = doc_info["file_paths"]

        result = f"""
╔═══════════════════════════════════════════════════╗
║           📄 DOCUMENT READY FOR DOWNLOAD          ║
╚═══════════════════════════════════════════════════╝

📋 Document: {title}
🆔 Document ID: {doc_id}

📥 AVAILABLE FORMATS:
"""

        for fmt, path in file_paths.items():
            if os.path.exists(path):
                size_mb = os.path.getsize(path) / (1024 * 1024)
                result += f"  ✓ {fmt:12} - {size_mb:.2f} MB  [Click to download]\n"
            else:
                result += f"  ✗ {fmt:12} - File not found\n"

        result += f"""
💾 Total Formats: {len(file_paths)}
⏱️  Generated: {doc_info['created_at']}

🔗 Share this ID: {doc_id}
   (Users can use this ID to access the document)
"""

        return result

    def create_preview_section(self, doc_id: str, max_chars: int = 1000) -> str:
        """
        Create a preview section of the document.

        Args:
            doc_id: Document ID
            max_chars: Maximum characters to show

        Returns:
            Preview text
        """
        doc_info = self.get_document_info(doc_id)
        if not doc_info:
            return "❌ Document not found"

        preview = doc_info["content_preview"]
        if len(preview) > max_chars:
            preview = preview[:max_chars] + f"\n... [{len(preview) - max_chars} more characters]"

        return f"""
📝 DOCUMENT PREVIEW:
{'─' * 50}
{preview}
{'─' * 50}
"""

    def get_file_bytes(self, doc_id: str, format_type: str) -> Optional[bytes]:
        """
        Get file bytes for download.

        Args:
            doc_id: Document ID
            format_type: Format type (PDF, Word, etc.)

        Returns:
            File bytes or None
        """
        file_path = self.get_download_link(doc_id, format_type)
        if file_path and os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as f:
                    return f.read()
            except Exception as e:
                logger.error(f"Error reading file {file_path}: {str(e)}")
                return None
        return None


class DocumentDisplayFormatter:
    """
    Format documents for display in Gradio interface.
    """

    @staticmethod
    def format_generation_result_with_download(
        result_text: str,
        doc_id: str,
        file_paths: Dict[str, str],
        preview_manager: DocumentPreviewManager
    ) -> str:
        """
        Format generation result with download links.

        Args:
            result_text: Original generation result text
            doc_id: Document ID
            file_paths: Generated file paths
            preview_manager: DocumentPreviewManager instance

        Returns:
            Formatted text with download info
        """
        download_interface = preview_manager.generate_download_interface(doc_id)

        return f"""{result_text}

{download_interface}

🎯 NEXT STEPS:
  1. Click on any format below to download
  2. Or use Document ID '{doc_id}' to access from another browser
  3. All formats contain the same content, choose your preferred format
"""

    @staticmethod
    def create_download_buttons_html(
        doc_id: str,
        formats_available: List[str]
    ) -> str:
        """
        Create HTML with download buttons.

        Args:
            doc_id: Document ID
            formats_available: List of available formats

        Returns:
            HTML for download buttons
        """
        html = f"""
        <div style="margin: 20px 0; padding: 15px; background: #e7f3ff; border-radius: 8px; border-left: 4px solid #007bff;">
            <h3 style="margin-top: 0; color: #004085;">📥 Download Your Document</h3>
            <p style="color: #004085;">Document ID: <code style="background: #fff; padding: 2px 6px;">{doc_id}</code></p>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        """

        format_colors = {
            "PDF": "#dc3545",
            "WORD": "#0078d4",
            "MARKDOWN": "#6f42c1",
            "HTML": "#fd7e14",
            "LATEX": "#28a745"
        }

        for fmt in formats_available:
            fmt_upper = fmt.upper()
            color = format_colors.get(fmt_upper, "#6c757d")
            html += f"""
                <a href="#" onclick="downloadDocument('{doc_id}', '{fmt}')" 
                   style="padding: 10px 20px; background: {color}; color: white; 
                          text-decoration: none; border-radius: 4px; font-weight: bold;
                          cursor: pointer; display: inline-block;">
                    ⬇️ Download {fmt_upper}
                </a>
            """

        html += """
            </div>
        </div>
        """

        return html

    @staticmethod
    def format_document_list(preview_manager: DocumentPreviewManager) -> str:
        """
        Format list of all generated documents.

        Args:
            preview_manager: DocumentPreviewManager instance

        Returns:
            Formatted document list
        """
        all_docs = preview_manager.get_all_documents()

        if not all_docs:
            return "📭 No documents generated yet"

        result = """
╔══════════════════════════════════════════════════════════════╗
║                  📄 GENERATED DOCUMENTS                      ║
╚══════════════════════════════════════════════════════════════╝

"""

        for i, (doc_id, doc_info) in enumerate(all_docs.items(), 1):
            formats_str = ", ".join(doc_info["file_paths"].keys())
            result += f"""
{i}. {doc_info['title']}
   ID: {doc_id}
   Formats: {formats_str}
   Created: {doc_info['created_at']}
   Accessed: {doc_info['access_count']} times

"""

        return result

    @staticmethod
    def format_download_status(doc_id: str, format_type: str, success: bool, file_path: str = "") -> str:
        """Format download status message."""
        if success:
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            return f"""
✅ DOWNLOAD SUCCESSFUL

📄 Format: {format_type}
📦 File Size: {size_mb:.2f} MB
💾 Saved to: {file_path}

Your document is ready to use!
"""
        else:
            return f"""
❌ DOWNLOAD FAILED

Format: {format_type}
Document ID: {doc_id}

Please try again or contact support.
"""


class DocumentAccessor:
    """
    Access and retrieve generated documents.
    """

    def __init__(self, preview_manager: DocumentPreviewManager):
        """Initialize document accessor."""
        self.preview_manager = preview_manager

    def get_document_for_download(self, doc_id: str, format_type: str) -> Tuple[bool, bytes, str]:
        """
        Get document bytes for download.

        Args:
            doc_id: Document ID
            format_type: Format type

        Returns:
            Tuple of (success, file_bytes, filename)
        """
        doc_info = self.preview_manager.get_document_info(doc_id)
        if not doc_info:
            return False, b"", ""

        file_path = self.preview_manager.get_download_link(doc_id, format_type)
        if not file_path or not os.path.exists(file_path):
            return False, b"", ""

        try:
            with open(file_path, 'rb') as f:
                file_bytes = f.read()

            filename = f"{doc_info['title'].replace(' ', '_')}.{format_type.lower()}"
            return True, file_bytes, filename

        except Exception as e:
            logger.error(f"Error accessing document: {str(e)}")
            return False, b"", ""

    def get_preview(self, doc_id: str) -> str:
        """Get document preview."""
        return self.preview_manager.create_preview_section(doc_id)

    def list_available_formats(self, doc_id: str) -> List[str]:
        """List available formats for a document."""
        return self.preview_manager.get_formats_available(doc_id)

    def get_document_info_formatted(self, doc_id: str) -> str:
        """Get formatted document information."""
        doc_info = self.preview_manager.get_document_info(doc_id)
        if not doc_info:
            return "❌ Document not found"

        return f"""
📄 Document Information:
  Title: {doc_info['title']}
  ID: {doc_id}
  Created: {doc_info['created_at']}
  Formats: {', '.join(doc_info['file_paths'].keys())}
  Accessed: {doc_info['access_count']} times
"""
