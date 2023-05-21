"""Test the text parsing functions."""
import os
import pandas as pd
import pytest

from logic.processing.text_parsing import (
    parse_clippings_to_dict, dict_to_dataframe, parse_clippings_to_dataframe, read_text_file,
    parse_clippings_file_to_dataframe
)
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


def test_read_text_file(tmp_path):
    # Create a test file with some content
    # file_content = "This is a test file."
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, "test_clipping_file.txt")
    # with open(file_path, "w", encoding="utf-8") as file:
    #    file.write(file_content)

    # Call the read_text_file function
    content = read_text_file(file_path)

    # Check the result
    assert content
    assert isinstance(content, str)
    assert '\ufeff' not in content

    # Test with a new temp file
    file_content = "This is a test file."
    temp_file_path = tmp_path / "test_clipping_file.txt"
    with open(temp_file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    # Call the read_text_file function
    content = read_text_file(str(temp_file_path))

    # Check the result
    assert content
    assert isinstance(content, str)
    assert '\ufeff' not in content
    assert content == file_content


def test_parse_clippings_file_to_dataframe(tmp_path):
    # Test parsing the test clippings file
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, "test_clipping_file.txt")

    # Call the parse_clippings_file_to_dataframe function
    output_df = parse_clippings_file_to_dataframe(file_path)

    # Check the result
    assert isinstance(output_df, pd.DataFrame)
    assert len(output_df) == 5
    assert list(output_df.columns) == ['book', 'author', 'location', 'date_added', 'clipping_text']
    for index, row in output_df.iterrows():
        assert row['book'] == "Flowers For Algernon (S.F. MASTERWORKS)"
        assert row['author'] == "Keyes, Daniel"
        assert len(row['location']) < 20
        assert isinstance(row['clipping_text'], str)
