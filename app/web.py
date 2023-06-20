"""The web application to generate a random or custom meme.

You can start the Flask web app with

`flask -A app.web run -h 0.0.0.0 -p 3000`
"""

import os
import pathlib
import random

import requests
from flask import Flask, abort, render_template, request

from config import Config
from meme import random_image, random_quote, setup_images, setup_quotes
from MemeGenerator import MemeEngine


def setup():
    """Load all resources."""
    quote_files = Config.QUOTE_FILES
    quotes = setup_quotes(quote_files)
    images_path = Config.PHOTOS_PATH
    imgs = setup_images(images_path)
    return quotes, imgs


app = Flask(__name__)
quotes, imgs = setup()
meme = MemeEngine(Config.STATIC_ROOT)


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random_image(imgs)
    quote = random_quote(quotes)
    full_path = meme.make_meme(img, quote.body, quote.author, font=Config.FONT)
    relative_path = pathlib.Path(full_path).relative_to(
        pathlib.Path(__file__).parent.resolve()
    )
    return render_template("meme.html", path=relative_path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    if not image_url or not body or not author:
        return render_template(
            "error.html", error="Image url, body or author is not provided"
        )

    # Use requests to save the image from the image_url
    # form param to a temp local file.
    res = requests.get(image_url)
    in_file = None
    if res.status_code == 200:
        ext = image_url.split(".")[-1]
        in_file = f"{Config.TMP_ROOT}/{random.randint(0,10000000)}.{ext}"
        if not os.path.exists(Config.TMP_ROOT):
            os.makedirs(Config.TMP_ROOT)
        try:
            with open(in_file, "wb") as out:
                out.write(res.content)
        except:
            os.remove(in_file)
            return render_template(
                "error.html", error=f"Could not download and save the image."
            )
    else:
        return render_template(
            "error.html",
            error=f"Response of image download is with status code {res.status_code}",
        )

    try:
        # Use the meme object to generate a meme using this temp
        # file and the body and author form paramaters.
        full_path = meme.make_meme(in_file, body, author, font=Config.FONT)
        relative_path = pathlib.Path(full_path).relative_to(
            pathlib.Path(__file__).parent.resolve()
        )
    finally:
        # Remove the temporary saved image.
        os.remove(in_file)
    return render_template("meme.html", path=relative_path)


if __name__ == "__main__":
    app.run()
