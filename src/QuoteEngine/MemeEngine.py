"""Create a meme from an image and a given text.

Provide the image path, the text and the author of the text. Optionally you can define
the width of the image.
"""
from PIL import Image, ImageDraw, ImageFont
import random
import os

class MemeEngine:
    """Engine to generate a meme."""

    def __init__(self, output_dir: str):
        """Provide the path where the image can be stored."""
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Make a meme from the img_path, with a text and the author.

        The width you provide will take the aspect ratio into account.

        Args:
            img_path (str): Path to the image
            text (str): The text of the message in the image
            author (str): the author of the message for the image.
            width (int, optional): The final width of the image. Defaults to 500.

        Raises:
            Exception: Raise exception if reading or saving of the image path can not be done.

        Returns:
            str: The path of the output image.
        """
        if not os.path.exists(img_path):
            raise Exception(f"The image path {img_path} does not exists")

        if not os.path.exists(self.output_dir):
            try:
                os.mkdir(self.output_dir)
            except:
                raise Exception(f"Could not create the output folder {self.output_dir}")

        try:
            im = Image.open(img_path)
            factor = im.height / im.width
            im = im.resize((width, factor * width))

            fnt = ImageFont.truetype("./_data/fonts/IBMPlexSans-Bold.ttf", 20)
            d = ImageDraw.Draw(im)

            # calculate the max width of the texts and should not be larger than the width itself.
            message_width_max = min(max(d.textlength(text, font=fnt), d.textlength(author, font=fnt)), width)

            # add the message
            message = f"{text}\n{author}"
            xy = ( (width - message_width_max) / 2, 350)
            d.text(xy, message, align="center", font=fnt, fill='black', stroke_width=3, stroke_fill='white')

            # save the image
            out_path = f"{self.output_dir}/{random.randint(0,1000000)}.png"
            im.save(out_path)
            return out_path
        except Exception as e:
            raise Exception("Could not generate the image from the path {img_path}. Error: {e}")
