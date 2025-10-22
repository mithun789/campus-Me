"""
Material Upload UI Integration - Functions for Gradio interface
Handles material upload, analysis, and content generation
"""

from typing import List, Tuple, Optional, Dict, Any
import json
import logging

logger = logging.getLogger(__name__)


def analyze_uploaded_materials(files: List[Any]) -> Tuple[str, str, str, str, str, str, str, str]:
    """
    Analyze uploaded lecture materials.
    
    Args:
        files: List of uploaded file objects from Gradio
        
    Returns:
        Tuple of (concepts, objectives, definitions, structure, themes, difficulty, summary, focus_areas)
    """
    if not files:
        return ("No files uploaded", "", "", "", "", "", "", "")

    try:
        from src.ai_engine import MaterialAnalyzer, MaterialProcessor, FileManager
        
        # Initialize
        processor = MaterialProcessor()
        file_manager = FileManager()
        
        all_analyses = []
        error_messages = []
        
        # Process each file
        for file_obj in files:
            try:
                # Upload to manager
                success, result = file_manager.upload_file(str(file_obj.name) if hasattr(file_obj, 'name') else file_obj)
                
                if success:
                    file_id = result
                    # Get file path
                    file_path = file_manager.get_file_path(file_id)
                    
                    if file_path:
                        # Process and analyze
                        analysis, content = processor.process_material(file_path)
                        all_analyses.append(analysis)
                        
                        # Mark for cleanup (delete in 30 seconds)
                        file_manager.mark_processed(file_id, delete_after=30)
                else:
                    error_messages.append(f"Error uploading: {result}")
            
            except Exception as e:
                error_messages.append(f"Error processing file: {str(e)[:100]}")
                logger.error(f"Material processing error: {str(e)}")
                continue
        
        if not all_analyses:
            return (
                "❌ " + " | ".join(error_messages),
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            )
        
        # If multiple materials, combine analysis (use first one for simplicity, or combine)
        combined = all_analyses[0]
        
        if len(all_analyses) > 1:
            combined = combine_multiple_analyses(all_analyses)
        
        # Format outputs for display
        concepts_str = format_concepts(combined.get("key_concepts", []))
        objectives_str = format_objectives(combined.get("learning_objectives", []))
        definitions_str = format_definitions(combined.get("key_definitions", []))
        structure_str = format_structure(combined.get("structure", {}))
        themes_str = format_themes(combined.get("main_themes", []))
        difficulty_str = combined.get("difficulty_level", "Unknown")
        summary_str = combined.get("summary", "No summary available")
        focus_str = format_focus_areas(combined.get("focus_areas", []))
        
        return (
            concepts_str,
            objectives_str,
            definitions_str,
            structure_str,
            themes_str,
            difficulty_str,
            summary_str,
            focus_str
        )
    
    except Exception as e:
        logger.error(f"Material analysis error: {str(e)}")
        return (
            f"❌ Analysis error: {str(e)[:200]}",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        )


def generate_from_material_analysis(
    concepts: str,
    objectives: str,
    definitions: str,
    document_type: str,
    output_formats: List[str],
    content_generator
) -> str:
    """
    Generate documents based on material analysis.
    
    Args:
        concepts: Extracted concepts
        objectives: Learning objectives
        definitions: Key definitions
        document_type: Type of document to generate
        output_formats: List of output formats
        content_generator: ContentGenerator instance
        
    Returns:
        Status message
    """
    try:
        from utils import FileHandler
        
        # Parse extracted information
        status_messages = []
        
        # Build prompt from analysis
        prompt = build_prompt_from_analysis(
            concepts, objectives, definitions, document_type
        )
        
        # Generate content using content_generator
        generated_content = content_generator.generate_section(
            title=f"{document_type} - Study Material",
            context=concepts + "\n" + objectives,
            topic=document_type,
            word_count=1000,
            style="academic"
        )
        
        status_messages.append(f"✓ Generated content ({len(generated_content)} chars)")
        
        # Could generate multiple formats here if needed
        if "pdf" in output_formats or "docx" in output_formats:
            status_messages.append("✓ Ready for export to PDF/Word")
        
        return "\n".join(status_messages)
    
    except Exception as e:
        logger.error(f"Document generation error: {str(e)}")
        return f"❌ Generation error: {str(e)[:200]}"


def format_concepts(concepts: List[Dict[str, Any]]) -> str:
    """Format concepts for display."""
    if not concepts:
        return "No concepts extracted"
    
    lines = ["**Key Concepts Extracted:**\n"]
    for i, concept in enumerate(concepts[:15], 1):
        importance = concept.get("importance", 0)
        concept_name = concept.get("concept", "Unknown")
        bar = "█" * (importance // 10) + "░" * (10 - importance // 10)
        lines.append(f"{i}. **{concept_name}** [{bar}] {importance}%")
    
    return "\n".join(lines)


def format_objectives(objectives: List[str]) -> str:
    """Format learning objectives for display."""
    if not objectives:
        return "No learning objectives found"
    
    lines = ["**Learning Objectives:**\n"]
    for i, obj in enumerate(objectives, 1):
        lines.append(f"{i}. {obj}")
    
    return "\n".join(lines)


def format_definitions(definitions: List[Dict[str, str]]) -> str:
    """Format definitions for display."""
    if not definitions:
        return "No definitions extracted"
    
    lines = ["**Key Definitions:**\n"]
    for i, d in enumerate(definitions[:10], 1):
        term = d.get("term", "Unknown")
        definition = d.get("definition", "")[:150] + ("..." if len(d.get("definition", "")) > 150 else "")
        lines.append(f"**{i}. {term}:** {definition}")
    
    return "\n".join(lines)


def format_structure(structure: Dict[str, Any]) -> str:
    """Format document structure for display."""
    if not structure:
        return "No structure information"
    
    lines = [
        f"**Document Structure Analysis:**",
        f"- Total Lines: {structure.get('total_lines', 0)}",
        f"- Paragraphs: {structure.get('total_paragraphs', 0)}",
        f"- Sections: {structure.get('estimated_sections', 0)}",
        f"- Avg Paragraph Length: {structure.get('average_paragraph_length', 0)} chars",
        f"- Has Lists: {'Yes' if structure.get('has_lists') else 'No'}",
        f"- Has Numbering: {'Yes' if structure.get('has_numbering') else 'No'}",
    ]
    
    return "\n".join(lines)


def format_themes(themes: List[Dict[str, Any]]) -> str:
    """Format main themes for display."""
    if not themes:
        return "No themes identified"
    
    lines = ["**Main Themes:**\n"]
    for i, theme in enumerate(themes[:10], 1):
        theme_name = theme.get("theme", "Unknown")
        importance = theme.get("importance", 0)
        mentions = theme.get("mentions", 0)
        lines.append(f"{i}. **{theme_name}** - Mentions: {mentions}, Importance: {importance}%")
    
    return "\n".join(lines)


def format_focus_areas(focus_areas: List[str]) -> str:
    """Format focus areas for display."""
    if not focus_areas:
        return "No focus areas identified"
    
    lines = ["**Suggested Focus Areas:**\n"]
    for i, area in enumerate(focus_areas[:5], 1):
        lines.append(f"{i}. {area}")
    
    return "\n".join(lines)


def build_prompt_from_analysis(
    concepts: str,
    objectives: str,
    definitions: str,
    document_type: str
) -> str:
    """Build a generation prompt from extracted material analysis."""
    prompt = f"""
Based on the following extracted material analysis, generate a {document_type}:

Key Concepts:
{concepts}

Learning Objectives:
{objectives}

Key Definitions:
{definitions}

Task: Create a comprehensive {document_type} that covers all the above material, 
organized by learning objectives, with clear explanations of each concept and definition.

Ensure the output is:
- Well-structured and easy to understand
- Academic in tone
- Comprehensive but concise
- Includes all key concepts and definitions
    """
    return prompt


def combine_multiple_analyses(analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Combine multiple material analyses into one comprehensive analysis.
    
    Args:
        analyses: List of individual material analyses
        
    Returns:
        Combined analysis
    """
    if not analyses:
        return {}
    
    if len(analyses) == 1:
        return analyses[0]
    
    # Combine concepts (remove duplicates, keep highest importance)
    all_concepts = {}
    for analysis in analyses:
        for concept in analysis.get("key_concepts", []):
            concept_name = concept.get("concept", "Unknown").lower()
            if concept_name not in all_concepts:
                all_concepts[concept_name] = concept
            else:
                # Keep the one with higher importance
                if concept.get("importance", 0) > all_concepts[concept_name].get("importance", 0):
                    all_concepts[concept_name] = concept
    
    # Combine objectives
    all_objectives = []
    seen_objectives = set()
    for analysis in analyses:
        for obj in analysis.get("learning_objectives", []):
            if obj not in seen_objectives:
                all_objectives.append(obj)
                seen_objectives.add(obj)
    
    # Combine definitions
    all_definitions = []
    seen_terms = set()
    for analysis in analyses:
        for definition in analysis.get("key_definitions", []):
            term = definition.get("term", "").lower()
            if term not in seen_terms:
                all_definitions.append(definition)
                seen_terms.add(term)
    
    # Use first analysis as base, then override with combined data
    combined = analyses[0].copy()
    combined["key_concepts"] = list(all_concepts.values())[:20]
    combined["learning_objectives"] = all_objectives
    combined["key_definitions"] = all_definitions
    combined["material_count"] = len(analyses)
    
    return combined


def get_material_upload_instructions() -> str:
    """Get instructions for material upload tab."""
    return """
### 📚 Upload & Analyze Lecture Materials

This tool allows you to upload your lecture materials (PDFs, Word documents, PowerPoint slides, etc.) 
and automatically extract:

- **Key Concepts** - Important topics and terms with importance scores
- **Learning Objectives** - What you're expected to learn
- **Key Definitions** - Important terms and their definitions  
- **Document Structure** - How the material is organized
- **Main Themes** - Primary topics and their relationships
- **Difficulty Level** - Whether this is beginner, intermediate, or advanced material
- **Focus Areas** - Where you should concentrate your study efforts

#### Supported File Formats:
- 📄 PDF files (.pdf)
- 📊 PowerPoint presentations (.pptx, .ppt)
- 📝 Word documents (.docx, .doc)
- 📋 Text files (.txt)
- 🖊️ Markdown files (.md)

#### How to Use:
1. Click "Upload Lecture Materials" and select one or more files
2. Click "Analyze Materials" to extract insights
3. Review the analysis results
4. Use "Generate Documents Based on Analysis" to create study materials
5. Files are automatically deleted after processing (privacy protected)

#### Privacy Note:
- Files are processed temporarily and automatically deleted
- No data is stored permanently
- Analysis happens locally without external storage
"""
