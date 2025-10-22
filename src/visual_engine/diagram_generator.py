"""
Diagram Generator - Generate diagrams, flowcharts, and concept maps
"""

from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class DiagramGenerator:
    """
    Generate various diagram types (flowcharts, concept maps, etc.).
    """

    def __init__(self):
        """Initialize diagram generator."""
        pass

    def generate_flowchart(
        self, steps: List[str], title: str = "Process Flowchart"
    ) -> str:
        """
        Generate ASCII flowchart.

        Args:
            steps: List of process steps
            title: Flowchart title

        Returns:
            ASCII flowchart string
        """
        flowchart = f"\n{title}\n"
        flowchart += "=" * len(title) + "\n\n"

        for i, step in enumerate(steps):
            flowchart += f"  [{i+1}] {step}\n"
            if i < len(steps) - 1:
                flowchart += "      |\n"
                flowchart += "      v\n"

        return flowchart

    def generate_concept_map(self, central_concept: str, connections: Dict[str, List[str]]) -> str:
        """
        Generate ASCII concept map.

        Args:
            central_concept: Central concept
            connections: Dictionary of {concept: [related_concepts]}

        Returns:
            ASCII concept map string
        """
        concept_map = f"\n        {central_concept}\n"
        concept_map += "        " + ("=" * len(central_concept)) + "\n"
        concept_map += "\n"

        for concept, related in connections.items():
            concept_map += f"    {concept}:\n"
            for item in related:
                concept_map += f"        - {item}\n"
            concept_map += "\n"

        return concept_map

    def generate_hierarchy_diagram(self, hierarchy: Dict[str, List[str]]) -> str:
        """
        Generate ASCII hierarchy diagram (org chart style).

        Args:
            hierarchy: Dictionary representing hierarchy {parent: [children]}

        Returns:
            ASCII hierarchy diagram string
        """
        diagram = ""

        def add_level(items, level=0, parent_text=""):
            indent = "  " * level
            for item in items:
                if isinstance(item, dict):
                    key = list(item.keys())[0]
                    children = item[key]
                    diagram_line = f"{indent}├─ {key}\n"
                    diagram = diagram_line.replace
                    for child in children:
                        diagram += f"{indent}│  ├─ {child}\n"
                else:
                    diagram = f"{indent}├─ {item}\n"

            return diagram

        for parent, children in hierarchy.items():
            diagram += f"{parent}\n"
            for child in children:
                diagram += f"├─ {child}\n"

        return diagram

    def generate_timeline(self, events: Dict[str, str]) -> str:
        """
        Generate ASCII timeline.

        Args:
            events: Dictionary of {year_or_date: event_description}

        Returns:
            ASCII timeline string
        """
        timeline = "\nTIMELINE\n"
        timeline += "=" * 40 + "\n\n"

        for time_point, event in events.items():
            timeline += f"  {time_point:<15} -----> {event}\n"

        return timeline

    def generate_venn_diagram_text(
        self, set_a: str, set_b: str, intersection: str = None
    ) -> str:
        """
        Generate text representation of Venn diagram.

        Args:
            set_a: Items in set A
            set_b: Items in set B
            intersection: Items in intersection

        Returns:
            Text Venn diagram
        """
        diagram = """
          (A)              (B)
         / A \\            / B \\
        /  A  \\          /  B  \\
       |    A  |======  |  B   |
        \\  A  /  BOTH   \\  B  /
         \\ A /            \\ B /
          (A)              (B)
        """

        # Replace with actual content
        diagram = diagram.replace("A", set_a[:10])
        diagram = diagram.replace("B", set_b[:10])

        return diagram

    def generate_matrix_diagram(
        self, rows: List[str], cols: List[str], title: str = "Matrix"
    ) -> str:
        """
        Generate text matrix/grid diagram.

        Args:
            rows: Row labels
            cols: Column labels
            title: Diagram title

        Returns:
            Text matrix diagram
        """
        diagram = f"\n{title}\n"
        diagram += "=" * (len(title) + 20) + "\n\n"

        # Header
        diagram += "       " + "  ".join(f"{col:8}" for col in cols) + "\n"
        diagram += "    " + "-" * (len(cols) * 10) + "\n"

        # Rows
        for row in rows:
            diagram += f"{row:6} | "
            for col in cols:
                diagram += "[   ]  "
            diagram += "\n"

        return diagram

    def generate_svg_flowchart(self, steps: List[str]) -> str:
        """
        Generate SVG flowchart.

        Args:
            steps: List of process steps

        Returns:
            SVG flowchart string
        """
        svg_parts = []
        svg_parts.append(
            '<?xml version="1.0" encoding="UTF-8"?>'
        )
        svg_parts.append(
            f'<svg width="400" height="{len(steps)*80 + 40}" xmlns="http://www.w3.org/2000/svg">'
        )

        y_pos = 20

        for i, step in enumerate(steps):
            # Rectangle for step
            svg_parts.append(
                f'<rect x="50" y="{y_pos}" width="300" height="50" fill="#e8f4f8" stroke="#333" stroke-width="2"/>'
            )

            # Text
            svg_parts.append(
                f'<text x="200" y="{y_pos + 30}" text-anchor="middle" font-family="Arial" font-size="14">{step[:30]}</text>'
            )

            y_pos += 50

            # Arrow if not last
            if i < len(steps) - 1:
                svg_parts.append(
                    f'<polygon points="200,{y_pos} 195,{y_pos+10} 205,{y_pos+10}" fill="#333"/>'
                )
                svg_parts.append(
                    f'<line x1="200" y1="{y_pos}" x2="200" y2="{y_pos+15}" stroke="#333" stroke-width="2"/>'
                )

            y_pos += 20

        svg_parts.append("</svg>")

        return "\n".join(svg_parts)

    def generate_swimlane_diagram(
        self, lanes: Dict[str, List[str]], title: str = "Process Swimlanes"
    ) -> str:
        """
        Generate text representation of swimlane diagram.

        Args:
            lanes: Dictionary of {lane_name: [activities]}
            title: Diagram title

        Returns:
            Text swimlane diagram
        """
        diagram = f"\n{title}\n"
        diagram += "=" * (len(title) + 10) + "\n\n"

        for lane_name, activities in lanes.items():
            diagram += f"[{lane_name}]\n"
            for activity in activities:
                diagram += f"  --> {activity}\n"
            diagram += "\n"

        return diagram
