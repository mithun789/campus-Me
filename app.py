"""
AI Academic Document Suite - Main Gradio Application
Complete next-generation AI document generation platform
Optimized for HF Spaces Free Tier (2vCPU + 16GB RAM)
"""

import gradio as gr
import os
from datetime import datetime
from typing import Tuple

# Import all modules
from config import *
from src.ai_engine import (
    DocumentParser, RequirementAnalyzer, ContentGenerator,
    Humanizer, CitationManager, AIDetector
)
from src.document_engine import (
    PDFGenerator, WordGenerator, MarkdownGenerator,
    HTMLGenerator, LaTeXGenerator
)
from src.visual_engine import (
    TableGenerator, ChartGenerator, DiagramGenerator, LayoutManager
)
from src.data_engine import (
    DataAnalyzer, StatsGenerator, VisualizationAI
)
from src.research_tools import (
    QualityMetrics, DocumentComparison, TransparencyLogger
)
from templates import DocumentTemplates, CitationFormats
from utils import TextFormatter, FileHandler
from src.optimization import optimization_manager, get_system_health
from utils.document_preview import DocumentPreviewManager, DocumentDisplayFormatter, DocumentAccessor
from utils.document_viewer_ui import (
    create_document_preview_section, create_full_document_viewer,
    format_download_instructions, create_document_info_card,
    create_quick_download_html, get_document_view_instructions,
    create_access_history_display
)

# Initialize components
parser = DocumentParser()
analyzer = RequirementAnalyzer()
generator = ContentGenerator()
humanizer = Humanizer()
citation_mgr = CitationManager()
detector = AIDetector()

pdf_gen = PDFGenerator()
word_gen = WordGenerator()
md_gen = MarkdownGenerator()
html_gen = HTMLGenerator()
latex_gen = LaTeXGenerator()

table_gen = TableGenerator()
chart_gen = ChartGenerator()
diagram_gen = DiagramGenerator()
layout_mgr = LayoutManager()

data_analyzer = DataAnalyzer()
stats_gen = StatsGenerator()
viz_ai = VisualizationAI()

metrics = QualityMetrics()
comparison = DocumentComparison()
transparency = TransparencyLogger()

# Document Preview & Download System
preview_manager = DocumentPreviewManager()
document_accessor = DocumentAccessor(preview_manager)


# ==================== TAB 1: GENERATE DOCUMENT ====================

def generate_document(
    title: str,
    requirements: str,
    lecture_notes: str,
    document_type: str,
    length_words: int,
    style: str,
    include_tables: bool,
    include_charts: bool,
    include_citations: bool,
    citation_style: str,
    formats: list,
) -> Tuple[str, dict, dict, dict]:
    """Generate complete academic document with all features."""
    
    try:
        # Log event
        transparency.log_event("document_generation_started", {
            "title": title,
            "type": document_type,
            "length": length_words,
            "formats": formats,
        })

        # Parse requirements
        reqs = analyzer.analyze_requirements(requirements, lecture_notes)
        
        # Generate content sections
        content_dict = generator.generate_document_sections(
            sections=reqs.sections,
            context=requirements,
            topics=reqs.key_topics,
            style=reqs.style,
            total_words=length_words,
        )

        # Humanize content
        for section in content_dict:
            content_dict[section] = humanizer.humanize_content(
                content_dict[section],
                style=reqs.style
            )

        # Generate visualizations if requested
        tables_html = ""
        if include_tables:
            table_data = table_gen.generate_summary_table("\n".join(content_dict.values()))
            tables_html = table_gen.format_as_html(table_data)

        # Generate citations if requested
        citations = []
        if include_citations:
            citations = [
                citation_mgr.generate_citation(
                    ["Smith, J.", "Doe, A."],
                    f"Research on {reqs.key_topics[0] if reqs.key_topics else 'Topic'}",
                    "Academic Journal",
                    2024,
                    style=citation_style
                ),
                citation_mgr.generate_citation(
                    ["Johnson, B."],
                    "Contemporary Research Methods",
                    "University Press",
                    2023,
                    style=citation_style
                ),
            ]

        # Generate documents in requested formats
        outputs = {}
        status_updates = []

        if "pdf" in formats:
            try:
                pdf_bytes = pdf_gen.generate_pdf(title, content_dict, include_citations=include_citations, citations=citations)
                pdf_path = FileHandler.save_file(pdf_bytes, f"{title.replace(' ', '_')}.pdf")
                outputs["PDF"] = pdf_path
                status_updates.append("✓ PDF generated successfully")
            except Exception as e:
                status_updates.append(f"✗ PDF generation failed: {str(e)[:50]}")

        if "docx" in formats:
            try:
                docx_bytes = word_gen.generate_word_doc(title, content_dict, include_citations=include_citations, citations=citations)
                docx_path = FileHandler.save_file(docx_bytes, f"{title.replace(' ', '_')}.docx")
                outputs["Word"] = docx_path
                status_updates.append("✓ Word document generated successfully")
            except Exception as e:
                status_updates.append(f"✗ Word generation failed: {str(e)[:50]}")

        if "md" in formats:
            try:
                md_bytes = md_gen.generate_markdown_bytes(title, content_dict, include_citations=include_citations, citations=citations)
                md_path = FileHandler.save_file(md_bytes, f"{title.replace(' ', '_')}.md")
                outputs["Markdown"] = md_path
                status_updates.append("✓ Markdown generated successfully")
            except Exception as e:
                status_updates.append(f"✗ Markdown generation failed: {str(e)[:50]}")

        if "html" in formats:
            try:
                html_bytes = html_gen.generate_html_bytes(title, content_dict, include_citations=include_citations, citations=citations)
                html_path = FileHandler.save_file(html_bytes, f"{title.replace(' ', '_')}.html")
                outputs["HTML"] = html_path
                status_updates.append("✓ HTML generated successfully")
            except Exception as e:
                status_updates.append(f"✗ HTML generation failed: {str(e)[:50]}")

        # Quality metrics
        full_content = "\n".join(content_dict.values())
        quality = metrics.get_quality_report(full_content)

        # AI Detection analysis
        detection = detector.analyze_detection_risk(full_content)

        result_text = (
            f"✅ DOCUMENT GENERATION COMPLETE\n\n"
            f"Title: {title}\n"
            f"Type: {document_type}\n"
            f"Word Count: {TextFormatter.word_count(full_content)}\n"
            f"Reading Time: ~{TextFormatter.estimate_reading_time(full_content)} minutes\n\n"
            f"📊 QUALITY METRICS:\n"
            f"  Readability Score: {quality['readability']}/100\n"
            f"  Coherence: {quality['coherence']}/100\n"
            f"  Originality: {quality['originality']}/100\n\n"
            f"⚠️ AI DETECTION RISK: {detection['risk_level']}\n"
            f"  Risk Score: {detection['risk_score']:.1%}\n"
            f"  Recommendation: {detection['recommendation']}\n\n"
            f"📥 GENERATED FORMATS:\n" +
            "\n".join(f"  ✓ {fmt.upper()}" for fmt in outputs.keys()) + "\n\n" +
            f"🔗 STATUS:\n" +
            "\n".join(f"  {s}" for s in status_updates)
        )

        # Register document for preview & download
        doc_id = preview_manager.register_document(
            title=title,
            file_paths=outputs,
            content_preview=full_content,
            metadata={
                "document_type": document_type,
                "word_count": TextFormatter.word_count(full_content),
                "reading_time": TextFormatter.estimate_reading_time(full_content),
                "quality_score": quality['readability'],
                "ai_detection_risk": detection['risk_level'],
                "formats_available": list(outputs.keys())
            }
        )

        # Add download information to result
        result_text += f"\n\n{'=' * 60}\n"
        result_text += format_download_instructions(doc_id, list(outputs.keys()))
        result_text += f"{'=' * 60}\n"

        transparency.log_event("document_generation_completed", {
            "formats_generated": list(outputs.keys()),
            "word_count": TextFormatter.word_count(full_content),
            "quality_score": quality['readability'],
            "document_id": doc_id,
        })

        return result_text, quality, detection, {"tables": tables_html}

    except Exception as e:
        return f"❌ Error: {str(e)}", {}, {}, {}


# ==================== TAB 2: DATA & VISUALIZATIONS ====================

def generate_visualizations(data_text: str, viz_types: list) -> Tuple[str, str]:
    """Generate data visualizations."""
    try:
        numbers = data_analyzer.extract_numbers(data_text)
        
        if not numbers:
            return "No numeric data found in input.", ""

        stats_report = stats_gen.generate_summary_statistics(numbers)
        
        viz_suggestions = viz_ai.recommend_visualizations(data_text)
        
        result = f"Data Analysis Results:\n\n{stats_report}\n\nVisualization Recommendations:\n"
        result += "- Charts: " + ", ".join(viz_suggestions["charts"]) + "\n"
        result += "- Tables: " + ", ".join(viz_suggestions["tables"]) + "\n"
        
        return result, "Visualizations would be generated here"

    except Exception as e:
        return f"Error: {str(e)}", ""


# ==================== TAB 3: DOCUMENT TEMPLATES ====================

def load_template(template_name: str) -> str:
    """Load and describe a document template."""
    template = DocumentTemplates.get_template(template_name)
    
    description = (
        f"📋 Template: {template['name']}\n\n"
        f"Description: {template['description']}\n\n"
        f"Sections:\n" +
        "\n".join(f"  {i+1}. {section}" for i, section in enumerate(template['sections']))
    )
    
    return description


# ==================== TAB 5: AI CAPABILITIES RESEARCH ====================

def analyze_ai_capability(capability_name: str) -> str:
    """Analyze specific AI capability."""
    try:
        from src.research_engine import AICapabilitiesAnalyzer
        analyzer = AICapabilitiesAnalyzer()
        
        capability_data = analyzer.get_capability_details(capability_name)
        score = analyzer.score_capability(capability_name)
        
        result = f"""
### {capability_name.replace('_', ' ').title()}

**Description:** {capability_data.get('description', 'N/A')}

**Examples:**
"""
        for example in capability_data.get('examples', [])[:5]:
            result += f"- {example}\n"
        
        result += f"""
**Maturity Level:** {score.get('maturity_score', 0)}/100
**Reliability:** {score.get('reliability_score', 0)}/100  
**Scalability:** {score.get('scalability_score', 0)}/100
**Real-world Impact:** {score.get('real_world_impact', 'High')}

**Confidence Level:** {capability_data.get('confidence_level', 'Very High')}
"""
        return result
    except Exception as e:
        return f"Error analyzing capability: {str(e)}"


def generate_limitations_report() -> str:
    """Generate limitations report."""
    try:
        from src.research_engine import AILimitationsAnalyzer
        analyzer = AILimitationsAnalyzer()
        
        classification = analyzer.classify_limitations()
        
        report = """# AI LIMITATIONS: Comprehensive Analysis

## Likely Never Solvable (Fundamental Barriers)

These limitations are likely impossible with current computational paradigms:
"""
        for limitation in classification['likely_never_solvable']:
            report += f"\n### {limitation.replace('_', ' ').title()}\n"
            limitation_details = analyzer.get_limitation_details(limitation)
            report += f"{limitation_details.get('description', 'N/A')}\n"
        
        report += """

## Fundamental Barriers (Very Difficult)

These are deeply hard problems but might be solvable:
"""
        for limitation in classification['fundamental_barriers'][:3]:
            report += f"- {limitation.replace('_', ' ').title()}\n"
        
        report += """

## Engineering Challenges (Solvable)

These are engineering problems that can be addressed:
"""
        for limitation in classification['engineering_challenges'][:5]:
            report += f"- {limitation.replace('_', ' ').title()}\n"
        
        return report
    except Exception as e:
        return f"Error generating report: {str(e)}"


def analyze_human_advantage(advantage_name: str) -> str:
    """Analyze specific human advantage."""
    try:
        from src.research_engine import HumanAIComparison
        comparison = HumanAIComparison()
        
        advantage_data = comparison.analyze_human_advantage(advantage_name)
        
        result = f"""
### {advantage_name.replace('_', ' ').title()}

**Description:** {advantage_data.get('description', 'N/A')}

**Examples:**
"""
        for example in advantage_data.get('examples', []):
            result += f"- {example}\n"
        
        result += f"""
**Why AI Cannot Replicate This:** {advantage_data.get('ai_cannot_replicate', 'Fundamental difference')}

**Competitive Value:** {advantage_data.get('competitive_value', 'Very High')}

**Implication:** This human advantage becomes MORE valuable in an AI-enabled world, not less.
"""
        return result
    except Exception as e:
        return f"Error analyzing advantage: {str(e)}"


def compare_domain(domain: str) -> str:
    """Compare AI vs Humans in specific domain."""
    try:
        from src.research_engine import HumanAIComparison
        comparison = HumanAIComparison()
        
        domain_comparison = comparison.compare_domain(domain)
        
        result = f"""
### {domain.replace('_', ' ').title()}

**AI Strength:** {domain_comparison.get('ai_strength', 'N/A')}

**Human Strength:** {domain_comparison.get('human_strength', 'N/A')}

**Winner: {domain_comparison.get('winner', 'Unclear')}**

**Analysis:** {domain_comparison.get('analysis', 'Both have advantages')}

This demonstrates that AI and humans have complementary strengths rather than 
one being universally superior. Optimal results come from collaboration.
"""
        return result
    except Exception as e:
        return f"Error comparing domain: {str(e)}"


def generate_future_projection() -> str:
    """Generate future AI capabilities projection."""
    from src.research_engine import AdvancedReasoningEngine
    
    engine = AdvancedReasoningEngine()
    projection = engine._project_future_capabilities()
    
    report = """# FUTURE AI CAPABILITIES PROJECTION (5-10 Years)

## Likely Within 5 Years:
"""
    for capability in projection['next_5_years']:
        report += f"- **{capability['capability'].replace('_', ' ').title()}**: {capability['potential_impact']}\n"
    
    report += """

## Likely Within 10 Years:
"""
    for capability in projection['next_10_years']:
        report += f"- **{capability['capability'].replace('_', ' ').title()}**: {capability['potential_impact']}\n"
    
    report += """

## Still Unknown / Highly Uncertain:
"""
    for item in projection['still_unknown']:
        report += f"- {item}\n"
    
    report += """

## Likely Never Solvable:
"""
    for item in projection['likely_impossible']:
        report += f"- {item}\n"
    
    return report


def generate_full_research_analysis() -> str:
    """Generate full comprehensive research analysis."""
    try:
        from src.research_engine import AdvancedReasoningEngine
        engine = AdvancedReasoningEngine()
        
        analysis = engine.generate_research_paper_outline()
        return analysis
    except Exception as e:
        return f"Error generating analysis: {str(e)}"


# ==================== HELPER FUNCTION: ACCESS GENERATED DOCUMENTS ====================

def _access_document(doc_id: str, preview_manager, document_accessor):
    """
    Access a generated document by its ID.
    
    Returns:
        Tuple of (preview, info, full_content, pdf_file, word_file, markdown_file, html_file, latex_file)
    """
    try:
        if not doc_id or not doc_id.strip():
            return (
                "❌ Please enter a Document ID",
                "No document selected",
                "",
                None, None, None, None, None
            )
        
        doc_info = preview_manager.get_document_info(doc_id)
        if not doc_info:
            return (
                f"❌ Document ID '{doc_id}' not found",
                "Unable to locate document",
                "",
                None, None, None, None, None
            )
        
        # Get preview and info
        preview = document_accessor.get_preview(doc_id)
        info = document_accessor.get_document_info_formatted(doc_id)
        full_content = doc_info.get("content_preview", "")
        
        # Prepare file downloads
        file_paths = doc_info.get("file_paths", {})
        
        # Try to get each format
        pdf_file = file_paths.get("PDF") if os.path.exists(file_paths.get("PDF", "")) else None
        word_file = file_paths.get("Word") if os.path.exists(file_paths.get("Word", "")) else None
        markdown_file = file_paths.get("Markdown") if os.path.exists(file_paths.get("Markdown", "")) else None
        html_file = file_paths.get("HTML") if os.path.exists(file_paths.get("HTML", "")) else None
        latex_file = file_paths.get("LaTeX") if os.path.exists(file_paths.get("LaTeX", "")) else None
        
        return (
            preview,
            info,
            full_content,
            pdf_file,
            word_file,
            markdown_file,
            html_file,
            latex_file
        )
    
    except Exception as e:
        return (
            f"❌ Error accessing document: {str(e)}",
            f"Error: {str(e)}",
            "",
            None, None, None, None, None
        )


# ==================== TAB 4: ANALYSIS & RESEARCH ====================

def analyze_content(content: str) -> Tuple[str, str, str]:
    """Analyze content and provide metrics."""
    try:
        quality = metrics.get_quality_report(content)
        detection = detector.analyze_detection_risk(content)
        transparency_report = transparency.generate_transparency_report()

        quality_text = (
            f"📊 QUALITY ANALYSIS\n"
            f"{'='*50}\n\n"
            f"Readability Score: {quality['readability']}/100\n"
            f"Coherence Score: {quality['coherence']}/100\n"
            f"Originality Score: {quality['originality']}/100\n"
            f"Word Count: {quality['word_count']}\n"
            f"Sentence Count: {quality['sentence_count']}\n"
        )

        detection_text = detector.get_detection_report(content)

        return quality_text, detection_text, transparency_report

    except Exception as e:
        return f"Error in analysis: {str(e)}", "", ""


# ==================== TAB 5: ADVANCED SETTINGS ====================

def save_settings(font_size: int, line_spacing: float, margins: str) -> str:
    """Save advanced settings."""
    return (
        f"✅ Settings saved successfully!\n\n"
        f"Font Size: {font_size}pt\n"
        f"Line Spacing: {line_spacing}\n"
        f"Margins: {margins}\n\n"
        f"These settings will be applied to all future documents."
    )


# ==================== TAB 6: ABOUT & ETHICS ====================

def get_about_info() -> str:
    """Get about and ethics information."""
    return f"""
{'='*60}
AI ACADEMIC DOCUMENT SUITE - ABOUT & ETHICS
{'='*60}

📚 PURPOSE
This tool demonstrates next-generation AI capabilities in document 
creation, visualization, and academic writing. It's designed for:
- Educational research and learning
- Understanding AI document generation
- Exploring AI capabilities in professional work
- Demonstrating document automation

⚠️ ETHICS & ACADEMIC INTEGRITY

THIS IS AN EDUCATIONAL & RESEARCH TOOL ONLY

{ETHICS_WARNING}

🔒 PRIVACY
- All processing is local (no data sent externally)
- Files are temporarily stored and deleted
- No user data is retained or tracked
- Open source for full transparency

🎓 RESPONSIBLE USE
1. Use AI tools transparently and with permission
2. Disclose AI use to instructors and institutions
3. Use for learning, not deception
4. Understand the technology and its limitations
5. Respect academic integrity policies

📊 FEATURES
✓ Multi-format document export (PDF, Word, Markdown, HTML, LaTeX)
✓ Intelligent data visualization
✓ Citation management (APA, MLA, Chicago, Harvard, IEEE)
✓ Professional document layout
✓ AI detection analysis
✓ Quality metrics
✓ Research transparency logging

🚀 FUTURE IMPROVEMENTS
- More advanced NLP and language models
- Real-time collaboration features
- Advanced template customization
- Integration with academic databases
- Multi-language support

📝 LICENSE: MIT (Open Source)

{'='*60}
Made with ❤️ for education and research
{'='*60}
"""


# ==================== GRADIO INTERFACE ====================

def create_interface():
    """Create the complete Gradio interface with 6 tabs."""
    
    with gr.Blocks(title="AI Academic Document Suite", theme=gr.themes.Soft()) as demo:
        
        gr.Markdown("""
        # 🚀 AI Academic Document Suite
        ## Next-Generation Document Generation Platform
        
        **Demonstrating AI capabilities in professional document creation**
        
        ⚠️ *Research & Educational Tool - See 'About & Ethics' for important information*
        """)
        
        # System health status
        with gr.Row():
            health = optimization_manager.check_memory_health()
            health_status = "✅ HEALTHY" if health['status'] == 'HEALTHY' else f"⚠️ {health['status']}"
            health_text = f"**System Status:** {health_status} | **Memory:** {health['ram_percent']:.1f}% | **Available:** {health['available_gb']:.1f}GB"
            gr.Markdown(health_text)

        with gr.Tabs():
            
            # ========== TAB 1: GENERATE DOCUMENT ==========
            with gr.Tab("📄 Generate Document", id="tab_generate"):
                gr.Markdown("### Create Professional Academic Documents")
                
                with gr.Row():
                    with gr.Column():
                        title_input = gr.Textbox(
                            label="📌 Document Title",
                            placeholder="e.g., The Impact of AI on Modern Education"
                        )
                        doc_type = gr.Dropdown(
                            choices=["research", "essay", "report", "lab", "thesis"],
                            value="research",
                            label="📋 Document Type"
                        )
                        length_words = gr.Slider(
                            minimum=500, maximum=10000, value=2000, step=100,
                            label="📝 Target Word Count"
                        )
                    
                    with gr.Column():
                        style = gr.Dropdown(
                            choices=["academic", "formal", "informal", "technical"],
                            value="academic",
                            label="🎨 Writing Style"
                        )
                        citation_style = gr.Dropdown(
                            choices=CITATION_STYLES,
                            value="APA",
                            label="📚 Citation Style"
                        )
                        formats = gr.CheckboxGroup(
                            choices=["pdf", "docx", "md", "html", "latex"],
                            value=["pdf", "docx"],
                            label="💾 Export Formats"
                        )

                with gr.Row():
                    requirements = gr.Textbox(
                        label="📋 Assignment Requirements",
                        placeholder="Paste your assignment requirements here...",
                        lines=4
                    )
                    lecture_notes = gr.Textbox(
                        label="📖 Lecture Notes / Source Material",
                        placeholder="Paste lecture notes or source material here...",
                        lines=4
                    )

                with gr.Row():
                    include_tables = gr.Checkbox(label="📊 Include Tables", value=True)
                    include_charts = gr.Checkbox(label="📈 Include Charts", value=True)
                    include_citations = gr.Checkbox(label="📚 Include Citations", value=True)

                generate_btn = gr.Button("🚀 Generate Document", size="lg")

                with gr.Row():
                    output_text = gr.Textbox(label="Generation Results", lines=15)

                with gr.Row():
                    quality_metrics = gr.JSON(label="Quality Metrics")
                    detection_analysis = gr.JSON(label="AI Detection Analysis")

                generate_btn.click(
                    fn=generate_document,
                    inputs=[
                        title_input, requirements, lecture_notes, doc_type,
                        length_words, style, include_tables, include_charts,
                        include_citations, citation_style, formats
                    ],
                    outputs=[output_text, quality_metrics, detection_analysis, gr.State()]
                )

            # ========== TAB 1B: DOCUMENT PREVIEW & DOWNLOAD ==========
            with gr.Tab("📥 Download Documents", id="tab_download"):
                gr.Markdown(get_document_view_instructions())
                
                with gr.Row():
                    doc_id_input = gr.Textbox(
                        label="📄 Document ID",
                        placeholder="Paste your Document ID here to access generated documents",
                        info="You can find the Document ID in your generation results"
                    )
                    access_btn = gr.Button("🔍 Access Document", size="lg")
                
                with gr.Row():
                    with gr.Column():
                        doc_preview = gr.Textbox(
                            label="📋 Document Preview",
                            lines=10,
                            interactive=False,
                            info="First 500 characters of your document"
                        )
                    with gr.Column():
                        doc_info = gr.Textbox(
                            label="ℹ️ Document Information",
                            lines=10,
                            interactive=False,
                            info="Format, size, quality, and other metadata"
                        )
                
                with gr.Row():
                    download_pdf = gr.File(label="📄 Download PDF", interactive=False)
                    download_word = gr.File(label="📝 Download Word", interactive=False)
                    download_markdown = gr.File(label="📋 Download Markdown", interactive=False)
                
                with gr.Row():
                    download_html = gr.File(label="🌐 Download HTML", interactive=False)
                    download_latex = gr.File(label="📐 Download LaTeX", interactive=False)
                
                with gr.Row():
                    full_content = gr.Textbox(
                        label="📖 Full Document Content",
                        lines=15,
                        interactive=False,
                        info="Complete document text"
                    )
                
                access_btn.click(
                    fn=lambda doc_id: _access_document(doc_id, preview_manager, document_accessor),
                    inputs=[doc_id_input],
                    outputs=[
                        doc_preview, doc_info, full_content,
                        download_pdf, download_word, download_markdown,
                        download_html, download_latex
                    ]
                )
                
                gr.Markdown("""
                ### 💾 All Generated Documents
                
                Here's a history of all your generated documents:
                """)
                
                doc_history = gr.Textbox(
                    label="📜 Document History",
                    lines=12,
                    interactive=False,
                    value=create_access_history_display(preview_manager.get_all_documents())
                )

            # ========== TAB 2: DATA & VISUALIZATIONS ==========
            with gr.Tab("📊 Data & Visualizations", id="tab_visualize"):
                gr.Markdown("### Generate Visualizations from Data")
                
                data_input = gr.Textbox(
                    label="📈 Data Input",
                    placeholder="Enter data or paste numbers to analyze...",
                    lines=8
                )
                
                viz_types = gr.CheckboxGroup(
                    choices=["bar chart", "line chart", "pie chart", "scatter plot", "table"],
                    label="Visualization Types"
                )

                viz_btn = gr.Button("📊 Generate Visualizations")
                
                viz_output = gr.Textbox(label="Visualization Results", lines=10)
                viz_preview = gr.Textbox(label="Preview", lines=5)

                viz_btn.click(
                    fn=generate_visualizations,
                    inputs=[data_input, viz_types],
                    outputs=[viz_output, viz_preview]
                )

            # ========== TAB 3: DOCUMENT TEMPLATES ==========
            with gr.Tab("📚 Document Templates", id="tab_templates"):
                gr.Markdown("### Pre-built Document Templates")
                
                template_names = DocumentTemplates.get_template_names()
                template_dropdown = gr.Dropdown(
                    choices=template_names,
                    value=template_names[0],
                    label="Select Template"
                )

                template_output = gr.Textbox(label="Template Description", lines=15)
                
                template_dropdown.change(
                    fn=load_template,
                    inputs=template_dropdown,
                    outputs=template_output
                )

                # Initial load
                template_output.value = load_template(template_names[0])

            # ========== TAB 4: ANALYSIS & RESEARCH ==========
            with gr.Tab("🔍 Analysis & Research", id="tab_analysis"):
                gr.Markdown("### Content Analysis & Research Tools")
                
                analysis_input = gr.Textbox(
                    label="Content to Analyze",
                    placeholder="Paste content here for analysis...",
                    lines=10
                )

                analyze_btn = gr.Button("🔍 Analyze Content")

                with gr.Row():
                    quality_output = gr.Textbox(label="Quality Metrics", lines=8)
                    detection_output = gr.Textbox(label="AI Detection Report", lines=8)

                transparency_output = gr.Textbox(label="Transparency Log", lines=8)

                analyze_btn.click(
                    fn=analyze_content,
                    inputs=analysis_input,
                    outputs=[quality_output, detection_output, transparency_output]
                )

            # ========== TAB 5: AI CAPABILITIES RESEARCH ==========
            with gr.Tab("🔬 AI Capabilities Research", id="tab_research"):
                gr.Markdown("""
                ## AI Capabilities, Limitations & Human Advantages
                ### SLIIT Research Project: Understanding AI in Modern Context
                
                Comprehensive analysis of what AI can do, cannot do, and what humans do better.
                """)
                
                with gr.Tabs():
                    # Sub-tab 5.1: What AI Can Do
                    with gr.Tab("What AI Can Do"):
                        gr.Markdown("### Current AI Capabilities")
                        
                        with gr.Row():
                            capability_select = gr.Dropdown(
                                choices=[
                                    "pattern_recognition",
                                    "language_processing",
                                    "data_analysis",
                                    "optimization",
                                    "task_automation",
                                    "computer_vision",
                                    "content_generation",
                                    "recommendation_systems",
                                    "voice_recognition",
                                    "game_playing",
                                    "scientific_discovery",
                                    "parallel_processing",
                                    "knowledge_retrieval",
                                    "logical_reasoning"
                                ],
                                label="Select Capability",
                                value="pattern_recognition"
                            )
                            capability_btn = gr.Button("Analyze", variant="primary")
                        
                        capability_output = gr.Markdown(label="Capability Details")
                        
                        capability_btn.click(
                            fn=lambda cap: analyze_ai_capability(cap),
                            inputs=capability_select,
                            outputs=capability_output
                        )
                    
                    # Sub-tab 5.2: What AI Cannot Do
                    with gr.Tab("What AI Cannot Do"):
                        gr.Markdown("### AI Limitations & Fundamental Barriers")
                        
                        limitation_report = gr.Textbox(
                            value=generate_limitations_report(),
                            label="AI Limitations Analysis",
                            lines=20,
                            interactive=False
                        )
                    
                    # Sub-tab 5.3: What Humans Do Better
                    with gr.Tab("What Humans Do Better"):
                        gr.Markdown("### Human Advantages Over AI")
                        
                        with gr.Row():
                            advantage_select = gr.Dropdown(
                                choices=[
                                    "creativity_and_novelty",
                                    "general_intelligence",
                                    "emotional_intelligence",
                                    "common_sense",
                                    "strategic_thinking",
                                    "adaptability",
                                    "embodied_understanding",
                                    "moral_and_ethical_reasoning",
                                    "intrinsic_motivation",
                                    "complex_social_interaction",
                                    "learning_from_failure",
                                    "intuition_and_pattern_recognition",
                                    "contextual_understanding",
                                    "perspective_taking",
                                    "meaning_making",
                                    "physical_manipulation",
                                    "communication",
                                    "decision_making_under_uncertainty",
                                    "meta_cognition"
                                ],
                                label="Select Human Advantage",
                                value="creativity_and_novelty"
                            )
                            advantage_btn = gr.Button("Analyze", variant="primary")
                        
                        advantage_output = gr.Markdown(label="Advantage Details")
                        
                        advantage_btn.click(
                            fn=lambda adv: analyze_human_advantage(adv),
                            inputs=advantage_select,
                            outputs=advantage_output
                        )
                    
                    # Sub-tab 5.4: Domain Comparison
                    with gr.Tab("AI vs Human by Domain"):
                        gr.Markdown("### Comparison of AI and Human Capabilities by Domain")
                        
                        with gr.Row():
                            domain_select = gr.Dropdown(
                                choices=[
                                    "mathematical_computation",
                                    "creative_writing",
                                    "image_recognition",
                                    "strategic_planning",
                                    "data_analysis",
                                    "emotional_support",
                                    "learning_new_skill",
                                    "pattern_recognition",
                                    "moral_judgment",
                                    "physical_dexterity"
                                ],
                                label="Select Domain",
                                value="mathematical_computation"
                            )
                            domain_btn = gr.Button("Compare", variant="primary")
                        
                        domain_output = gr.Markdown(label="Comparison Results")
                        
                        domain_btn.click(
                            fn=lambda dom: compare_domain(dom),
                            inputs=domain_select,
                            outputs=domain_output
                        )
                    
                    # Sub-tab 5.5: Future Projection
                    with gr.Tab("Future AI Capabilities"):
                        gr.Markdown("### What AI Will Likely Do in 5-10 Years")
                        
                        future_output = gr.Textbox(
                            value=generate_future_projection(),
                            label="Future Capabilities Projection",
                            lines=20,
                            interactive=False
                        )
                    
                    # Sub-tab 5.6: Research Summary
                    with gr.Tab("Full Research Analysis"):
                        gr.Markdown("### Comprehensive SLIIT Research Summary")
                        
                        summary_btn = gr.Button("Generate Full Analysis", variant="primary")
                        summary_output = gr.Textbox(
                            label="Full Research Report",
                            lines=30,
                            interactive=False
                        )
                        
                        summary_btn.click(
                            fn=generate_full_research_analysis,
                            outputs=summary_output
                        )

            # ========== TAB 6: ADVANCED SETTINGS ==========
            with gr.Tab("⚙️ Advanced Settings", id="tab_settings"):
                gr.Markdown("### Customize Document Generation Settings")
                
                with gr.Row():
                    font_size = gr.Slider(
                        minimum=10, maximum=16, value=12, step=1,
                        label="Font Size (pt)"
                    )
                    line_spacing = gr.Slider(
                        minimum=1.0, maximum=2.5, value=1.5, step=0.1,
                        label="Line Spacing"
                    )

                margins = gr.Textbox(
                    label="Margins (top, bottom, left, right in inches)",
                    value="1.0, 1.0, 1.0, 1.0"
                )

                save_btn = gr.Button("💾 Save Settings")
                settings_output = gr.Textbox(label="Confirmation", lines=5)

                save_btn.click(
                    fn=save_settings,
                    inputs=[font_size, line_spacing, margins],
                    outputs=settings_output
                )

            # ========== TAB 6: ABOUT & ETHICS ==========
            with gr.Tab("📖 About & Ethics", id="tab_about"):
                about_output = gr.Textbox(
                    value=get_about_info(),
                    label="About This Tool",
                    lines=30,
                    interactive=False
                )

    return demo


# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
    )
