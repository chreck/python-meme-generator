"""Main application as a CLI.

Calling this file to run the CLI.
"""
import argparse
import pathlib

from meme import generate_meme

def make_parser() -> argparse.ArgumentParser:
    """Create an argument parser for the CLI meme generator.

    Returns:
        ArgumentParser: returns the argument parser
    """
    parser = argparse.ArgumentParser(
        description="Create a meme from an image and a quote. "
        "If you provide a body you also need to provide an author. "
        "If no argument is defined a random selection of image and text is done."
    )
    parser.add_argument(
        "--path",
        type=pathlib.Path,
        default=None,
        help="path to an image file or files",
    )
    parser.add_argument(
        "--body",
        type=str,
        default=None,
        help="quote body to add to the image",
    )
    parser.add_argument(
        "--author",
        type=str,
        default=None,
        help="quote author to add to the image",
    )
    return parser

if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    print(generate_meme(args.path,args.body,args.author))