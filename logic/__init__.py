"""Wrappers to shortcut some of the function flows."""
import os
import pandas as pd

from logic.processing.text_parsing import parse_clippings_file_to_dataframe
from logic.processing.token_analysis import calculate_cost_of_embeddings
from logic.processing.embeddings import add_embeddings_to_dataframe
from logic.querying.embedding_search import run_similarity_query

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DEFAULT_CLIPPINGS_FILE_PATH = os.path.join(parent_dir, "My Clippings.txt")


def get_dataframe_with_embeddings(
        clippings_file_path: str = DEFAULT_CLIPPINGS_FILE_PATH,
        api_key: str = None
) -> pd.DataFrame:
    """Parse the clippings file and add embeddings to the dataframe."""
    df = parse_clippings_file_to_dataframe(clippings_file_path)
    if api_key:
        df = add_embeddings_to_dataframe(df, api_key=api_key)
    else:
        df = add_embeddings_to_dataframe(df)
    return df
