"""
PDF Generator - Generate professional PDF documents
"""

import io
from typing import Dict, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class PDFGenerator:
    """
    Generate professional PDF documents with formatting, headers, footers, and citations.
    """

    def __init__(self):
        """Initialize PDF generator."""
        self.page_size = "A4"
        self.margins = {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0}
        self.font_name = "Arial"
        self.font_size = 12
        self.line_spacing = 1.5

    def generate_pdf(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
    ) -> bytes:
        """
        Generate PDF document.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations

        Returns:
            PDF bytes
        """
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
            from reportlab.lib import colors

            # Create PDF in memory
            pdf_buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                pdf_buffer,
                pagesize=A4,
                rightMargin=1 * inch,
                leftMargin=1 * inch,
                topMargin=1 * inch,
                bottomMargin=1 * inch,
            )

            # Create story (content)
            story = []

            # Add title page
            story.extend(self._create_title_page(title, author))
            story.append(PageBreak())

            # Add table of contents
            if include_toc:
                story.extend(self._create_toc(content))
                story.append(PageBreak())

            # Add sections
            styles = getSampleStyleSheet()
            for section_title, section_content in content.items():
                story.append(Paragraph(section_title, styles["Heading1"]))
                story.append(Spacer(1, 0.2 * inch))

                # Split content into paragraphs
                paragraphs = section_content.split("\n\n")
                for para_text in paragraphs:
                    if para_text.strip():
                        story.append(Paragraph(para_text, styles["Normal"]))
                        story.append(Spacer(1, 0.1 * inch))

                story.append(Spacer(1, 0.3 * inch))

            # Add bibliography
            if include_citations and citations:
                story.append(PageBreak())
                story.append(Paragraph("References", styles["Heading1"]))
                story.append(Spacer(1, 0.2 * inch))

                for citation in citations:
                    story.append(Paragraph(citation, styles["Normal"]))
                    story.append(Spacer(1, 0.1 * inch))

            # Build PDF
            doc.build(story)
            pdf_buffer.seek(0)
            return pdf_buffer.getvalue()

        except ImportError:
            logger.warning("reportlab not available, using fallback")
            return self._generate_pdf_fallback(title, content)

    def _create_title_page(self, title: str, author: str) -> list:
        """Create title page elements."""
        try:
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.platypus import Paragraph, Spacer
            from reportlab.lib.units import inch

            styles = getSampleStyleSheet()
            story = []

            story.append(Spacer(1, 1 * inch))
            story.append(Paragraph(title, styles["Title"]))
            story.append(Spacer(1, 0.5 * inch))
            story.append(Paragraph(f"By {author}", styles["Normal"]))
            story.append(Spacer(1, 0.2 * inch))
            story.append(Paragraph(datetime.now().strftime("%B %d, %Y"), styles["Normal"]))

            return story
        except:
            return []

    def _create_toc(self, content: Dict[str, str]) -> list:
        """Create table of contents."""
        try:
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.platypus import Paragraph, Spacer
            from reportlab.lib.units import inch

            styles = getSampleStyleSheet()
            story = []

            story.append(Paragraph("Table of Contents", styles["Heading1"]))
            story.append(Spacer(1, 0.3 * inch))

            for i, section in enumerate(content.keys(), 1):
                story.append(Paragraph(f"{i}. {section}", styles["Normal"]))
                story.append(Spacer(1, 0.1 * inch))

            return story
        except:
            return []

    def _generate_pdf_fallback(self, title: str, content: Dict[str, str]) -> bytes:
        """Fallback PDF generation using fpdf2."""
        try:
            from fpdf import FPDF

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)

            # Title
            pdf.cell(0, 10, title, ln=True, align="C")
            pdf.ln(10)

            # Content
            pdf.set_font("Arial", "", 12)
            for section_title, section_content in content.items():
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, section_title, ln=True)
                pdf.set_font("Arial", "", 12)

                # Add content with text wrapping
                for line in section_content.split("\n"):
                    pdf.multi_cell(0, 10, line)
                pdf.ln(5)

            return pdf.output(dest="S").encode("latin-1")

        except ImportError:
            # Fallback to simple text
            return f"PDF Generation Failed - {title}".encode("utf-8")

    def add_header_footer(self, pdf_content: bytes, header: str = "", footer: str = "") -> bytes:
        """
        Add header and footer to PDF.

        Args:
            pdf_content: Original PDF bytes
            header: Header text
            footer: Footer text

        Returns:
            PDF with header/footer
        """
        try:
            from PyPDF2 import PdfReader, PdfWriter
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            import io

            # Create header/footer canvas
            header_buffer = io.BytesIO()
            c = canvas.Canvas(header_buffer, pagesize=A4)
            c.setFont("Arial", 10)

            if header:
                c.drawString(50, 750, header)
            if footer:
                c.drawString(50, 30, footer)

            c.save()
            header_buffer.seek(0)

            # Merge with original PDF
            reader = PdfReader(io.BytesIO(pdf_content))
            writer = PdfWriter()

            for page in reader.pages:
                page.merge_page(PdfReader(header_buffer).pages[0])
                writer.add_page(page)

            output_buffer = io.BytesIO()
            writer.write(output_buffer)
            output_buffer.seek(0)

            return output_buffer.getvalue()

        except:
            return pdf_content  # Return original if header/footer fails

    def extract_text_from_pdf(self, pdf_content: bytes) -> str:
        """
        Extract text from PDF.

        Args:
            pdf_content: PDF bytes

        Returns:
            Extracted text
        """
        try:
            import pdfplumber
            import io

            with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() + "\n"

            return text

        except:
            return "PDF text extraction failed"
