"""Functions to run."""
import pandas as pd


def add_embeddings_to_dataframe(dataframe: pd.DataFrame, api_key: str) -> pd.DataFrame:
    """
    Adds OpenAI embeddings to the dataframe for each clipping.

    Args:
        dataframe: A pandas dataframe containing Kindle clippings.
        api_key: A string containing the OpenAI API key.

    Returns:
        A dataframe with an additional column for embeddings.
    """
    pass  # placeholder for actual logic


def run_similarity_query(query: str, dataframe: pd.DataFrame):
    """
    Runs a similarity query against the vector database of clippings.

    Args:
        query: A string containing the search query.
        dataframe: A pandas dataframe containing the vector database of clippings.

    Returns:
        The search results.
    """
    pass  # placeholder for actual logic
