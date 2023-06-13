
import random
import os

from QuoteEngine import MemeEngine, QuoteModel
from QuoteEngine import Ingestor
from config import PHOTOS_PATH, DATA_ROOT, TMP_ROOT

def setup_images(image_path=None):

    images = None
    if image_path:
        images = []
        for root, dirs, files in os.walk(image_path):
            images = [os.path.join(root, name) for name in files]

    return images

def setup_quotes(quote_files=None):

    if not quote_files:
        quote_files = [DATA_ROOT / 'DogQuotes/DogQuotesTXT.txt',
                       DATA_ROOT / 'DogQuotes/DogQuotesDOCX.docx',
                       DATA_ROOT / 'DogQuotes/DogQuotesPDF.pdf',
                       DATA_ROOT / 'DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        if not os.path.exists(file):
            raise Exception(f"The quote file {file} does not exist")
        quotes.extend(Ingestor.parse(str(file)))

    return quotes

def random_image(imgs):
    return random.choice(imgs)

def random_quote(quotes):
    return random.choice(quotes)

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    image = None
    quote = None
    image_path = None

    if path is None:
        image_path = PHOTOS_PATH
    else:
        if os.path.isdir(path[0]):
            image_path = path[0]
        elif os.path.exists(path[0]):
            image = path[0]
        else:
            raise Exception(f"Image path {path} does not exist.")

    if image_path:
        images = setup_images(image_path)
        image = random_image(images)

    if body is None:
        quotes = setup_quotes()
        quote = random_quote(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine(TMP_ROOT)
    path = meme.make_meme(image, quote.body, quote.author)
    return path
