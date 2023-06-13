import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import MemeEngine
from meme import random_image, random_quote, setup_images, setup_quotes
from config import PHOTOS_PATH, DATA_ROOT, STATIC_ROOT, QUOTE_FILES

app = Flask(__name__)

meme = MemeEngine(STATIC_ROOT)

def setup():
    """ Load all resources """

    quote_files = QUOTE_FILES
    quotes = setup_quotes(quote_files)

    images_path = PHOTOS_PATH
    imgs = setup_images(images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random_image(imgs)
    quote = random_quote(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
