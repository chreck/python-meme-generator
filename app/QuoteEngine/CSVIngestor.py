"""CSVIngestor supports csv files to be parsed and extracts QuoteModels from.

The csv formatting lines are separated by CSV specific style.
"""

from typing import List

import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """The CSVIngestor implementation which supports CSV files."""

    """All allowed file name extensions"""
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx files and returns QuoteModel instances.

        >>> from app.config import Config
        >>> len(CSVIngestor.parse(str(Config.DATA_ROOT / 'DogQuotes/DogQuotesCSV.csv')))
        2

        Args:
            path (str): The path to the document

        Raises:
            Exception: If file extension is not supported,
                the path is incorrect or parsing failed.

        Returns:
            List[QuoteModel]: A list of quote models
        """
        cls.can_ingest_or_throw(path)
        cls.check_path_exists_or_throw(path)

        models = []
        doc = pandas.read_csv(path, header=0)

        for _, row in doc.iterrows():
            [quote, author] = row
            model = QuoteModel(quote, author)
            models.append(model)
        return models


if __name__ == "__main__":
    import doctest

    doctest.testmod()
