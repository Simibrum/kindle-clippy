"""Tests for initial functions. We can split these up in later refactoring."""
import pandas as pd
import pytest
from logic.functions import (
    parse_clippings_to_dataframe, calculate_cost_of_embeddings, add_embeddings_to_dataframe,
    run_similarity_query, parse_clippings_to_dict, dict_to_dataframe
)
from test_clipping_data import clipping_samples


@pytest.mark.parametrize('sample_clipping_text, expected_output', clipping_samples)
def test_parse_clippings_to_dict(sample_clipping_text, expected_output):
    # Act
    output_dict = parse_clippings_to_dict(sample_clipping_text)

    # Assert
    assert output_dict == expected_output


@pytest.mark.parametrize('sample_dict', [b for a, b in clipping_samples])
def test_dict_to_dataframe(sample_dict):
    # Act
    output_df = dict_to_dataframe(sample_dict)

    # Assert
    # Check that the output is a DataFrame
    assert isinstance(output_df, pd.DataFrame)

    # Check that the DataFrame has the right shape
    assert output_df.shape[0] == len(sample_dict)
    assert output_df.shape[1] == 5  # We have 5 fields: 'book', 'author', 'location', 'date_added', 'clipping_text'

    # Check that the DataFrame has the right columns
    expected_columns = ['book', 'author', 'location', 'date_added', 'clipping_text']
    assert all([column in output_df.columns for column in expected_columns])


@pytest.mark.parametrize('sample_clipping_text, expected_output', clipping_samples)
def test_parse_clippings_to_dataframe(sample_clipping_text, expected_output):
    # Act
    output_df = parse_clippings_to_dataframe(sample_clipping_text)

    # Assert
    assert isinstance(output_df, pd.DataFrame)
    assert len(output_df) == len(expected_output)
    assert list(output_df.columns) == ['book', 'author', 'location', 'date_added', 'clipping_text']


def test_calculate_cost_of_embeddings():
    """Test for calculating cost of embeddings."""
    # Arrange
    sample_dataframe = pd.DataFrame()  # fill this with a sample dataframe

    # Act
    total_cost = calculate_cost_of_embeddings(sample_dataframe)

    # Assert
    # we expect total cost to be sum of tokens in dataframe clippings
    assert total_cost == sample_dataframe['text_column_name'].apply(lambda x: len(x.split())).sum()


def test_add_embeddings_to_dataframe():
    """Test for adding embeddings to dataframe."""
    # Arrange
    sample_dataframe = pd.DataFrame()  # fill this with a sample dataframe
    mock_openai_api_key = 'test_key'

    # Act
    output_dataframe = add_embeddings_to_dataframe(sample_dataframe, mock_openai_api_key)

    # Assert
    # check that output has an embeddings column
    assert 'embeddings' in output_dataframe.columns


def test_run_similarity_query():
    """Test for running similarity query."""
    # Arrange
    query = 'sample query'
    sample_dataframe = pd.DataFrame()  # fill this with a sample dataframe

    # Act
    output = run_similarity_query(query, sample_dataframe)

    # Assert
    # check that output is within the dataframe
    assert output in sample_dataframe['clippings'].values

