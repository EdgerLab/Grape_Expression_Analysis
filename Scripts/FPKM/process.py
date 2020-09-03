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
from fpkm import calc_fpkm


def process(gene_annotation, count_matrix, selection, output_dir):
    ids_and_exon_lengths = import_genes(gene_annotation)
    counts = import_count_matrix(count_matrix, selection)
    merged_data = pd.merge(ids_and_exon_lengths, counts, on="GSVIV")
    merged_data.drop(columns=["Chromosome", "PAC_ID"], inplace=True)
    merged_data.set_index("GSVIV", inplace=True)
    lengths = merged_data.Total_Exon_Length
    merged_data.drop(columns=["Total_Exon_Length"], inplace=True)

    fpkm_vals = calc_fpkm(merged_data, lengths)
    fpkm_vals = pd.DataFrame(fpkm_vals, columns=merged_data.columns)
    fpkm_vals.set_index(merged_data.index, inplace=True)
    fpkm_vals.to_csv(
        os.path.join(output_dir, str(selection + "_FPKM_Out.tsv")), sep="\t"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="calculate gene lengths")
    path_main = os.path.abspath(__file__)
    parser.add_argument("genes_input_file", type=str, help="parent path of gene file")
    parser.add_argument("count_matrix", type=str, help="parent path of counts file")
    parser.add_argument(
        "selection", type=str, help="type of counts file (specific to grape analyses"
    )

    parser.add_argument(
        "--output_dir",
        "-o",
        type=str,
        default=os.path.join(path_main, "../../../../", "Grape_Data/Results"),
        help="parent directory to output results",
    )

    args = parser.parse_args()
    args.genes_input_file = os.path.abspath(args.genes_input_file)
    args.count_matrix = os.path.abspath(args.count_matrix)
    args.selection = str(args.selection)
    args.output_dir = os.path.abspath(args.output_dir)

    process(args.genes_input_file, args.count_matrix, args.selection, args.output_dir)
