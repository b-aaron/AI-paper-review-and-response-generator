"""
pdf_parser.py
Parses an academic paper PDF and extracts its text content.
"""

import os


class PDFParser:
    """Extract text from a PDF file using PyMuPDF (fitz)."""

    def __init__(self, pdf_path: str):
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        self.pdf_path = pdf_path

    def extract_text(self) -> str:
        """Return the full text extracted from every page of the PDF."""
        try:
            import fitz  # PyMuPDF
        except ImportError as exc:
            raise ImportError(
                "PyMuPDF is required for PDF parsing. "
                "Install it with: pip install pymupdf"
            ) from exc

        text_parts: list[str] = []
        with fitz.open(self.pdf_path) as doc:
            for page in doc:
                text_parts.append(page.get_text())

        return "\n".join(text_parts)
