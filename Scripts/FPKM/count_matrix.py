import pandas as pd


def import_count_matrix(matrix_input_file):
    """

    """
    counts = pd.read_csv(matrix_input_file, sep="\t", header="infer")

    # Only work on the 724 set
    # counts.drop(["X.x", "X.y"], axis=1, inplace=True)
    counts.drop(["X"], axis=1, inplace=True)

    # Remove all the stupid characters from the HTSeq and R transformations
    counts.rename(columns=lambda x: x.rstrip("_Count.count"), inplace=True)
    counts.rename(columns=lambda x: x.rstrip("_Count.count.x"), inplace=True)
    counts.rename(columns=lambda x: x.rstrip("_Count.count.y"), inplace=True)
    counts.rename(columns={"Gene_Name": "GSVIV"}, inplace=True)

    return counts
