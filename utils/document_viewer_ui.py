"""
Document Viewer UI - Gradio interface for document preview and download
Shows generated documents with full preview and download capabilities
"""

import os
from typing import Tuple, List, Optional, Dict, Any
import json
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def create_document_preview_section(
    doc_id: str,
    title: str,
    preview_text: str,
    available_formats: List[str],
    file_sizes: Dict[str, float]
) -> str:
    """
    Create a formatted document preview section.

    Args:
        doc_id: Document ID
        title: Document title
        preview_text: Preview of document content
        available_formats: List of available formats
        file_sizes: Dict of format -> size in MB

    Returns:
        Formatted preview text
    """
    preview = f"""
╔════════════════════════════════════════════════════════════════╗
║                    📄 DOCUMENT PREVIEW                         ║
╚════════════════════════════════════════════════════════════════╝

📋 DOCUMENT: {title}
🆔 ID: {doc_id}

📝 PREVIEW CONTENT:
{'─' * 65}
{preview_text[:800]}
{'...' if len(preview_text) > 800 else ''}
{'─' * 65}

📥 DOWNLOAD OPTIONS:
"""

    for fmt in available_formats:
        size = file_sizes.get(fmt, 0)
        preview += f"  ✓ {fmt:12} ({size:.2f} MB)\n"

    preview += f"""
{'─' * 65}

💡 TIP: You can download in any format above.
   They all contain the same content!
"""

    return preview


def create_full_document_viewer(
    doc_id: str,
    title: str,
    full_content: str,
    available_formats: List[str],
    file_paths: Dict[str, str]
) -> Tuple[str, str, str]:
    """
    Create a full document viewer interface.

    Args:
        doc_id: Document ID
        title: Document title
        full_content: Full document content
        available_formats: List of available formats
        file_paths: Dict of format -> file path

    Returns:
        Tuple of (content_view, download_info, status)
    """
    # Create content view
    content_view = f"""
╔════════════════════════════════════════════════════════════════╗
║                    📖 FULL DOCUMENT VIEW                       ║
╚════════════════════════════════════════════════════════════════╝

📄 {title}

{full_content}
"""

    # Create download info
    download_info = f"""
📥 DOWNLOAD THIS DOCUMENT

Available Formats:
"""

    for fmt in available_formats:
        if fmt in file_paths:
            size_mb = os.path.getsize(file_paths[fmt]) / (1024 * 1024)
            download_info += f"  {fmt}: {size_mb:.2f} MB\n"

    download_info += f"""

Document ID: {doc_id}
Share this ID to allow others to access your document!
"""

    # Create status
    status = f"✅ Document ready for download. {len(available_formats)} formats available."

    return content_view, download_info, status


def format_download_instructions(doc_id: str, formats: List[str]) -> str:
    """Format download instructions for users."""
    return f"""
🎉 YOUR DOCUMENT IS READY!

📄 Document ID: {doc_id}

📥 DOWNLOAD OPTIONS:
{chr(10).join(f"  ✓ {fmt}" for fmt in formats)}

HOW TO ACCESS:
  1. Click on any format above to download
  2. Or copy the Document ID and share it with others
  3. Use "View Document" tab to see full content
  4. Use "Download" section to get files

💾 All formats contain identical content - choose what you need!
"""


def create_document_info_card(
    doc_id: str,
    title: str,
    doc_type: str,
    word_count: int,
    quality_score: int,
    formats_available: List[str],
    file_sizes: Dict[str, float]
) -> str:
    """
    Create an information card about the document.

    Args:
        doc_id: Document ID
        title: Document title
        doc_type: Type of document
        word_count: Word count
        quality_score: Quality score (0-100)
        formats_available: Available formats
        file_sizes: File sizes in MB

    Returns:
        Formatted info card
    """
    quality_bar = "█" * (quality_score // 10) + "░" * (10 - quality_score // 10)

    card = f"""
┌────────────────────────────────────────────────────────┐
│                  📊 DOCUMENT INFORMATION               │
├────────────────────────────────────────────────────────┤
│ Title:        {title[:45]:45} │
│ ID:           {doc_id[:45]:45} │
│ Type:         {doc_type[:45]:45} │
│ Word Count:   {str(word_count)[:45]:45} │
│ Quality:      [{quality_bar}] {quality_score}%       │
│ Formats:      {', '.join(formats_available[:2])[:35]}... │
├────────────────────────────────────────────────────────┤
"""

    card += "│ FILE SIZES:                                            │\n"
    for fmt, size in file_sizes.items():
        card += f"│   {fmt:12} {size:8.2f} MB                            │\n"

    card += "└────────────────────────────────────────────────────────┘\n"

    return card


def create_tabbed_document_view(
    doc_id: str,
    title: str,
    content: str,
    formats: List[str],
    file_paths: Dict[str, str],
    metadata: Dict[str, Any]
) -> Tuple[str, str, str, str]:
    """
    Create a multi-tabbed document view interface.

    Returns:
        Tuple of (overview, content, download, metadata_view)
    """
    # Overview tab
    word_count = metadata.get("word_count", 0)
    quality = metadata.get("quality_score", 0)
    reading_time = metadata.get("reading_time", 0)

    overview = f"""
{'═' * 60}
📄 DOCUMENT OVERVIEW
{'═' * 60}

Title: {title}
Document ID: {doc_id}

📊 STATISTICS:
  • Word Count: {word_count:,} words
  • Quality Score: {quality}%
  • Estimated Reading Time: {reading_time} minutes
  • Available Formats: {len(formats)}

🔗 DOWNLOAD: Choose a format below
🔍 VIEW: Check the "Content" tab for full document
📋 INFO: See metadata in the "Info" tab
"""

    # Content tab
    content_view = f"""
{'═' * 60}
📖 {title}
{'═' * 60}

{content}

{'═' * 60}
End of document
"""

    # Download tab
    download_view = f"""
{'═' * 60}
📥 DOWNLOAD OPTIONS
{'═' * 60}

Document: {title}
ID: {doc_id}

AVAILABLE FORMATS:
"""

    for fmt in formats:
        if fmt in file_paths:
            size_mb = os.path.getsize(file_paths[fmt]) / (1024 * 1024)
            download_view += f"\n✓ {fmt}\n  Size: {size_mb:.2f} MB\n  [Click to download above]\n"

    download_view += f"""

All formats contain the same content.
Choose based on your preference:
  • PDF: Best for sharing and printing
  • Word: Best for editing
  • Markdown: Best for version control
  • HTML: Best for web viewing
"""

    # Metadata tab
    metadata_view = f"""
{'═' * 60}
ℹ️ DOCUMENT METADATA
{'═' * 60}

{json.dumps(metadata, indent=2, default=str)}
"""

    return overview, content_view, download_view, metadata_view


def create_quick_download_html(doc_id: str, formats: List[str]) -> str:
    """Create quick download HTML with buttons."""
    html = f"""
    <div style="padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 10px; color: white; text-align: center;">
        <h2 style="margin-top: 0;">✅ Document Generated Successfully!</h2>
        <p style="font-size: 18px; margin: 10px 0;">
            Download your document now:
        </p>
        <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
    """

    format_icons = {
        "PDF": "📄",
        "WORD": "📝",
        "MARKDOWN": "📋",
        "HTML": "🌐",
        "LATEX": "📐"
    }

    for fmt in formats:
        icon = format_icons.get(fmt.upper(), "📥")
        html += f"""
            <div style="background: rgba(255,255,255,0.2); padding: 15px 20px; 
                       border-radius: 8px; cursor: pointer; transition: all 0.3s;
                       border: 2px solid transparent;">
                <div style="font-size: 24px;">{icon}</div>
                <div style="font-weight: bold; margin-top: 5px;">{fmt}</div>
                <div style="font-size: 12px; margin-top: 3px;">Document ID: {doc_id}</div>
            </div>
        """

    html += """
        </div>
        <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.3);">
            <p style="margin: 0; font-size: 14px;">
                💡 Tip: All formats contain the same content. Choose what works best for you!
            </p>
        </div>
    </div>
    """

    return html


def get_document_view_instructions() -> str:
    """Get instructions for viewing documents."""
    return """
### 📥 View & Download Generated Documents

Your documents are automatically saved and available for download in multiple formats.

#### 📋 How to Access Your Documents:

1. **Immediate Download** - Download links appear right after generation
2. **Document ID** - Use the document ID to access it later
3. **Multiple Formats** - Choose the format that works best for you
4. **Preview** - View content before downloading

#### 📂 Available Formats:

- **PDF** 📄 - Professional format, great for sharing and printing
- **Word** 📝 - Editable format (DOCX), perfect for further editing
- **Markdown** 📋 - Plain text format, great for version control
- **HTML** 🌐 - Web format, view in any browser
- **LaTeX** 📐 - Scientific format for academic papers

#### 💾 Where Files Are Stored:

- All generated documents are saved in the `generated_documents/` folder
- Files are named after your document title
- Each format is saved separately but contains identical content

#### 🔗 Sharing Documents:

- Use the **Document ID** to share with others
- Recipients can access the preview and download options
- All files are stored locally for privacy

#### ⚙️ Technical Info:

- Document ID: Unique identifier for your document
- File Size: Varies by format (HTML usually smallest, PDF largest)
- Quality Score: Indicates content quality (0-100%)
- Word Count: Total words in the document
"""


def create_access_history_display(documents: Dict[str, Dict[str, Any]]) -> str:
    """Create a display of document access history."""
    if not documents:
        return "No documents generated yet."

    display = """
╔════════════════════════════════════════════════════════════════╗
║                    📜 YOUR DOCUMENTS                           ║
╚════════════════════════════════════════════════════════════════╝

"""

    for i, (doc_id, info) in enumerate(documents.items(), 1):
        display += f"""
{i}. {info.get('title', 'Untitled')}
   📆 Created: {info.get('created_at', 'Unknown')}
   🆔 ID: {doc_id}
   📊 Formats: {', '.join(info.get('file_paths', {}).keys())}
   👁️  Accessed: {info.get('access_count', 0)} times

"""

    return display
