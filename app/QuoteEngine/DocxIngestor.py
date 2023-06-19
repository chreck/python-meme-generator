"""DocxIngestor supports docx files to be parsed and extracts QuoteModels from.

The docx formatting lines are defined by "quote - author".
"""

from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """The DocxIngestor implementation which supports Word Documents docx files."""

    """All allowed file name extensions"""
    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx files and returns QuoteModel instances.

        >>> from app.config import Config
        >>> len(DocxIngestor.parse(str(Config.DATA_ROOT / 'DogQuotes/DogQuotesDOCX.docx')))
        4

        Args:
            path (str): The path to the document

        Raises:
            Exception: If file extension is not supported, the path is incorrect or parsing failed.

        Returns:
            List[QuoteModel]: A list of quote models
        """
        cls.can_ingest_or_throw(path)
        cls.check_path_exists_or_throw(path)

        models = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            try:
                if para.text != "":
                    [quote, author] = para.text.split(" - ")
                    model = QuoteModel(quote, author)
                    models.append(model)
            except:
                print(f"Could not parse line {para.text}")
        return models


if __name__ == "__main__":
    import doctest

    doctest.testmod()
