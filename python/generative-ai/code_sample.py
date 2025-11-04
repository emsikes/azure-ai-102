import os
from pathlib import Path
from typing import List, Dict, Optional


class DocumentProcessor:
    # Supported file types
    SUPPORTED_FORMATS = {
        '.txt': 'text',
        '.pdf': 'pdf',
        '.docx': 'docx',
        '.doc': 'doc',
        '.pptx': 'pptx',
        '.md': 'markdown',
        '.html': 'html',
        '.csv': 'csv'
    }

    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

    def _detect_file_type(self, file_path: str) -> str:
        """
        Detect the file type based on extension.

        Why this matters:
        - Different files need different extraction methods
        - Helps us route to the right loader
        - Provides clear error messages for unsupported types
        """
        suffix = Path(file_path).suffix.lower()

        if suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format: {suffix}. "
                f"Supported formats: {list(self.SUPPORTED_FORMATS.keys())}"
            )

        return self.SUPPORTED_FORMATS[suffix]
