"""Test the text parsing functions."""

import pandas as pd
import pytest

from logic.processing.text_parsing import parse_clippings_to_dict, dict_to_dataframe, parse_clippings_to_dataframe
from tests.test_clipping_data import clipping_samples


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
