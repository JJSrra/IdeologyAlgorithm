#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J IA-30-4

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o IA-exp-30-4.dat

# Redirect error stream to this file.
#SBATCH -e IA-exp-30-4-err.dat

#_______________________________________________________________________________

# IA Experiments
python3 ~/IA/IAbenchmark30-4.py
