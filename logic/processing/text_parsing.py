import re
from typing import List

import pandas as pd


def parse_clippings_to_dict(clipping_text: str) -> List[dict]:
    """
    Parses Kindle clippings and converts them into a dictionary.

    Args:
        clipping_text: A string containing the text of Kindle clippings.

    Returns:
        A dictionary where each entry represents a clipping.
    """
    # Regular expression pattern to match the book, author, location, date, and clipping text
    # pattern = r'(.*?) \((?<=\()(.*?)(?=\))\)\n- Your Highlight (on Page \d+ |)Location ' \
    #          r'(.*?) \| Added on (.*?)\n\n(.*?)(?=\n=)'
    # pattern = r'(.*?)\s\(([^)]+)\)\n- Your Highlight (?:on Page \d+ |)
    # Location (.*?) \| Added on (.*?)\n\n(.*?)(?=\n=)'
    # Easier for error checking to break this down into sections
    title_and_author_pattern = r'(?:(?<=^)|(?<===\n))([\s\S]*?)\s\(([^)]+)\)\n'
    page_pattern = r'- Your Highlight (?:on [pP]age \d+ \| )?'
    location_pattern = r'[lL]ocation (.*?) \| Added on (.*?)\n\n'
    clipping_text_pattern = r'(.*?)(?:\n===|$)'
    pattern = title_and_author_pattern + page_pattern + location_pattern + clipping_text_pattern

    # Find all matches in the clipping text
    matches = re.findall(pattern, clipping_text, re.DOTALL)

    # Convert matches to a dictionary
    clippings_dict = []
    for match in matches:
        clippings_dict.append({
            'book': match[0],
            'author': match[1],
            'location': match[2],
            'date_added': match[3],
            'clipping_text': match[4]
        })

    return clippings_dict


def dict_to_dataframe(clippings_as_dict: List[dict]) -> pd.DataFrame:
    """
    Converts a dictionary of Kindle clippings into a pandas dataframe.

    Args:
        clippings_as_dict: A dictionary where each entry represents a clipping.

    Returns:
        A dataframe where each row represents a clipping.
    """
    return pd.DataFrame(clippings_as_dict)


def parse_clippings_to_dataframe(clipping_text: str) -> pd.DataFrame:
    """
    Parses Kindle clippings and converts them into a pandas dataframe.

    Args:
        clipping_text: A string containing the text of Kindle clippings.

    Returns:
        A dataframe where each row represents a clipping.
    """
    clipping_dict = parse_clippings_to_dict(clipping_text)
    return dict_to_dataframe(clipping_dict)


def read_text_file(path: str) -> str:
    """
    Read the content of a text file at the specified path.

    Args:
        path: The path to the text file.

    Returns:
        The content of the text file as a string.
    """
    with open(path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    # Replace the BOM (byte order mark) character
    content = content.replace('\ufeff', '')

    return content


def parse_clippings_file_to_dataframe(path: str) -> pd.DataFrame:
    """
    Parse a Kindle clippings file at the specified path and convert it to a pandas dataframe.

    Args:
        path: The path to the Kindle clippings file.

    Returns:
        A dataframe where each row represents a clipping.
    """
    clipping_text = read_text_file(path)
    return parse_clippings_to_dataframe(clipping_text)
