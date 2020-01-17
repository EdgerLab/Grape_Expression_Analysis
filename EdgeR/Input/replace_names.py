#!/usr/bin/env python3

"""
Replace the gene names. Go from PAC names to GSVIV names
Utilize the gff file to replace. I can find the corresponding GSVIV name from
the Name= identifier present on the mRNA lines. On the mRNA lines there is also
the PAC ID so I should be able to easily match the two
"""

__author__ = "Scott Teresi"

import pandas as pd
input_tsvs = '/home/scott/Documents/Uni/Research/Projects/Grape_RNA_Seq_Expression_Analysis/\
EdgeR/Input/HTSeq_Output/Unmodified/'

input_GFF = '/home/scott/Documents/Uni/Research/Projects/Grape_RNA_Seq_Expression_Analysis/\
EdgeR/Input/HTSeq_Output/Unmodified/Vvinifera_145_gene_exons.gff3'

# Load the data
Seq_724 = pd.read_csv(input_tsvs + '724_Seq.tsv', header='infer', sep='\t')
Seq_802 = pd.read_csv(input_tsvs + '802_Seq.tsv', header='infer', sep='\t')
Seq_809 = pd.read_csv(input_tsvs + '809_Seq.tsv', header='infer', sep='\t')

# Remove extraneous rows from top
Seq_724 = Seq_724.iloc[5:]
Seq_802 = Seq_802.iloc[5:]
Seq_809 = Seq_809.iloc[5:]


col_names = ['Chromosome', 'Software', 'Feature', 'Start', 'Stop', \
             'Score', 'Strand', 'Frame', 'FullName']

col_to_use = ['Feature', 'FullName']

GFF_Data = pd.read_csv(
        input_GFF,
        sep='\t+',
        header=None,
        engine='python',
        names = col_names,
        usecols = col_to_use)

GFF_Data = GFF_Data[GFF_Data.Feature == 'mRNA']  # drop non-mRNA rows

GFF_Data[['PAC_ID', 'GSVIV_ID']] = GFF_Data.FullName.str.split(';Name=', expand=True)
GFF_Data[['Nonsense_1', 'PAC_ID']] = GFF_Data.PAC_ID.str.split('=', expand=True)
GFF_Data[['GSVIV_ID', 'Nonsense_2']] = GFF_Data.GSVIV_ID.str.split(';pacid=',expand=True,n=1)
GFF_Data = GFF_Data.drop(['FullName', 'Nonsense_1', 'Nonsense_2'], axis = 1)

my_dict = dict(zip(GFF_Data.PAC_ID, GFF_Data.GSVIV_ID))
Seq_809.to_csv('Prior.csv')
Seq_809.gene_id = Seq_809.gene_id.replace(to_replace = my_dict, value = None)
Seq_809.to_csv('After.csv')


print(GFF_Data.head())
print(Seq_809.head())
