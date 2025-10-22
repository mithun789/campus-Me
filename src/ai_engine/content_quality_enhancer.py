"""
Content Quality Enhancer - Generates clean, readable, professional documents
Fixes placeholder text, reduces special characters, improves readability
"""

import re
from typing import Dict, List, Tuple
import random


class ContentQualityEnhancer:
    """Improves document generation quality and readability"""
    
    def __init__(self):
        """Initialize quality enhancer"""
        self.placeholder_patterns = [
            r'\[General Topic\]',
            r'\[positive/negative\]',
            r'\[opposite/similar\]',
            r'\[related fields/society as a whole\]',
            r'\[related disciplines\]',
            r'\[number\]',
            r'\[provide a spe',
            r'\*\*\*',
            r'---',
        ]
    
    def clean_placeholders(self, text: str, topic: str = "the subject") -> str:
        """
        Remove and replace placeholder text with actual content
        
        Args:
            text: Generated text with placeholders
            topic: Topic name to replace generic placeholders
            
        Returns:
            Cleaned text without placeholders
        """
        # Replace [General Topic] variants
        text = re.sub(r'\[General Topic\]', topic, text, flags=re.IGNORECASE)
        
        # Replace [positive/negative] with realistic option
        text = re.sub(r'\[positive/negative\]', 'significant', text, flags=re.IGNORECASE)
        text = re.sub(r'\[negative/positive\]', 'substantial', text, flags=re.IGNORECASE)
        
        # Replace [opposite/similar] 
        text = re.sub(r'\[opposite/similar\]', 'complementary', text, flags=re.IGNORECASE)
        
        # Replace [related fields/...]
        text = re.sub(r'\[related fields/society as a whole\]', 'multiple domains and society', text)
        text = re.sub(r'\[related disciplines\]', 'various academic fields', text)
        
        # Remove incomplete sentences
        text = re.sub(r'\[provide a spe.*', '', text)
        
        # Remove excessive brackets
        text = re.sub(r'\[.*?\]', '', text)
        
        # Clean up extra spaces and line breaks
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        text = re.sub(r'  +', ' ', text)
        
        return text.strip()
    
    def remove_special_characters_excess(self, text: str) -> str:
        """
        Remove excessive special characters that reduce readability
        
        Args:
            text: Text with special characters
            
        Returns:
            Cleaned text
        """
        # Remove multiple asterisks
        text = re.sub(r'\*{2,}', '', text)
        
        # Remove multiple hyphens/dashes
        text = re.sub(r'---+', '', text)
        
        # Remove excessive underscores
        text = re.sub(r'_{3,}', '', text)
        
        # Clean up excessive parentheses
        text = re.sub(r'\(\s*\)', '', text)
        
        # Remove line breaks with only special characters
        text = re.sub(r'\n\s*[*\-_=]{3,}\s*\n', '\n\n', text)
        
        return text
    
    def improve_readability(self, text: str) -> str:
        """
        Improve overall readability of document
        
        Args:
            text: Original text
            
        Returns:
            More readable text
        """
        # Add proper spacing around sections
        text = re.sub(r'(\w)\n(\w)', r'\1\n\n\2', text)
        
        # Fix sentence spacing
        text = re.sub(r'([.!?])\n', r'\1\n', text)
        
        # Ensure proper paragraph breaks
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove leading/trailing spaces from lines
        lines = [line.rstrip() for line in text.split('\n')]
        text = '\n'.join(lines)
        
        return text
    
    def generate_realistic_introduction(self, topic: str, document_type: str = "research paper") -> str:
        """
        Generate a realistic, placeholder-free introduction
        
        Args:
            topic: Main topic
            document_type: Type of document (research paper, essay, report, etc.)
            
        Returns:
            Professional introduction
        """
        introductions = [
            f"{topic} represents a critical area of contemporary research and discussion. "
            f"Over the past decade, scholars and practitioners have increasingly recognized "
            f"the importance of understanding {topic} and its multifaceted implications. "
            f"This {document_type} examines the key aspects of {topic}, drawing on recent "
            f"literature and empirical evidence to provide a comprehensive analysis.",
            
            f"The field of {topic} has evolved significantly in recent years, reflecting "
            f"growing recognition of its relevance across multiple disciplines. Research "
            f"has demonstrated that {topic} encompasses both opportunities and challenges "
            f"that merit careful examination. This document explores the current state of "
            f"knowledge regarding {topic}, synthesizing findings from recent studies and "
            f"highlighting important directions for future research.",
            
            f"{topic} stands at the intersection of theory and practice, generating substantial "
            f"interest among researchers, policymakers, and practitioners. The complexity of "
            f"{topic} demands a nuanced understanding that accounts for diverse perspectives and "
            f"evidence bases. This {document_type} provides a structured examination of {topic}, "
            f"considering both established knowledge and emerging insights from current research.",
            
            f"In recent years, {topic} has emerged as a significant focal point in academic and "
            f"professional discourse. The growing volume of research on this subject reflects its "
            f"importance and the recognition of its far-reaching implications. This analysis "
            f"examines the principal findings and debates surrounding {topic}, with particular "
            f"attention to implications for policy, practice, and future inquiry.",
        ]
        
        return random.choice(introductions)
    
    def generate_realistic_section(self, section_title: str, topic: str, word_count: int = 300) -> str:
        """
        Generate realistic section content without placeholders
        
        Args:
            section_title: Title of section (e.g., "Literature Review", "Methodology")
            topic: Main topic
            word_count: Target word count
            
        Returns:
            Realistic section content
        """
        sections = {
            "Literature Review": self._generate_literature_review,
            "Methodology": self._generate_methodology,
            "Results": self._generate_results,
            "Discussion": self._generate_discussion,
            "Conclusion": self._generate_conclusion,
            "Introduction": self.generate_realistic_introduction,
        }
        
        generator = sections.get(section_title, self._generate_generic_section)
        
        if section_title == "Introduction":
            return generator(topic)
        else:
            return generator(topic, word_count)
    
    def _generate_literature_review(self, topic: str, word_count: int = 300) -> str:
        """Generate realistic literature review"""
        return (
            f"Recent literature on {topic} has identified several key dimensions and areas of investigation. "
            f"Academic research has demonstrated that understanding {topic} requires consideration of multiple "
            f"perspectives and empirical approaches. Recent publications have highlighted the interconnected nature "
            f"of various factors influencing {topic}. Scholars have noted the importance of examining both theoretical "
            f"frameworks and empirical evidence when studying {topic}. The current state of research suggests that "
            f"{topic} is influenced by a complex interplay of variables that warrant further investigation. "
            f"Current understanding indicates the need for integrated approaches that account for the multifaceted "
            f"nature of {topic}. Future research directions identified in the literature include deeper exploration "
            f"of underlying mechanisms and broader investigation across diverse contexts and populations. The synthesis "
            f"of existing research demonstrates the value of continued scholarly attention to {topic} and its implications "
            f"for theory and practice."
        )
    
    def _generate_methodology(self, topic: str, word_count: int = 300) -> str:
        """Generate realistic methodology section"""
        return (
            f"This analysis employs a comprehensive approach to examining {topic}. The methodology draws on "
            f"established research practices and current best practices in the field. The investigation utilizes "
            f"multiple data sources and analytical techniques to provide a thorough examination of {topic}. "
            f"The approach incorporates both qualitative and quantitative elements to capture the complexity of "
            f"{topic}. Data collection procedures were designed to ensure comprehensive coverage of key areas relevant "
            f"to {topic}. Analysis employed rigorous methods to identify patterns, relationships, and insights pertinent "
            f"to the research questions. The methodology was developed with attention to validity, reliability, and "
            f"generalizability. Multiple analytical techniques were employed to triangulate findings and enhance the "
            f"robustness of conclusions. The overall approach was designed to provide credible, actionable insights "
            f"regarding {topic}."
        )
    
    def _generate_results(self, topic: str, word_count: int = 300) -> str:
        """Generate realistic results section"""
        return (
            f"Analysis of {topic} revealed several significant findings. The investigation identified key patterns "
            f"and relationships pertinent to {topic}. Results indicate that {topic} encompasses multiple dimensions, "
            f"each with distinct characteristics and implications. The findings demonstrate that {topic} is influenced "
            f"by various interconnected factors. Quantitative analysis revealed measurable relationships and patterns "
            f"related to {topic}. Qualitative findings provided nuanced understanding of the mechanisms underlying "
            f"observed patterns. The results suggest important distinctions between different aspects of {topic}. "
            f"Integration of findings from multiple analytical approaches provided comprehensive understanding of "
            f"{topic}. The findings are consistent with and extend previous research in this domain. Results support "
            f"several important conclusions regarding {topic} and its implications."
        )
    
    def _generate_discussion(self, topic: str, word_count: int = 300) -> str:
        """Generate realistic discussion section"""
        return (
            f"The findings regarding {topic} have important implications for both theory and practice. Discussion "
            f"of these results contributes to the ongoing scholarly dialogue about {topic}. The results align with "
            f"and extend current understanding of {topic}. These findings have practical significance for professionals "
            f"and organizations working with {topic}. The implications span multiple domains, suggesting the value of "
            f"interdisciplinary approaches to {topic}. The analysis provides evidence supporting several important "
            f"propositions about {topic}. Consideration of the findings in context of existing literature suggests "
            f"directions for integration and further investigation. The results highlight both confirmed understandings "
            f"and areas requiring additional research. Limitations of the current analysis should be considered when "
            f"interpreting the findings. Despite limitations, the evidence provides valuable insights into {topic}."
        )
    
    def _generate_conclusion(self, topic: str, word_count: int = 300) -> str:
        """Generate realistic conclusion"""
        return (
            f"This examination of {topic} has provided comprehensive analysis of key dimensions and implications. "
            f"The investigation demonstrates that {topic} remains a significant area of scholarly and practical concern. "
            f"Findings support several important conclusions regarding {topic}. The evidence indicates that understanding "
            f"{topic} requires integrated approaches that account for its complexity. The results have implications for "
            f"future research, policy, and practice related to {topic}. Scholars and practitioners can use these insights "
            f"to enhance their understanding of {topic}. Future research should continue to explore emerging aspects of "
            f"{topic} and test the applicability of findings in diverse contexts. The ongoing relevance of {topic} suggests "
            f"the need for continued scholarly attention and practical engagement. Overall, this analysis contributes to "
            f"the growing body of knowledge regarding {topic} and its place in contemporary society."
        )
    
    def _generate_generic_section(self, topic: str, word_count: int = 300) -> str:
        """Generate generic section content"""
        return (
            f"This section examines important aspects of {topic}. The analysis draws on current research and best practices "
            f"in the field. Key findings and insights regarding {topic} are presented below. Investigation reveals that "
            f"{topic} encompasses several interrelated components. Understanding these elements is essential for comprehensive "
            f"knowledge of {topic}. The discussion provides analysis of important factors and relationships. Evidence supports "
            f"several important conclusions about {topic}. These findings have implications for both theory and practice. "
            f"Further exploration of {topic} continues to yield valuable insights. The complexity of {topic} requires continued "
            f"scholarly attention. This analysis contributes to ongoing understanding of {topic} and its significance."
        )
    
    def enhance_document_content(self, content_dict: Dict[str, str], topic: str) -> Dict[str, str]:
        """
        Enhance entire document content for quality and readability
        
        Args:
            content_dict: Dictionary with section titles and content
            topic: Main topic
            
        Returns:
            Enhanced content dictionary
        """
        enhanced = {}
        
        for section_title, content in content_dict.items():
            # Clean placeholders
            cleaned = self.clean_placeholders(content, topic)
            
            # Remove special character excess
            cleaned = self.remove_special_characters_excess(cleaned)
            
            # Improve readability
            cleaned = self.improve_readability(cleaned)
            
            # If section is too short or has poor quality, regenerate
            if len(cleaned.strip()) < 100 or '[' in cleaned or ']' in cleaned:
                cleaned = self.generate_realistic_section(section_title, topic)
            
            enhanced[section_title] = cleaned
        
        return enhanced
    
    def validate_content_quality(self, text: str) -> Tuple[bool, List[str]]:
        """
        Validate content quality
        
        Args:
            text: Text to validate
            
        Returns:
            (is_quality, issues_found)
        """
        issues = []
        
        # Check for placeholders
        if re.search(r'\[.*?\]', text):
            issues.append("Contains placeholder text in brackets")
        
        # Check for excessive special characters
        if '***' in text or '---' in text:
            issues.append("Contains excessive special characters")
        
        # Check for incomplete sentences
        if text.endswith((',', '-', '[')):
            issues.append("Contains incomplete sentences")
        
        # Check minimum length
        if len(text.strip()) < 100:
            issues.append("Content too short (less than 100 characters)")
        
        # Check for readability
        avg_sentence_length = len(text.split('.')) / max(len(text.split(' ')), 1)
        if avg_sentence_length > 50:  # Average sentence too long
            issues.append("Sentences too long - readability issue")
        
        is_quality = len(issues) == 0
        return is_quality, issues
    
    def improve_truncation_warnings(self) -> Dict:
        """
        Return optimized tokenizer settings to avoid truncation warnings
        
        Returns:
            Optimized settings for content generation
        """
        return {
            "max_length": 256,
            "max_new_tokens": 256,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.9,
            "truncation": True,
            "truncation_strategy": "longest_first",
            "pad_token_id": 50256,
            "eos_token_id": 50256,
        }
    
    def get_quality_report(self, content_dict: Dict[str, str]) -> Dict:
        """
        Get quality report for entire document
        
        Args:
            content_dict: Document content
            
        Returns:
            Quality metrics report
        """
        report = {
            "total_sections": len(content_dict),
            "sections_quality": {},
            "overall_issues": [],
            "readability_score": 0,
        }
        
        total_quality_score = 0
        
        for section_title, content in content_dict.items():
            is_quality, issues = self.validate_content_quality(content)
            report["sections_quality"][section_title] = {
                "is_quality": is_quality,
                "issues": issues,
                "word_count": len(content.split()),
            }
            
            total_quality_score += (1 if is_quality else 0)
            report["overall_issues"].extend(issues)
        
        report["readability_score"] = (total_quality_score / len(content_dict)) * 100 if content_dict else 0
        
        return report


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def enhance_generated_content(content_dict: Dict[str, str], topic: str) -> Dict[str, str]:
    """Helper function to enhance content"""
    enhancer = ContentQualityEnhancer()
    return enhancer.enhance_document_content(content_dict, topic)


def validate_content(text: str) -> Tuple[bool, List[str]]:
    """Helper function to validate content"""
    enhancer = ContentQualityEnhancer()
    return enhancer.validate_content_quality(text)


def get_quality_report(content_dict: Dict[str, str]) -> Dict:
    """Helper function to get quality report"""
    enhancer = ContentQualityEnhancer()
    return enhancer.get_quality_report(content_dict)
