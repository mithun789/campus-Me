"""
Markdown Generator - Generate .md files
"""

from typing import Dict, List, Optional
from datetime import datetime


class MarkdownGenerator:
    """
    Generate Markdown (.md) files with proper formatting.
    """

    def __init__(self):
        """Initialize Markdown generator."""
        pass

    def generate_markdown(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
    ) -> str:
        """
        Generate Markdown content.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations

        Returns:
            Markdown string
        """
        md_content = []

        # Add title
        md_content.append(f"# {title}\n")

        # Add metadata
        md_content.append(f"**Author:** {author}\n")
        md_content.append(f"**Date:** {datetime.now().strftime('%B %d, %Y')}\n\n")
        md_content.append("---\n\n")

        # Add table of contents
        if include_toc:
            md_content.append("## Table of Contents\n\n")
            for i, section in enumerate(content.keys(), 1):
                # Create anchor link
                anchor = section.lower().replace(" ", "-")
                md_content.append(f"{i}. [{section}](#{anchor})\n")
            md_content.append("\n---\n\n")

        # Add sections
        for section_title, section_content in content.items():
            md_content.append(f"## {section_title}\n\n")
            md_content.append(section_content)
            md_content.append("\n\n")

        # Add bibliography
        if include_citations and citations:
            md_content.append("---\n\n")
            md_content.append("## References\n\n")
            for i, citation in enumerate(citations, 1):
                md_content.append(f"{i}. {citation}\n\n")

        return "".join(md_content)

    def generate_markdown_bytes(
        self,
        title: str,
        content: Dict[str, str],
        author: str = "AI Academic Suite",
        include_toc: bool = True,
        include_citations: bool = False,
        citations: List[str] = None,
    ) -> bytes:
        """
        Generate Markdown content as bytes.

        Args:
            title: Document title
            content: Dictionary of section titles and content
            author: Document author
            include_toc: Include table of contents
            include_citations: Include bibliography
            citations: List of citations

        Returns:
            Markdown bytes
        """
        md_text = self.generate_markdown(
            title, content, author, include_toc, include_citations, citations
        )
        return md_text.encode("utf-8")

    def add_formatting(self, text: str, formatting_type: str = "emphasis") -> str:
        """
        Add Markdown formatting to text.

        Args:
            text: Text to format
            formatting_type: Type of formatting (bold, italic, code, etc.)

        Returns:
            Formatted text
        """
        if formatting_type == "bold":
            return f"**{text}**"
        elif formatting_type == "italic":
            return f"*{text}*"
        elif formatting_type == "code":
            return f"`{text}`"
        elif formatting_type == "code_block":
            return f"```\n{text}\n```"
        elif formatting_type == "quote":
            return f"> {text}"
        elif formatting_type == "link":
            # Assumes text format: "label|url"
            if "|" in text:
                label, url = text.split("|", 1)
                return f"[{label}]({url})"
            return text
        else:
            return text

    def convert_html_to_markdown(self, html_content: str) -> str:
        """
        Convert HTML to Markdown.

        Args:
            html_content: HTML string

        Returns:
            Markdown string
        """
        try:
            from html2text import HTML2Text

            h = HTML2Text()
            h.ignore_links = False
            return h.handle(html_content)

        except ImportError:
            # Fallback basic conversion
            import re

            md_content = html_content

            # Basic HTML to Markdown conversions
            md_content = re.sub(r"<h1>(.*?)</h1>", r"# \1", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<h2>(.*?)</h2>", r"## \1", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<h3>(.*?)</h3>", r"### \1", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<b>(.*?)</b>", r"**\1**", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<i>(.*?)</i>", r"*\1*", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<code>(.*?)</code>", r"`\1`", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<p>(.*?)</p>", r"\1\n\n", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<a href=['\"]([^'\"]+)['\"]>(.*?)</a>", r"[\2](\1)", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<br\s*/?>", r"\n", md_content, flags=re.IGNORECASE)
            md_content = re.sub(r"<[^>]+>", "", md_content)  # Remove remaining tags

            return md_content

    def create_table(self, headers: List[str], rows: List[List[str]]) -> str:
        """
        Create Markdown table.

        Args:
            headers: Table column headers
            rows: List of rows (each row is list of cell values)

        Returns:
            Markdown table string
        """
        md_table = "| " + " | ".join(headers) + " |\n"
        md_table += "|" + "|".join(["---" for _ in headers]) + "|\n"

        for row in rows:
            md_table += "| " + " | ".join(str(cell) for cell in row) + " |\n"

        return md_table

    def create_code_block(self, code: str, language: str = "") -> str:
        """
        Create Markdown code block.

        Args:
            code: Code content
            language: Programming language for syntax highlighting

        Returns:
            Markdown code block
        """
        return f"```{language}\n{code}\n```"

    def create_list(self, items: List[str], ordered: bool = False) -> str:
        """
        Create Markdown list.

        Args:
            items: List items
            ordered: Whether to create ordered (numbered) list

        Returns:
            Markdown list
        """
        if ordered:
            return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
        else:
            return "\n".join(f"- {item}" for item in items)

    def create_task_list(self, tasks: Dict[str, bool]) -> str:
        """
        Create Markdown task list.

        Args:
            tasks: Dictionary of task descriptions and completion status

        Returns:
            Markdown task list
        """
        task_list = ""
        for task, completed in tasks.items():
            checkbox = "[x]" if completed else "[ ]"
            task_list += f"{checkbox} {task}\n"

        return task_list
