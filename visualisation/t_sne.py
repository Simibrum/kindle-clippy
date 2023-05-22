"""2D Projections Using t-SNE."""
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from visualisation.clustering import get_embedding_matrix


def get_tsne_projection(df, number_of_components: int = 2, perplexity: float = 30.0) -> np.ndarray:
    """Get the t-SNE projection of the embeddings.

    Args:
        df: The DataFrame containing the embeddings.
        number_of_components: The number of components to use. Default is 2.
        perplexity: The perplexity to use. Default is None.

    Returns:
        The t-SNE projection of the embeddings.
    """
    # Get the embedding matrix
    embedding_matrix = get_embedding_matrix(df)

    # Perform t-SNE projection
    tsne = TSNE(n_components=number_of_components, random_state=42, perplexity=perplexity)
    tsne_projection = tsne.fit_transform(embedding_matrix)

    return tsne_projection


def add_tsne_projection(df, number_of_components: int = 2, perplexity: float = 30.0) -> pd.DataFrame:
    """Add t-SNE projection to a DataFrame.

    Args:
        df: The DataFrame containing the embeddings.
        number_of_components: The number of components to use. Default is 2.
        perplexity: The perplexity to use. Default is None.

    Returns:
        The DataFrame with t-SNE projection added.
    """
    # Get the t-SNE projection
    tsne_projection = get_tsne_projection(df, number_of_components, perplexity)

    # Add t-SNE projection to the DataFrame
    for i in range(number_of_components):
        df[f'tsne_{i}'] = tsne_projection[:, i]

    return df
