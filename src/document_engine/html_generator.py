"""
HTML Generator - Generate HTML documents
"""

from typing import Dict, List, Optional
from datetime import datetime


class HTMLGenerator:
    """
    Generate HTML documents with CSS styling.
    """

    def __init__(self):
        """Initialize HTML generator."""
        self.default_css = self._get_default_css()

    def generate_html(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
        custom_css: Optional[str] = None,
    ) -> str:
        """
        Generate HTML document.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations
            custom_css: Custom CSS styles

        Returns:
            HTML string
        """
        html_parts = []

        # HTML header
        html_parts.append("<!DOCTYPE html>")
        html_parts.append("<html lang='en'>")
        html_parts.append("<head>")
        html_parts.append("<meta charset='UTF-8'>")
        html_parts.append("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
        html_parts.append(f"<title>{title}</title>")

        # Add CSS
        css = custom_css if custom_css else self.default_css
        html_parts.append(f"<style>{css}</style>")

        html_parts.append("</head>")
        html_parts.append("<body>")

        # Title page
        html_parts.append("<header>")
        html_parts.append(f"<h1>{title}</h1>")
        html_parts.append(f"<p class='author'>By {author}</p>")
        html_parts.append(f"<p class='date'>{datetime.now().strftime('%B %d, %Y')}</p>")
        html_parts.append("</header>")

        # Table of contents
        if include_toc:
            html_parts.append("<nav class='toc'>")
            html_parts.append("<h2>Table of Contents</h2>")
            html_parts.append("<ul>")
            for i, section in enumerate(content.keys(), 1):
                anchor = section.lower().replace(" ", "-")
                html_parts.append(f"<li><a href='#{anchor}'>{i}. {section}</a></li>")
            html_parts.append("</ul>")
            html_parts.append("</nav>")
            html_parts.append("<hr>")

        # Main content
        html_parts.append("<main>")
        for section_title, section_content in content.items():
            anchor = section_title.lower().replace(" ", "-")
            html_parts.append(f"<section id='{anchor}'>")
            html_parts.append(f"<h2>{section_title}</h2>")

            # Convert paragraph breaks
            for para in section_content.split("\n\n"):
                if para.strip():
                    html_parts.append(f"<p>{para}</p>")

            html_parts.append("</section>")

        html_parts.append("</main>")

        # Bibliography
        if include_citations and citations:
            html_parts.append("<footer>")
            html_parts.append("<h2>References</h2>")
            html_parts.append("<ol class='references'>")
            for citation in citations:
                html_parts.append(f"<li>{citation}</li>")
            html_parts.append("</ol>")
            html_parts.append("</footer>")

        html_parts.append("</body>")
        html_parts.append("</html>")

        return "\n".join(html_parts)

    def generate_html_bytes(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
        custom_css: Optional[str] = None,
    ) -> bytes:
        """
        Generate HTML as bytes.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations
            custom_css: Custom CSS styles

        Returns:
            HTML bytes
        """
        html = self.generate_html(
            title, content, author, include_toc, include_citations, citations, custom_css
        )
        return html.encode("utf-8")

    def _get_default_css(self) -> str:
        """Get default CSS styling."""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Calibri', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #fff;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
        }
        
        header {
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 2px solid #333;
            padding-bottom: 20px;
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .author {
            font-size: 1.1em;
            font-weight: bold;
        }
        
        .date {
            color: #666;
            font-style: italic;
        }
        
        nav.toc {
            background-color: #f5f5f5;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid #007bff;
        }
        
        nav.toc h2 {
            margin-bottom: 15px;
        }
        
        nav.toc ul {
            list-style-position: inside;
        }
        
        nav.toc a {
            color: #007bff;
            text-decoration: none;
        }
        
        nav.toc a:hover {
            text-decoration: underline;
        }
        
        main {
            margin: 40px 0;
        }
        
        section {
            margin-bottom: 30px;
        }
        
        h2 {
            font-size: 1.8em;
            margin-top: 30px;
            margin-bottom: 15px;
            color: #222;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
        }
        
        h3 {
            font-size: 1.3em;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        p {
            margin-bottom: 15px;
            text-align: justify;
        }
        
        hr {
            margin: 30px 0;
            border: none;
            border-top: 1px solid #ddd;
        }
        
        footer {
            margin-top: 40px;
            border-top: 2px solid #333;
            padding-top: 20px;
        }
        
        footer h2 {
            font-size: 1.5em;
        }
        
        .references {
            margin-left: 30px;
            line-height: 1.8;
        }
        
        .references li {
            margin-bottom: 10px;
        }
        
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 15px 0;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        blockquote {
            border-left: 4px solid #007bff;
            padding-left: 15px;
            margin: 15px 0;
            font-style: italic;
            color: #555;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        table th, table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        table th {
            background-color: #f4f4f4;
            font-weight: bold;
        }
        
        table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        @media print {
            body {
                padding: 0;
            }
            nav.toc {
                page-break-after: always;
            }
        }
        """

    def create_html_table(self, headers: List[str], rows: List[List[str]]) -> str:
        """
        Create HTML table.

        Args:
            headers: Table headers
            rows: Table rows

        Returns:
            HTML table string
        """
        html = "<table>\n<thead>\n<tr>\n"

        for header in headers:
            html += f"<th>{header}</th>\n"

        html += "</tr>\n</thead>\n<tbody>\n"

        for row in rows:
            html += "<tr>\n"
            for cell in row:
                html += f"<td>{cell}</td>\n"
            html += "</tr>\n"

        html += "</tbody>\n</table>"

        return html

    def create_responsive_layout(self, left_content: str, right_content: str) -> str:
        """
        Create responsive two-column layout.

        Args:
            left_content: Left column HTML
            right_content: Right column HTML

        Returns:
            HTML with two-column layout
        """
        layout_css = """
        <style>
            .responsive-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }
            @media (max-width: 768px) {
                .responsive-container {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """

        return f"""
        {layout_css}
        <div class="responsive-container">
            <div class="left-column">{left_content}</div>
            <div class="right-column">{right_content}</div>
        </div>
        """
