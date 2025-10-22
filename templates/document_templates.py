"""
Document Templates - Pre-built document templates
"""


class DocumentTemplates:
    """Pre-built document templates for common document types."""

    RESEARCH_PAPER = {
        "name": "Research Paper",
        "sections": [
            "Abstract",
            "Introduction",
            "Literature Review",
            "Methodology",
            "Results",
            "Discussion",
            "Conclusion",
            "References",
        ],
        "description": "Standard academic research paper format",
    }

    ESSAY = {
        "name": "Essay",
        "sections": [
            "Introduction",
            "Body Paragraph 1",
            "Body Paragraph 2",
            "Body Paragraph 3",
            "Conclusion",
        ],
        "description": "Standard essay format with intro and multiple body sections",
    }

    LAB_REPORT = {
        "name": "Lab Report",
        "sections": [
            "Title Page",
            "Objective",
            "Introduction",
            "Procedure",
            "Results",
            "Analysis",
            "Conclusion",
            "References",
        ],
        "description": "Science/engineering lab report format",
    }

    THESIS = {
        "name": "Thesis",
        "sections": [
            "Title Page",
            "Abstract",
            "Table of Contents",
            "Introduction",
            "Literature Review",
            "Methodology",
            "Results",
            "Discussion",
            "Implications",
            "Conclusion",
            "References",
            "Appendices",
        ],
        "description": "Complete thesis/dissertation format",
    }

    BUSINESS_REPORT = {
        "name": "Business Report",
        "sections": [
            "Executive Summary",
            "Introduction",
            "Background",
            "Findings",
            "Analysis",
            "Recommendations",
            "Conclusion",
            "Appendices",
        ],
        "description": "Professional business report format",
    }

    @staticmethod
    def get_all_templates() -> dict:
        """Get all available templates."""
        return {
            "research_paper": DocumentTemplates.RESEARCH_PAPER,
            "essay": DocumentTemplates.ESSAY,
            "lab_report": DocumentTemplates.LAB_REPORT,
            "thesis": DocumentTemplates.THESIS,
            "business_report": DocumentTemplates.BUSINESS_REPORT,
        }

    @staticmethod
    def get_template(template_name: str) -> dict:
        """Get specific template."""
        templates = DocumentTemplates.get_all_templates()
        return templates.get(template_name.lower(), templates["research_paper"])

    @staticmethod
    def get_template_names() -> list:
        """Get list of available template names."""
        return list(DocumentTemplates.get_all_templates().keys())
