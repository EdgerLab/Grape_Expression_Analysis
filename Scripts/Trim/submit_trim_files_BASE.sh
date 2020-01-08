#!/bin/bash -login
#SBATCH --time=02:30:00
#SBATCH --cpus-per-task=15
#SBATCH --mem-per-cpu=20G
#SBATCH --job-name Trimmomatic_Teresi
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

# Submit:
# 	Path for shell script to submit
# 	This is what is submitted to SLURM
/mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Scripts/Trim/trim_files.sh FILE1 FILE2 NAME
