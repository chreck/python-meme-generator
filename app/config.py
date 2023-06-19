"""Contains all configuration constants."""

import pathlib


class Config:
    PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
    DATA_ROOT = PROJECT_ROOT / "_data"
    FONTS_ROOT = DATA_ROOT / "fonts"
    FONT = str(FONTS_ROOT / "IBMPlexSans-Bold.ttf")
    PHOTOS_PATH = DATA_ROOT / "photos/dog"
    TMP_ROOT = PROJECT_ROOT / "_tmp"
    STATIC_ROOT = PROJECT_ROOT / "static"
    QUOTE_FILES = [
        DATA_ROOT / "DogQuotes/DogQuotesTXT.txt",
        DATA_ROOT / "DogQuotes/DogQuotesDOCX.docx",
        DATA_ROOT / "DogQuotes/DogQuotesPDF.pdf",
        DATA_ROOT / "DogQuotes/DogQuotesCSV.csv",
    ]
