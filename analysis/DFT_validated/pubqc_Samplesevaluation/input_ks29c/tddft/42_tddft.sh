#!/bin/bash -
#-------------------------------------------------------------------------------
#  SBATCH CONFIG
#-------------------------------------------------------------------------------
## resources
#SBATCH -N1  # nodes
#SBATCH -n4  # tasks (cores)
#SBATCH --ntasks-per-node=4  # how many tasks per node
#SBATCH --mem-per-cpu=4G  # memory required per core
#SBATCH -t 00-08:00  # time (days-hours:minutes)
#
#SBATCH -p Lewis  # partition (which set of nodes to run on)
#SBATCH -o CCqCrCqOrCCO_tddft.out
#SBATCH -J gauss_rcgan
#
module load gaussian/gaussian-16-A.03
echo "### Starting Gaussian ###"
g16 < ./CCqCrCqOrCCO_tddft.com
echo "### All Done ###"

