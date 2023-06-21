"""PDFIngestor supports pdf files to be parsed and extracts QuoteModels from.

The pdf formatting lines are defined by "quote - author".
"""

import os
import platform
import random
import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """The PDFIngestor implementation which supports PDF files."""

    """All allowed file name extensions"""
    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf files and returns QuoteModel instances.

        >>> from app.config import Config
        >>> len(PDFIngestor.parse(str(Config.DATA_ROOT / 'DogQuotes/DogQuotesPDF.pdf')))
        3

        Args:
            path (str): The path to the document

        Raises:
            Exception: If file extension is not supported, the path is incorrect or parsing failed.

        Returns:
            List[QuoteModel]: A list of quote models
        """
        cls.can_ingest_or_throw(path)
        cls.check_path_exists_or_throw(path)
        if not cls.__is_tool_available("pdftotext"):
            raise Exception(
                "The tool pdftotext is not available. Please first install the tool."
            )

        models = []
        tmp: str = None
        try:
            if not os.path.exists("./tmp"):
                os.mkdir("./tmp")
            tmp = f"./tmp/{random.randint(0,100000000)}.txt"
            process_args = ["pdftotext", path, tmp]
            if platform.system() == "Darwin":
                process_args = ["pdftotext", "-simple", path, tmp]
            subprocess.call(process_args)
            with open(tmp, "r") as file_ref:
                for line in file_ref.readlines():
                    line = line.strip("\n\r").strip()
                    if len(line) > 0:
                        parse = line.split(" - ")
                        [quote, author] = parse
                        model = QuoteModel(quote, author)
                        models.append(model)
        finally:
            if tmp:
                os.remove(tmp)
        return models

    @classmethod
    def __is_tool_available(cls, name) -> bool:
        """Verify if a specific system tool is available or not."""
        from shutil import which

        return which(name) is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
