"""Tests for initial functions. We can split these up in later refactoring."""
import pandas as pd
from logic.functions import (
    parse_clippings_to_dataframe, calculate_cost_of_embeddings, add_embeddings_to_dataframe,
    run_similarity_query
)


def test_parse_clippings_to_dataframe():
    """Test for converting clippings text to dataframe."""
    sample_clipping_text = ""  # fill this with an example from your clippings file
    expected_output = {}  # fill this with what you expect the output dataframe row to look like

    # Act
    output_dataframe = parse_clippings_to_dataframe(sample_clipping_text)

    # Assert
    assert output_dataframe.equals(expected_output)


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


