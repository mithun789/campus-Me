"""
Configuration settings for AI Academic Document Suite
"""

# AI Models and Generation
TEXT_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"
TEMPERATURE = 0.7
TOP_P = 0.95
CHUNK_SIZE = 2000

# Document Settings
DEFAULT_PAGE_SIZE = "A4"
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 12
LINE_SPACING = 1.5
MARGINS = {
    "top": 1.0,
    "bottom": 1.0,
    "left": 1.0,
    "right": 1.0
}  # inches

# Citation Styles
CITATION_STYLES = ["APA", "MLA", "Chicago", "Harvard", "IEEE"]
DEFAULT_CITATION_STYLE = "APA"

# Visualization Settings
CHART_STYLE = "seaborn"
COLOR_PALETTE = "Set2"
DPI = 100  # ✅ OPTIMIZED: Web resolution (not 300 for print)
FIGURE_WIDTH = 8  # ✅ OPTIMIZED: Reduced from 10
FIGURE_HEIGHT = 6

# Export Formats
SUPPORTED_FORMATS = ["pdf", "docx", "md", "html", "latex"]
DEFAULT_FORMATS = ["pdf", "docx"]

# Performance
MAX_GENERATION_TIME = 180  # 3 minutes
CACHE_ENABLED = True
MAX_FILE_SIZE_MB = 50
MAX_GENERATION_LENGTH = 256  # ✅ OPTIMIZED: Per section (not 4096)
REQUEST_QUEUE_SIZE = 5  # ✅ OPTIMIZED: Limit concurrent requests
REQUEST_TIMEOUT = 120  # ✅ OPTIMIZED: 2 minute timeout

# Document Sections
DEFAULT_SECTIONS = [
    "Introduction",
    "Literature Review",
    "Methodology",
    "Results",
    "Discussion",
    "Conclusion",
    "References"
]

# Content Generation Parameters
MIN_WORDS_PER_SECTION = 150
MAX_WORDS_PER_SECTION = 500

# UI Settings
PREVIEW_HEIGHT = 500
DOWNLOAD_BUTTON_COLOR = "#4CAF50"

# Ethics Warning
ETHICS_WARNING = """
⚠️ RESEARCH & EDUCATIONAL TOOL ONLY

This AI Academic Document Suite is designed for:
✓ Understanding AI capabilities in document creation
✓ Learning how AI can assist academic work
✓ Generating content for study and research purposes
✓ Demonstrating next-generation AI technologies

NOT FOR:
✗ Submitting AI-generated work as original student work
✗ Academic fraud or plagiarism
✗ Violating academic integrity policies
✗ Deception of instructors or institutions

Using this tool to submit AI-generated content as your own work 
violates academic integrity policies and may result in serious 
consequences including course failure or disciplinary action.

This tool should be used transparently with proper disclosure of AI use.
"""

# File Upload Settings
ALLOWED_UPLOAD_EXTENSIONS = [".pdf", ".docx", ".doc", ".txt", ".md"]
UPLOAD_TEMP_DIR = "/tmp/uploads"

# API Rate Limiting
API_RATE_LIMIT = 100  # requests per hour
API_TIMEOUT = 60  # seconds

# Model Fallbacks
FALLBACK_MODELS = [
    "HuggingFaceH4/zephyr-7b-beta",
    "google/flan-t5-large",
    "gpt2"
]

# Logging
ENABLE_LOGGING = True
LOG_FILE = "app.log"
LOG_LEVEL = "INFO"
