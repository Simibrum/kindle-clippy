"""Code to provide embeddings for text using the OpenAI Embedding API."""
from typing import List
import os
import pandas as pd
import openai

# Get the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")


def get_embedding(text: str, model: str = "text-embedding-ada-002") -> List[float]:
    """
    Get the embedding for a given text using the OpenAI Embedding API.

    Args:
        text: The input text.
        model: The model name or ID to use for embeddings. Default is "text-embedding-ada-002".

    Returns:
        The embedding as a list of floats.
    """
    text = text.replace("\n", " ")
    response = openai.Embedding.create(input=[text], model=model, api_key=openai_api_key)
    embedding = response['data'][0]['embedding']
    return embedding


def add_embeddings_to_dataframe(
        df: pd.DataFrame,
        text_column: str,
        embedding_column: str = "embedding",
        model: str = "text-embedding-ada-002") -> pd.DataFrame:
    """
    Add embeddings to a dataframe for a specified text column.

    Args:
        df: The input dataframe.
        text_column: The name of the column containing the text.
        embedding_column: The name of the column to store the embeddings.
        model: The model name or ID to use for embeddings. Default is "text-embedding-ada-002".

    Returns:
        The modified dataframe with the embeddings added.
    """
    # Create a new column for embeddings
    df[embedding_column] = df[text_column].apply(lambda x: get_embedding(x, model))

    return df
