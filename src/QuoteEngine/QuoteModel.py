
"""The quote model to save one quote and the author of the quote."""

class QuoteModel:
    """The model to save the quote and the author."""

    def __init__(self, quote: str, author: str):
        """Init the model with quote an author."""
        self.quote = quote
        self.author = author

    def __str__(self) -> str:
        """Representation of this model as a string.

        Returns:
            str: The string of this model.
        """
        return f"QuoteModel: quote={self.quote}, author:{self.author}"

    def __repr__(self) -> str:
        """Model representation.

        Returns:
            str: Return a string as a machine code representation.
        """
        return f"QuoteModel(quote={self.quote}, author={self.author})"