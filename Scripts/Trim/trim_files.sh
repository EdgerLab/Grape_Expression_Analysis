#!/bin/bash


# Declare output directory:
# 	This is the master output folder
# 	star_expression_analysis.sh will make subdirectories in master output
cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files/809_Seq/
# 724_Seq
# 802_Seq
# 809_Seq

mkdir $3
cd $3

mkdir Trimmed
cd Trimmed

# Pre-Processing Step of Alignment
java -jar /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Trimmomatic/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 15 -phred33 $1 $2 $3.trimmed_P1.fq $3.trimmed_U1.fq $3.trimmed_P2.fq $3.trimmed_U2.fq ILLUMINACLIP:/mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Trimmomatic/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:1:30:10 SLIDINGWINDOW:10:20 MINLEN:40 HEADCROP:10 AVGQUAL:25
