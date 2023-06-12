"""The Ingestor class inherits from IngestorInterface and implements the abstract methods.

It detects by the filename extension which ingestor must be selected. The selected ingestor parses the file and returns the quote models.

The method `parse` parses automatically by the given file name extension and returns the quote models.
"""

from typing import List

from IngestorInterface import IngestorInterface
from DocxIngestor import DocxIngestor
from CSVIngestor import CSVIngestor
from PDFIngestor import PDFIngestor
from TextIngestor import TextIngestor

from QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """The ingestor class parses docx, csv, pdf and text files."""

    """All supported ingestors."""
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file if can ingest the path to the file and returns the quote models.

        Args:
            path (str): The path to the file to parse.

        Returns:
            List[QuoteModel]: a list of quote models.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        return []