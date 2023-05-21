import pandas as pd
import tiktoken


def count_total_tokens(df: pd.DataFrame,
                       text_column: str = 'clipping_text',
                       encoding_name: str = "cl100k_base") -> int:
    """
    Counts the total number of tokens in a specified column of a dataframe.

    Args:
        df: A pandas dataframe containing text.
        text_column: The column of the dataframe that contains the text. Default is 'clipping_text'.
        encoding_name: The encoding name to be used for counting tokens.

    Returns:
        The total number of tokens in the dataframe.
    """
    # Initialize a counter
    total_tokens = 0

    # Loop over each row in the dataframe
    for _, row in df.iterrows():
        # Count the tokens in the text
        num_tokens = count_tokens(row[text_column], encoding_name)
        # Add the number of tokens to the total
        total_tokens += num_tokens

    return total_tokens


def calculate_cost_of_embeddings(df: pd.DataFrame,
                                 text_column: str = 'clipping_text',
                                 encoding_name: str = "cl100k_base") -> float:
    """
    Calculates the cost of obtaining embeddings for a dataframe of text.

    Args:
        df: A pandas dataframe containing text to calculate embeddings for.
        text_column: The column of the dataframe that contains the text. Default is 'clipping_text'.
        encoding_name: The encoding name to be used for counting tokens.

    Returns:
        The cost of obtaining embeddings for all text in the dataframe.
    """
    # Count the total tokens in the dataframe
    total_tokens = count_total_tokens(df, text_column, encoding_name)

    # Compute the cost in dollars
    cost = (total_tokens / 1000) * 0.0004

    return cost


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens
