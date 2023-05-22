"""Code to perform clustering on the embeddings of the data."""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def get_embedding_matrix(df) -> np.ndarray:
    """Get the embedding matrix from a DataFrame.

    Args:
        df: The DataFrame containing the embeddings.

    Returns:
        The embedding matrix.
    """
    return np.vstack(df.embedding.values)


def add_cluster_labels(df, number_of_clusters: int = 10) -> pd.DataFrame:
    """Add cluster labels to a DataFrame.
    
    Args:
        df: The DataFrame containing the embeddings.
        number_of_clusters: The number of clusters to use. Default is 10.
    
    Returns:
        The DataFrame with cluster labels added.
    """
    # Get the embedding matrix
    embedding_matrix = get_embedding_matrix(df)

    # Perform clustering
    kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42).fit(embedding_matrix)

    # Add cluster labels to the DataFrame
    df['cluster'] = kmeans.labels_

    return df
