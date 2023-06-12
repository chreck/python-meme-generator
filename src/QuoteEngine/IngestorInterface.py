"""An ingesture interface abstract class checks which extensions are supported by the concrete implementation.

The class method `can_ingest` verifies if the concrete class supports the file extension to parse the content.

The class method `parse` needs to be implemented in the inherited classes and must parse the content by the file
name extension. So i.e. a file extension with .pdf means it is a PDF and the content must be handeled as it is a PDF
document.
"""

from abc import ABC, abstractmethod
from typing import List
from os.path import exists

from QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Interface of the ingestor."""

    """All allowed file name extensions."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Can ingest the file in the path.

        Args:
            path (str): the path to the file

        Returns:
            bool: true if we support this file extension
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def can_ingest_or_throw(cls, path: str):
        """Test if we can ingest and throws an Exception.

        Args:
            path (str): the path to the file

        Raises:
            Exception: If the extension is not supported
        """
        if not cls.can_ingest(path):
            raise Exception("Can not ingest the file extension f{ext}")

    @classmethod
    def check_path_exists_or_throw(cls, path: str):
        """Check the path if the file exists.

        Args:
            path (str): The path where the file is stored

        Raises:
            Exception: If the file does not exists.

        """
        if not exists(path):
            raise Exception(f"The path '{path}' does not exists.")

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the fil in the path and returns the quotes as a list.

        Args:
            path (str): The path to the file.

        Raises:
            NotImplementedError: The method needs to be overwritten otherwise we raise an error.

        Returns:
            List[QuoteModel]: A list of QuoteModels
        """
        raise NotImplementedError()

