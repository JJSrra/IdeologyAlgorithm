#!/bin/bash
#
# The name of the job, can be whatever makes sense to you
#SBATCH -J param-est-IA

# The job should be placed into the queue 'larga'.
#SBATCH -p larga

# Redirect output stream to this file.
#SBATCH -o param-est-IA.dat

# Redirect error stream to this file.
#SBATCH -e param-est-IA-err.dat

#_______________________________________________________________________________

# IA Parameter Estimation
python3 IA/IAparameters.py
