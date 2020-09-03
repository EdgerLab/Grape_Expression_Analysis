#!/usr/bin/env python3

"""
Calculate gene lengths for each gene from an annotation
"""

__author__ = "Scott Teresi"

import argparse
import os

import numpy as np
import pandas as pd

import sys

from gene_lengths import import_genes
from count_matrix import import_count_matrix


def process(gene_annotation, count_matrix_1):
    ids_and_exon_lengths = import_genes(gene_annotation)
    # ids_and_exon_lengths.to_csv("ids.tsv", sep="\t")
    counts = import_count_matrix(count_matrix_1)
    # counts.to_csv("counts.tsv", sep="\t")

    # print(ids_and_exon_lengths.head())
    # print(counts.head())

    merged_data = pd.merge(ids_and_exon_lengths, counts, on="GSVIV")

    merged_data.drop(columns=["Chromosome", "PAC_ID"], inplace=True)
    merged_data.set_index("GSVIV", inplace=True)
    X = fpkm(merged_data)
    # merged_data.to_csv("merged.tsv", sep="\t")


def fpkm(merge_matrix):
    # PSEUDOCODE
    # denominator = total mapped reads / gene length
    # numerator = number of reads for a specific gene, multiplied by scaling

    lengths = merge_matrix.Total_Exon_Length
    lengths = lengths.to_numpy()
    merge_matrix.drop(columns=["Total_Exon_Length"], inplace=True)
    counts = merge_matrix.to_numpy()
    # -----------------

    N = np.sum(counts, axis=0)
    L = lengths
    C = counts

    normalized = 1e9 * C / (N[np.newaxis, :] * L[:, np.newaxis])
    print(normalized)


def test_fpkm(merge_matrix):
    lengths = merge_matrix.Total_Exon_Length
    merge_matrix.drop(columns=["Total_Exon_Length"], inplace=True)
    total_mapped_reads = merge_matrix.sum()

    numerator = merge_matrix * 1e3 * 1e6

    i = 0
    my_columns = list(numerator)
    for sample in my_columns:
        x = numerator[sample] / (lengths * total_mapped_reads[i])
        print(x)
        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="calculate gene lengths")
    path_main = os.path.abspath(__file__)
    parser.add_argument("genes_input_file", type=str, help="parent path of gene file")
    parser.add_argument("count_matrix_1", type=str, help="parent path of counts file")

    parser.add_argument(
        "--output_dir",
        "-o",
        type=str,
        default=os.path.join(path_main, "../../../../", "Grape_Data/Results"),
        help="parent directory to output results",
    )

    args = parser.parse_args()
    args.genes_input_file = os.path.abspath(args.genes_input_file)
    args.count_matrix_1 = os.path.abspath(args.count_matrix_1)
    args.output_dir = os.path.abspath(args.output_dir)

    process(args.genes_input_file, args.count_matrix_1)
