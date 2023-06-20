"""The meme helper functions for setup image paths and quotes.

Selection of an image or quote in a list.

Generation of the meme by an image and a quote.
"""
import os
import random
from typing import List

from config import Config
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


def setup_images(image_path=None) -> List:
    """Return image files from an image path. Parse the path and return the paths to the images.

    Args:
        image_path (any, optional): The string or path to the images. Defaults to None.

    Returns:
        List: The list of images or None.
    """
    image_files = None
    if image_path:
        image_files = []
        for root, _, files in os.walk(image_path):
            image_files = [os.path.join(root, file_name) for file_name in files]

    return image_files


def setup_quotes(quote_files: str = None) -> List[QuoteModel]:
    """Return quotes from a list of quote files. Parse the quote file and extract the quotes.

    Args:
        quote_files (str, optional): Path or string of the quote files

    Returns:
        List: A list of QuoteModel

    """
    if not quote_files:
        quote_files = [
            Config.DATA_ROOT / "DogQuotes/DogQuotesTXT.txt",
            Config.DATA_ROOT / "DogQuotes/DogQuotesDOCX.docx",
            Config.DATA_ROOT / "DogQuotes/DogQuotesPDF.pdf",
            Config.DATA_ROOT / "DogQuotes/DogQuotesCSV.csv",
        ]
    quotes = []
    for file in quote_files:
        if not os.path.exists(file):
            raise Exception(f"The quote file {file} does not exist")
        quotes.extend(Ingestor.parse(str(file)))

    return quotes


def random_image(image_files: List[str]) -> str:
    """Generate a random image from image files.

    Args:
        image_files (List): List of image files

    Returns:
        str: Return a path or string to the image file
    """
    return random.choice(image_files)


def random_quote(quotes: List[QuoteModel]) -> QuoteModel:
    """Generate a random quote form a list of quotes.

    Args:
        quotes (List[QuoteModel]): The list of quotes.

    Returns:
        QuoteModel: Return the random selected quote model.
    """
    return random.choice(quotes)


def generate_meme(path=None, body: str = None, author: str = None) -> str:
    """Generate a meme from an image and a quote.

    Args:
        path (any, optional): The path can be a folder or a file. Defaults to None.
        body (str, optional): The body text of the quote. Defaults to None.
        author (str, optional): The author of the quote. Defaults to None.

    Raises:
        Exception: Raise an exception if the image path is not existing or the author is missing
            when the body text is present.

    Returns:
        str: Return the path of the generate image.
    """
    image_file = None
    quote = None
    image_folder = None

    if path is None:
        image_folder = Config.PHOTOS_PATH
    else:
        if os.path.isdir(path):
            image_folder = path
        elif os.path.isfile(path):
            image_file = path
        else:
            raise Exception(f"Image path {path} does not exist.")

    if image_folder:
        image_files = setup_images(image_folder)
        image_file = random_image(image_files)

    if body is None:
        quotes = setup_quotes()
        quote = random_quote(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine(Config.TMP_ROOT)
    path = meme.make_meme(image_file, quote.body, quote.author, font=Config.FONT)
    return path
