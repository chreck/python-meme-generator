# Project

Create a meme with an image and a text message. To generate the meme you can use the CLI and or the web interface.

## CLI interface

Before you can use the CLI please go through the installation steps below.

Run `python3 -m app.cli` so it is automatically selecting an image and a quote. By that it creates
a meme image and returns the path to the generated image. To use a specific image enter the `--path`, and
to use a specific body text enter it over `--body` and also enter the `--author`. If you enter the body you also
need to enter the author.

## Web interface

Before you can use the CLI please go through the installation steps below.

Run `flask -A app.web run -h 0.0.0.0 -p 3000` to run the web app. On the web interface it generates a random meme. If you press
the "Creator" button you can specify the image to download, the body and the author text to generate the meme. As an example you can use the Image URL http://0.0.0.0:3000/static/ns8230-image.jpg, enter any body and author text and press "Create Meme!".

# Installation

It is recommended to use a virtual environment. So please create a local one with

`python3 -m venv venv`

`source venv/bin/active`

After that you can install the dependencies for this project over the terminal command:

`pip -r requirements.txt`

# Test

In the QuoteEngine are a few doctest implemented

Run

- `python3 -m app.QuoteEngine.TextIngestor`
- `python3 -m app.QuoteEngine.CSVIngestor`
- `python3 -m app.QuoteEngine.DocxIngestor`
- `python3 -m app.QuoteEngine.PDFIngestor`

to test with doctest.
