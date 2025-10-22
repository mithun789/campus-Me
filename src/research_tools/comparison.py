"""
Document Comparison - Compare multiple document versions
"""

from typing import Dict, List


class DocumentComparison:
    """Compare multiple document versions."""

    def compare_documents(self, doc1: str, doc2: str) -> Dict:
        """Compare two documents."""
        words1 = set(doc1.lower().split())
        words2 = set(doc2.lower().split())

        common_words = words1 & words2
        unique_to_doc1 = words1 - words2
        unique_to_doc2 = words2 - words1

        return {
            "similarity": len(common_words) / max(len(words1), len(words2)),
            "common_words": len(common_words),
            "unique_to_first": len(unique_to_doc1),
            "unique_to_second": len(unique_to_doc2),
        }

    def generate_comparison_report(self, documents: Dict[str, str]) -> str:
        """Generate comparison report for multiple documents."""
        report = "DOCUMENT COMPARISON REPORT\n" + "=" * 40 + "\n\n"

        doc_names = list(documents.keys())
        for i, name1 in enumerate(doc_names):
            for name2 in doc_names[i+1:]:
                comparison = self.compare_documents(documents[name1], documents[name2])
                report += f"\n{name1} vs {name2}:\n"
                report += f"  Similarity: {comparison['similarity']:.1%}\n"
                report += f"  Common words: {comparison['common_words']}\n"

        return report
