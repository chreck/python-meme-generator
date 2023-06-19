"""Image Generator handles all the setup and making of the image itself.

Set input, output image path and the font file which must be used.

Getting the image needs the message to be inserted and the width of the image itself.
"""
from PIL import Image, ImageDraw, ImageFont


class ImageGenerator:
    """Image generator for creating memes."""

    def __init__(self, input_image: str, output_image: str, font_file: str):
        """Init the imaga generator by setting the image file and font file location.

        Args:
            input_image (str): The input file name and path
            output_image (str): The output file name and path
            font_file (str): The font file name and path
        """
        self.input_image = input_image
        self.output_image = output_image
        self.font = ImageFont.truetype(font_file, 20)
        self.stroke_width = 3

    def get_image(self, message: str, width: int) -> str:
        """Get the image with the message centered.

        Args:
            message (str): Text message to insert
            width (int): The maximum width of the image.

        Raises:
            Exception: If the creation of the fails it raises an exception.

        Returns:
            str: The path of the image which was created
        """
        self.message = message
        self.width = width
        try:
            self.image = Image.open(self.input_image)
            self.__resize()
            self.__draw_text()
            self.image.save(self.output_image)
            return self.output_image
        except Exception as e:
            raise Exception(f"Could not generate the image from the path '{self.input_image}'. Error: {e}")

    def __resize(self):
        """Resize the image to width and height."""
        self.__calculate_height()
        size = (
            self.width, self.height
        )
        self.image = self.image.resize(size)

    def __calculate_height(self):
        """Calculate the height by the given width."""
        self.factor = self.image.height / self.image.width
        self.height = int(self.factor * self.width)

    def __draw_text(self):
        """Draw the text into the image."""
        self.draw = ImageDraw.Draw(self.image)
        self.__calculate_message_height()
        self.__calculate_message_width()
        self.__calculate_xy_message()
        self.draw.text(
            self.xy_message,
            self.message,
            align="center",
            font=self.font,
            fill='black',
            stroke_width=self.stroke_width,
            stroke_fill='white'
        )

    def __calculate_message_width(self):
        """Calculate the maximum width of the text itself to center it."""
        lines = self.message.split('\n')
        max_width = 0
        for line in lines:
            line_width = self.draw.textlength(
                line, self.font,
            )
            max_width = max(max_width, line_width)
        self.message_width = min(max_width, self.width)

    def __calculate_xy_message(self):
        """Calculate the x and y to center the text in the image."""
        x = (self.width  / 2) - ( self.message_width / 2)
        y = self.height - self.message_height - 50
        self.xy_message = (x, y)

    def __calculate_message_height(self):
        # tuple(width, height)
        size: tuple = self.font.getsize(
            self.message,
            stroke_width=self.stroke_width,
        )
        (width, height) = size
        self.message_height = height
