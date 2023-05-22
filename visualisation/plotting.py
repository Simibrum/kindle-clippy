"""Plotting functions."""

import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.cm as cm
import pandas as pd
from visualisation.clustering import add_cluster_labels
from visualisation.t_sne import add_tsne_projection


def add_and_plot_clusters(df: pd.DataFrame, number_of_clusters: int = 10) -> pd.DataFrame:
    """Add cluster labels to a DataFrame and plot the clusters.

    Args:
        df: The DataFrame containing the embeddings.
        number_of_clusters: The number of clusters to use. Default is 10.

    Returns:
        The DataFrame with cluster labels added.
    """
    df = add_cluster_labels(df, number_of_clusters)
    df = add_tsne_projection(df)
    plot_clusters_with_matplotlib(df)
    return df


def plot_clusters_with_matplotlib(df: pd.DataFrame) -> None:
    """Plot the clusters using matplotlib.

    Args:
        df: The DataFrame containing the embeddings.

    Returns:
        None.
    """
    x = df.tsne_0
    y = df.tsne_1
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, c=df.cluster, alpha=0.3)
    plt.title("Clusters in Clippings using t-SNE")
    plt.savefig(f'cluster_plot.png')
    return None


def plot_clusters_with_plotly(df: pd.DataFrame) -> None:
    """Plot the clusters using plotly.

    Args:
        df: The DataFrame containing the embeddings.

    Returns:
        None.
    """
    fig = px.scatter(df, x="tsne_0", y="tsne_1", color="cluster", hover_data=['book', 'clipping_text'])
    fig.update_layout(
        xaxis_title='t-SNE Component 0',
        yaxis_title='t-SNE Component 1',
        title='Book Clusters t-SNE Projection'
    )
    fig.show()
    return None
