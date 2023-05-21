"""Test the embeddings functions."""
import pandas as pd
import numpy as np
import pytest
from logic.processing.embeddings import get_embedding, add_embeddings_to_dataframe
from unittest.mock import Mock, patch


def test_get_embedding(mocker):
    # Mock the Embedding.create API call
    mock_response = {
        'data': [
            {"embedding": [0.1, 0.2, 0.3]},
            {"embedding": [0.4, 0.5, 0.6]},
            {"embedding": [0.7, 0.8, 0.9]}
        ]
    }
    mocker.patch('openai.Embedding.create', return_value=mock_response)

    # Call the get_embedding function
    embeddings = get_embedding(["Some text", "some more text", "even more text"])

    # Check the result
    assert embeddings[0] == [0.1, 0.2, 0.3]
    assert embeddings[1] == [0.4, 0.5, 0.6]
    assert embeddings[2] == [0.7, 0.8, 0.9]
    assert len(embeddings) == 3


def test_add_embeddings_to_dataframe(mocker):
    # Define the mock response for the API call
    mock_response = {
        "data": [
            {"embedding": [0.1, 0.2, 0.3]},
            {"embedding": [0.4, 0.5, 0.6]},
            {"embedding": [0.7, 0.8, 0.9]}
        ]
    }

    # Configure the mock to return the response
    mocker.patch('openai.Embedding.create', return_value=mock_response)

    # Create a sample DataFrame
    df = pd.DataFrame({
        "clipping_text": ["text1", "text2", "text3"]
    })

    # Call the function to add embeddings
    result = add_embeddings_to_dataframe(df)

    # Assert that the embeddings were added to the DataFrame correctly
    assert all(np.array_equal(a, b) for a, b in zip(result["embedding"].tolist(), [
        np.array([0.1, 0.2, 0.3]),
        np.array([0.4, 0.5, 0.6]),
        np.array([0.7, 0.8, 0.9])
    ]))

    # Assert that the DataFrame shape remains the same
    assert result.shape == df.shape
