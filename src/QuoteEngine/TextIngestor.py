"""TextIngestor supports text files to be parsed and extracts QuoteModels from.

The text formatting lines are defined by "quote - author".
"""

from typing import List

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """The TextIngestor implementation which supports text files."""

    """All allowed file name extensions"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse text files and returns QuoteModel instances.

        >>> len(TextIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
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
        with open(path, "r") as file_ref:
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    [quote, author] = parse
                    model = QuoteModel(quote, author)
                    models.append(model)

        return models

if __name__ == "__main__":
    import doctest
    doctest.testmod()