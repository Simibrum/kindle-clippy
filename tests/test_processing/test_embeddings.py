"""Test the embeddings functions."""
import pandas as pd
import pytest
from logic.processing.embeddings import get_embedding, add_embeddings_to_dataframe
from unittest.mock import Mock, patch


def test_get_embedding(mocker):
    # Mock the Embedding.create API call
    mock_response = {
        'data': [
            {
                'embedding': [0.1, 0.2, 0.3]
            }
        ]
    }
    mocker.patch('openai.Embedding.create', return_value=mock_response)

    # Call the get_embedding function
    embedding = get_embedding("Some text")

    # Check the result
    assert embedding == [0.1, 0.2, 0.3]


def test_add_embeddings_to_dataframe(mocker):
    # Create a sample dataframe
    df = pd.DataFrame({
        'text': [
            'First text',
            'Second text',
            'Third text'
        ]
    })

    # Mock the get_embedding function
    mocker.patch('logic.processing.embeddings.get_embedding', return_value=[0.1, 0.2, 0.3])

    # Call the add_embeddings_to_dataframe function
    new_df = add_embeddings_to_dataframe(df, text_column='text', embedding_column='embedding')

    # Check the result
    assert 'embedding' in new_df.columns
    assert new_df['embedding'].tolist() == [[0.1, 0.2, 0.3]] * 3
