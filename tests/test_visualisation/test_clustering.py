"""Test the clustering functions."""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from visualisation.clustering import add_cluster_labels, get_embedding_matrix


# Test get_embedding_matrix
def test_get_embedding_matrix():
    # Example DataFrame
    df = pd.DataFrame({
        'embedding': [
            np.array([0.1, 0.2, 0.3]),
            np.array([0.4, 0.5, 0.6]),
            np.array([0.7, 0.8, 0.9])
        ]
    })

    # Expected embedding matrix
    expected_matrix = np.array([
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
        [0.7, 0.8, 0.9]
    ])

    # Call the function
    result = get_embedding_matrix(df)

    # Check the result
    assert np.array_equal(result, expected_matrix)


# Test add_cluster_labels
def test_add_cluster_labels():
    # Example DataFrame
    df = pd.DataFrame({
        'embedding': [
            np.array([0.1, 0.2, 0.3]),
            np.array([0.4, 0.5, 0.6]),
            np.array([0.7, 0.8, 0.9])
        ]
    })

    # Call the function
    result = add_cluster_labels(df, number_of_clusters=2)

    # Check the result
    assert 'cluster' in result.columns
    assert len(result['cluster'].unique()) == 2
