"""Tests for initial functions. We can split these up in later refactoring."""
import pandas as pd
from logic.functions import (
    add_embeddings_to_dataframe,
    run_similarity_query
)


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

