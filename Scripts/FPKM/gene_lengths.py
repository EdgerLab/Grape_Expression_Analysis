import pandas as pd


def import_genes(genes_input_path, contig_del=False):
    """Import genes file.

    Args:
        input_dir (command line argument) Specify the input directory of the gene
        annotation data, this is the same as the TE annotation directory

        contig_drop (bool): logical whether to drop rows with a contig as the
        chromosome id
    """

    col_names = [
        "Chromosome",
        "Software",
        "Feature",
        "Start",
        "Stop",
        "Score",
        "Strand",
        "Frame",
        "FullName",
    ]

    col_to_use = [
        "Chromosome",
        "Software",
        "Feature",
        "Start",
        "Stop",
        "Strand",
        "FullName",
    ]

    Gene_Data = pd.read_csv(
        genes_input_path,
        sep="\t+",
        header=None,
        engine="python",
        names=col_names,
        usecols=col_to_use,
    )

    Gene_Data = Gene_Data[~Gene_Data.Chromosome.str.contains("#")]
    mRNA = Gene_Data[Gene_Data.Feature == "mRNA"].copy(deep=True)
    exons = Gene_Data[Gene_Data.Feature == "exon"].copy(deep=True)

    mRNA[["Name1", "GSVIV"]] = mRNA.FullName.str.split(";Parent=", expand=True)
    mRNA[["Name2", "Name3"]] = mRNA.Name1.str.split(";pacid=", expand=True)
    mRNA[["PAC_ID", "Name4"]] = mRNA.Name3.str.split(";", expand=True)
    mRNA.drop(
        [
            "FullName",
            "Strand",
            "Name1",
            "Name2",
            "Name3",
            "Name4",
            "Feature",
            "Software",
            "Start",
            "Stop",
        ],
        axis=1,
        inplace=True,
    )

    exons[["Name1", "PAC_ID"]] = exons.FullName.str.split(";pacid=", expand=True)
    exons.drop(
        ["FullName", "Name1", "Feature", "Software", "Strand"], axis=1, inplace=True
    )
    exons["Total_Exon_Length"] = exons["Stop"] - exons["Start"] + 1
    pac_id_exon_sums = exons.groupby(["PAC_ID"]).Total_Exon_Length.sum()
    full_data = pd.merge(mRNA, pac_id_exon_sums, on="PAC_ID")

    return full_data
