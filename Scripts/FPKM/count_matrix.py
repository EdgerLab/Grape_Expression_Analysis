import pandas as pd


def import_count_matrix(matrix_input_file, selection):
    """

    """
    counts = pd.read_csv(matrix_input_file, sep="\t", header="infer")

    if selection == "724":
        counts.drop(["X.x", "X.y"], axis=1, inplace=True)
    elif selection == "809":
        counts.drop(["X"], axis=1, inplace=True)
    else:
        raise ValueError("You did not give appropriate sample grouping")

    # Remove all the stupid characters from the HTSeq and R transformations
    counts.rename(columns=lambda x: x.rstrip("_Count.count"), inplace=True)
    counts.rename(columns=lambda x: x.rstrip("_Count.count.x"), inplace=True)
    counts.rename(columns=lambda x: x.rstrip("_Count.count.y"), inplace=True)
    counts.rename(columns={"Gene_Name": "GSVIV"}, inplace=True)

    return counts
