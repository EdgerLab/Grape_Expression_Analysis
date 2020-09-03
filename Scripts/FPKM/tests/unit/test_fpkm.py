#!/usr/bin/env python3

"""
Unit test fpkm.py
"""

__author__ = "Scott Teresi"

import pytest

import numpy as np
import pandas as pd
import os

from Scripts.FPKM.fpkm import calc_fpkm


@pytest.fixture
def count_matrix():
    """Default count_matrix object."""
    data = pd.read_csv(
        "Test_CountData.tsv", sep="\t", header="infer", index_col="Gene_Name"
    )
    return data


@pytest.fixture
def lengths():
    """Default lengths object."""
    data = pd.read_csv(
        "Test_Lengths.tsv", sep="\t", header="infer", index_col="Gene_Name"
    )
    return data.Total_Exon_Length


@pytest.fixture
def expected_test_vals():
    """Expected test values"""
    data = pd.read_csv(
        "Test_ExpectedValues.tsv", sep="\t", header="infer", index_col="Gene_Name"
    )
    return data.round(3)


def test_load_data(count_matrix, lengths, expected_test_vals):
    output_vals = calc_fpkm(count_matrix, lengths)
    output_vals = pd.DataFrame(output_vals, columns=count_matrix.columns)
    output_vals = output_vals.round(3)
    output_vals.set_index(count_matrix.index, inplace=True)
    output_vals = output_vals.to_numpy()
    expected_test_vals = expected_test_vals.to_numpy()

    assert np.all(output_vals == expected_test_vals)


if __name__ == "__main__":
    pytest.main(["-s", __file__])  # for convenience
