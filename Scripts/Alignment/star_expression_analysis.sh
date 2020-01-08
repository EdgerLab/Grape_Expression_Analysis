#!/bin/bash
# Trimming is done previously! Compartmentalized into a separate step
# In this file we will align to the genome
# $3 is the variable given to us via the perl script.
# We use $3 to get the name of the specific directory we are working on




#for my_dir in 809_Seq 802_Seq 724_Seq
cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files
my_dir="724_Seq"
#do

cd $my_dir
cd $3
mkdir Mapping
cd Mapping


# ---------------------------------------------------
# ALIGN RNA-Seqs TO THE GENOME WITH STAR
#CORE
STAR --runThreadN 12 \
--genomeDir /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files/Index/ \
--readFilesIn /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files/$my_dir/$3/Trimmed/$3.trimmed_P1.fq /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files/$my_dir/$3/Trimmed/$3.trimmed_P2.fq
#--readFilesCommand zcat # Anything following is an extra option



#done








# EXTRA OPTIONS from Beth
#--seedSearchStartLmax 30 \ # look up these values
#--outFilterScoreMinOverLread 0 \ # different from standard, check out
#--outFilterMatchNminOverLread 0 \ # different from standard, check out
#--outFilterMatchNmin 20 \ # different from standard, check out
#--runThreadN 12


