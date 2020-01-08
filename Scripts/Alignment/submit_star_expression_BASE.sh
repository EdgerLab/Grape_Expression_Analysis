#!/bin/bash -login
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=50G
#SBATCH --job-name STAR_index_Teresi
#SBATCH -o %j.out
#SBATCH -e %j.err


# -------------------------------
# Load Modules
module purge
module load GCC/7.3.0-2.30
module load OpenMPI/3.1.1
module load Perl
module load Java
module load Trimmomatic
module load STAR

# -------------------------------
# Commands:

# Declare output directory:
# 	This is the master output folder
# 	star_expression_analysis.sh will make subdirectories in master output
#cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Output_Files/

# Submit:
# 	Path for shell script to submit
# 	This is what is submitted to SLURM
/mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Scripts/Alignment/star_expression_analysis.sh FILE1 FILE2 NAME
