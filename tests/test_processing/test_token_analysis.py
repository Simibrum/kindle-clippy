"""Test the token analysis functions."""
import pytest
import pandas as pd
from logic.processing.token_analysis import count_total_tokens, calculate_cost_of_embeddings


def test_count_total_tokens():
    df = pd.DataFrame({
        'clipping_text': [
            'First clipping',
            'Second clipping',
            'Third clipping'
        ]
    })
    assert count_total_tokens(df) == 6  # Randomly assumed token count, will be replaced with actual count


def test_calculate_cost_of_embeddings():
    df = pd.DataFrame({
        'clipping_text': [
            'First clipping',
            'Second clipping',
            'Third clipping'
        ]
    })
    # assert calculate_cost_of_embeddings(df) == pytest.approx(2.4e-06, abs=1e-9)
    assert calculate_cost_of_embeddings(df) == '$0.01'
