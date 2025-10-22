"""
LaTeX Generator - Generate LaTeX documents
"""

from typing import Dict, List, Optional
from datetime import datetime


class LaTeXGenerator:
    """
    Generate LaTeX documents for advanced academic formatting.
    """

    def __init__(self):
        """Initialize LaTeX generator."""
        pass

    def generate_latex(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
        document_class: str = "article",
    ) -> str:
        """
        Generate LaTeX document.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations
            document_class: LaTeX document class (article, report, book)

        Returns:
            LaTeX string
        """
        latex_parts = []

        # Document header
        latex_parts.append(f"\\documentclass{{{document_class}}}")
        latex_parts.append("\\usepackage[utf-8]{inputenc}")
        latex_parts.append("\\usepackage{babel}")
        latex_parts.append("\\usepackage{graphicx}")
        latex_parts.append("\\usepackage{hyperref}")
        latex_parts.append("\\usepackage{amsmath}")
        latex_parts.append("\\usepackage{cite}")

        # Document metadata
        latex_parts.append(f"\\title{{{title}}}")
        latex_parts.append(f"\\author{{{author}}}")
        latex_parts.append(f"\\date{{{datetime.now().strftime('%B %d, %Y')}}}")

        # Begin document
        latex_parts.append("\\begin{document}")
        latex_parts.append("\\maketitle")

        # Table of contents
        if include_toc:
            latex_parts.append("\\tableofcontents")
            latex_parts.append("\\newpage")

        # Sections
        for section_title, section_content in content.items():
            latex_parts.append(f"\\section{{{section_title}}}")
            latex_parts.append(self._sanitize_latex(section_content))
            latex_parts.append("")

        # Bibliography
        if include_citations and citations:
            latex_parts.append("\\begin{thebibliography}{99}")
            for citation in citations:
                latex_parts.append(f"\\bibitem{{ref}} {self._sanitize_latex(citation)}")
            latex_parts.append("\\end{thebibliography}")

        # End document
        latex_parts.append("\\end{document}")

        return "\n".join(latex_parts)

    def generate_latex_bytes(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
        document_class: str = "article",
    ) -> bytes:
        """
        Generate LaTeX as bytes.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations
            document_class: LaTeX document class

        Returns:
            LaTeX bytes
        """
        latex = self.generate_latex(
            title, content, author, include_toc, include_citations, citations, document_class
        )
        return latex.encode("utf-8")

    def _sanitize_latex(self, text: str) -> str:
        """
        Sanitize text for LaTeX special characters.

        Args:
            text: Text to sanitize

        Returns:
            Sanitized text
        """
        # Escape special LaTeX characters
        special_chars = {
            "\\": "\\textbackslash{}",
            "&": "\\&",
            "%": "\\%",
            "$": "\\$",
            "#": "\\#",
            "_": "\\_",
            "{": "\\{",
            "}": "\\}",
            "~": "\\textasciitilde{}",
            "^": "\\textasciicircum{}",
        }

        for char, escape in special_chars.items():
            text = text.replace(char, escape)

        return text

    def create_latex_table(self, headers: List[str], rows: List[List[str]]) -> str:
        """
        Create LaTeX table.

        Args:
            headers: Table headers
            rows: Table rows

        Returns:
            LaTeX table string
        """
        num_cols = len(headers)
        col_spec = "c" * num_cols

        latex_table = f"\\begin{{tabular}}{{{col_spec}}}\n"
        latex_table += " & ".join(headers) + " \\\\\n"
        latex_table += "\\hline\n"

        for row in rows:
            latex_table += " & ".join(self._sanitize_latex(str(cell)) for cell in row) + " \\\\\n"

        latex_table += "\\end{tabular}"

        return latex_table

    def create_latex_figure(
        self, image_path: str, caption: str = "", label: str = "fig:1", width: str = "0.8"
    ) -> str:
        """
        Create LaTeX figure environment.

        Args:
            image_path: Path to image file
            caption: Figure caption
            label: Figure label for referencing
            width: Figure width (as fraction of textwidth)

        Returns:
            LaTeX figure string
        """
        latex_fig = f"""
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width={width}\\textwidth]{{{image_path}}}
    \\caption{{{caption}}}
    \\label{{{label}}}
\\end{{figure}}
        """
        return latex_fig

    def create_latex_equation(self, equation: str, label: str = "eq:1") -> str:
        """
        Create LaTeX equation.

        Args:
            equation: Mathematical equation
            label: Equation label for referencing

        Returns:
            LaTeX equation string
        """
        return f"""
\\begin{{equation}}
    {equation}
    \\label{{{label}}}
\\end{{equation}}
        """

    def create_latex_section(self, title: str, content: str, subsections: Optional[Dict] = None) -> str:
        """
        Create LaTeX section with optional subsections.

        Args:
            title: Section title
            content: Section content
            subsections: Dictionary of subsection titles and content

        Returns:
            LaTeX section string
        """
        latex = f"\\section{{{title}}}\n{content}\n"

        if subsections:
            for sub_title, sub_content in subsections.items():
                latex += f"\\subsection{{{sub_title}}}\n{sub_content}\n"

        return latex

    def compile_to_pdf(self, latex_content: str, output_path: str) -> bool:
        """
        Compile LaTeX to PDF (requires pdflatex installed).

        Args:
            latex_content: LaTeX document content
            output_path: Output PDF file path

        Returns:
            Success status
        """
        try:
            import subprocess
            import tempfile
            import os

            # Create temporary tex file
            with tempfile.NamedTemporaryFile(mode="w", suffix=".tex", delete=False) as f:
                f.write(latex_content)
                tex_file = f.name

            try:
                # Compile LaTeX to PDF
                subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "-output-directory", os.path.dirname(output_path), tex_file],
                    check=True,
                    capture_output=True,
                )

                return True

            finally:
                # Clean up temporary file
                os.unlink(tex_file)

        except:
            return False
