"""Test the t-SNE visualisation functions."""

import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from visualisation.t_sne import get_tsne_projection, add_tsne_projection


# Test get_tsne_projection
def test_get_tsne_projection():
    # Example DataFrame
    df = pd.DataFrame({
        'embedding': [
            np.array([0.1, 0.2, 0.3]),
            np.array([0.4, 0.5, 0.6]),
            np.array([0.7, 0.8, 0.9]),
            np.array([0.1, 0.2, 0.3]),
            np.array([0.4, 0.5, 0.6]),
            np.array([0.7, 0.8, 0.9])
        ]
    })

    # Call the function
    result = get_tsne_projection(df, number_of_components=2, perplexity=2)

    # Check the result
    assert isinstance(result, np.ndarray)
    assert result.shape == (6, 2)


# Test add_tsne_projection
def test_add_tsne_projection():
    # Example DataFrame
    df = pd.DataFrame({
        'embedding': [
            np.array([0.1, 0.2, 0.3]),
            np.array([0.4, 0.5, 0.6]),
            np.array([0.7, 0.8, 0.9])
        ]
    })

    # Call the function
    result = add_tsne_projection(df, number_of_components=2, perplexity=2)

    # Check the result
    assert 'tsne_0' in result.columns
    assert 'tsne_1' in result.columns
    assert result.shape[1] == 3

