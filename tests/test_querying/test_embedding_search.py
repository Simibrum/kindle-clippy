"""Functions to test the embedding search API calls."""

import pandas as pd
import pytest
from logic.querying.embedding_search import run_similarity_query
from unittest.mock import Mock, patch


def test_run_similarity_query(mocker):
    # Create a sample dataframe
    df = pd.DataFrame({
        'text': [
            'First text',
            'Second text',
            'Third text'
        ],
        'embedding': [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
            [0.7, 0.8, 0.9]
        ]
    })

    # Mock the get_embedding function
    mocker.patch('logic.querying.embedding_search.get_embedding', return_value=[0.1, 0.2, 0.3])

    # Call the run_similarity_query function
    result_df = run_similarity_query(
        df, query_text='test_text', embedding_column='embedding', n=10, pprint=False)

    # Check the result
    assert len(result_df) == 3
    assert list(result_df['text']) == ['First text', 'Second text', 'Third text']
    assert list(result_df['embedding']) == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

    with patch('builtins.print') as mock_print:
        # Call the function with pprint=True
        run_similarity_query(
            df, query_text='test_text', embedding_column='embedding', n=10, pprint=True)

        # Assert that the print function was called
        mock_print.assert_called_once()

