"""Create a meme from an image and a given text.

Provide the image path, the text and the author of the text.
Provide the font to be used for the text and author.
Optionally you can define the width of the image.
"""
import os
import random

from .ImageGenerator import ImageGenerator


class MemeEngine:
    """Engine to generate a meme."""

    def __init__(self, output_dir: str):
        """Provide the path where the image can be stored."""
        self.output_dir = output_dir

    def make_meme(
        self, img_path: str, text: str, author: str, font: str, width: int = 500
    ) -> str:
        """Make a meme from the img_path, with a text and the author.

        The width you provide will take the aspect ratio into account.

        Args:
            img_path (str): Path to the image
            text (str): The text of the message in the image
            author (str): the author of the message for the image.
            font (str): the font path and file name
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

        out_path = f"{self.output_dir}/{random.randint(0,1000000)}.png"
        image_generator = ImageGenerator(
            input_image=img_path, output_image=out_path, font_file=font
        )
        message = f"{text}\n{author}"
        return image_generator.get_image(message, width)
