
"""The quote model to save one quote and the author of the quote."""

class QuoteModel:
    """The model to save the quote and the author."""

    def __init__(self, body: str, author: str):
        """Init the model with body and author."""
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """Representation of this model as a string.

        Returns:
            str: The string of this model.
        """
        return f"QuoteModel: body={self.body}, author:{self.author}"

    def __repr__(self) -> str:
        """Model representation.

        Returns:
            str: Return a string as a machine code representation.
        """
        return f"QuoteModel(body={self.body}, author={self.author})"