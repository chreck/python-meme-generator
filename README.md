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

# Implementation

## cli.py

The client interface is saved in the file `cli.py` it parses the arguments, generates the images and returns the path to the generated meme image file.

## config.py

The configuration for the different paths and files where the quotes, images and fonts are saved is defined in the `config.py` file.

## meme.py

The file `meme.py` contains a few helper functions which are used for the CLI and the web interface.

## web.py

The flask web application is implemented in the file `web.py`.

## MemeGenerator module

The meme generator module `MemeGenerator` has the `MemeEngine` which makes the meme by image, text, author. The image generation is encapsulated in the class `ImageGenerator`.

## QuoteEngine module

The module `QuoteEngine` takes part of the automatically reading of files which are storing quotes. It can read CSV, Docx, PDF and normal text files.

# Image Copyright

The image `app/static/ns8230-image.jpg` has the https://creativecommons.org/publicdomain/zero/1.0/ license. Image source is from https://www.rawpixel.com/image/5926065/photo-image-background-public-domain-dog
