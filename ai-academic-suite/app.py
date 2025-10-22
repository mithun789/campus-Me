"""ai-academic-suite: Main Gradio application

This is a minimal, functional Gradio app that demonstrates the core flows:
- Upload/paste content
- Generate an academic-style document (simple generator)
- Export to PDF, DOCX, Markdown, HTML, LaTeX

Designed for Hugging Face Spaces (Gradio).
"""
from __future__ import annotations

import io
import os
from datetime import datetime
from typing import List, Dict

import gradio as gr

from src.ai_engine.content_generator import generate_academic_content
from src.ai_engine.citation_manager import CitationManager
from src.document_engine.pdf_generator import PDFGenerator
from src.document_engine.word_generator import WordGenerator
from src.document_engine.markdown_generator import MarkdownGenerator
from src.document_engine.html_generator import HTMLGenerator
from src.document_engine.latex_generator import LaTeXGenerator
from src.visual_engine.chart_generator import ChartGenerator

CONFIG = {
    "APP_TITLE": "AI Academic Document Suite (Demo)",
}


def generate_and_export(notes: str, requirements: str, formats: List[str], citation_style: str):
    """Pipeline: generate content, visuals, citations, and export requested formats.

    Returns a dict of format -> bytes for download and a short preview text.
    """
    # 1. Generate content (simple structured dict)
    content = generate_academic_content(notes or "", requirements or "")

    # 2. Citations
    cm = CitationManager()
    bibliography = cm.format_bibliography(content.get("citations", []), style=citation_style)
    content["bibliography"] = bibliography

    # 3. Visuals (generate a demo chart if needed)
    chart_png = None
    if content.get("tables") or content.get("data_examples"):
        cg = ChartGenerator()
        chart_png = cg.simple_demo_chart()

    # 4. Export
    outputs = {}
    if "pdf" in formats:
        pdf = PDFGenerator()
        pdf_bytes = pdf.create_pdf(content, chart_png)
        outputs["pdf"] = pdf_bytes
    if "docx" in formats or "word" in formats:
        wg = WordGenerator()
        docx_bytes = wg.create_docx(content)
        outputs["docx"] = docx_bytes
    if "md" in formats:
        mg = MarkdownGenerator()
        outputs["md"] = mg.create_markdown(content)
    if "html" in formats:
        hg = HTMLGenerator()
        outputs["html"] = hg.create_html(content)
    if "latex" in formats:
        lg = LaTeXGenerator()
        outputs["latex"] = lg.create_latex(content)

    preview = "\n\n".join([f"{s['heading']}\n{(s['text'][:400] + '...') if len(s['text'])>400 else s['text']}" for s in content.get("sections", [])[:3]])

    return outputs, preview


def bytes_to_download_link(file_bytes: bytes, filename: str):
    return (filename, io.BytesIO(file_bytes))


def build_ui():
    with gr.Blocks(title=CONFIG["APP_TITLE"]) as demo:
        gr.Markdown("# AI Academic Document Suite — Demo\nThis demo generates simple multi-format academic documents with visuals and citations. For research/educational use only.")

        with gr.Tabs():
            with gr.TabItem("📄 Generate Document"):
                notes_in = gr.Textbox(label="Lecture notes / Source (paste)", lines=6)
                reqs_in = gr.Textbox(label="Assignment requirements", lines=3)
                formats = gr.CheckboxGroup(choices=["pdf", "docx", "md", "html", "latex"], value=["pdf", "docx"], label="Export formats")
                citation_style = gr.Dropdown(choices=["APA", "MLA", "Chicago"], value="APA", label="Citation style")
                generate_btn = gr.Button("Generate Complete Document")
                output_preview = gr.Textbox(label="Preview", lines=10)
                downloads = gr.Files(label="Download files")

                def on_generate(notes, reqs, formats_sel, c_style):
                    outputs, preview = generate_and_export(notes, reqs, formats_sel, c_style)
                    files = []
                    for fmt, data in outputs.items():
                        if isinstance(data, bytes):
                            fname = f"document.{ 'pdf' if fmt=='pdf' else ('docx' if fmt=='docx' else fmt) }"
                            files.append(bytes_to_download_link(data, fname))
                        elif isinstance(data, io.BytesIO):
                            files.append((f"document.{fmt}", data))
                        elif isinstance(data, str):
                            files.append((f"document.{fmt}", io.BytesIO(data.encode("utf-8"))))
                    return preview, files

                generate_btn.click(on_generate, inputs=[notes_in, reqs_in, formats, citation_style], outputs=[output_preview, downloads])

            with gr.TabItem("📊 Data & Visualizations"):
                gr.Markdown("Upload CSV/Excel to generate charts — demo tab.")
                csv_in = gr.File(label="Upload CSV")
                analyze_btn = gr.Button("Analyze & Suggest Visuals")
                analyze_out = gr.Textbox(label="Suggestions", lines=6)

                def analyze_demo(file):
                    if not file:
                        return "No file uploaded. Paste small CSV to test."
                    return "Detected data and suggested: bar chart for categorical comparisons; line chart for trends."

                analyze_btn.click(analyze_demo, inputs=[csv_in], outputs=[analyze_out])

            with gr.TabItem("📚 Document Templates"):
                gr.Markdown("Pre-built templates available: Research Paper, Essay, Report (demo).")

            with gr.TabItem("🔍 Analysis & Research"):
                gr.Markdown("Quality metrics, detection, and transparency logs (demo).")

            with gr.TabItem("⚙️ Advanced Settings"):
                gr.Markdown("Configure citation style, formatting, and model parameters (demo).")

            with gr.TabItem("📖 About & Ethics"):
                gr.Markdown("## About this demo\nThis project is for research and educational purposes. Do not submit AI-generated text as original work. See README for details.")

    return demo


if __name__ == "__main__":
    ui = build_ui()
    ui.launch()
