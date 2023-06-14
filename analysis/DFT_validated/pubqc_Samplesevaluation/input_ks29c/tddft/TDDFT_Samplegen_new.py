#import pybel
#from pybel import *
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from openbabel import *
from openbabel.pybel import *
import openbabel.pybel as pybel
import openbabel
import os
import ntpath
import re


for filename in os.listdir('./'):
    if filename.endswith(".csv"):
        samples = ntpath.basename(filename)
        print (samples)

samples_smiles = pd.read_csv(samples)
print (samples_smiles.head())

for ii, smiles in enumerate(samples_smiles['SMILES']):
    mol = pybel.readstring("smi", smiles)
    print (mol)
    mol.make3D()
    p_counter = 0
    for kk, char in enumerate (smiles):
        s = smiles.replace("=","d")
        s = s.replace("#","t")
        s = s.replace("(","q")
        s = s.replace(")","r")
    f = open("{}_tddft.com".format(s), "w")    
    f.write("%chk={}.chk\n".format(s))
    f.write("%NProcShared=20\n")
    f.write("# opt freq b3lyp/6-31+g(2df,p) Geom=AllCheckpoint TD(NStates=10)\n")
    f.write("\n")
    f.write("Title Card Required")
    f.write("\n")
    ff = open("{}_tddft.sh".format(ii+1),'w')
    ff.write("#!/bin/bash -\n")
    ff.write("#-------------------------------------------------------------------------------\n")
    ff.write("#  SBATCH CONFIG\n")
    ff.write("#-------------------------------------------------------------------------------\n")
    ff.write("## resources\n")
    ff.write("#SBATCH -N1  # nodes\n")
    ff.write("#SBATCH -n4  # tasks (cores)\n")
    ff.write("#SBATCH --ntasks-per-node=4  # how many tasks per node\n")
    ff.write("#SBATCH --mem-per-cpu=4G  # memory required per core\n")
    ff.write("#SBATCH -t 00-08:00  # time (days-hours:minutes)\n")
    ff.write("#\n")
    ff.write("#SBATCH -p Lewis  # partition (which set of nodes to run on)\n")
    ff.write("#SBATCH -o {}_tddft.out\n".format(s))
    ff.write("#SBATCH -J gauss_rcgan\n")
    ff.write("#\n")
    ff.write("module load gaussian/gaussian-16-A.03\n")
    ff.write('echo "### Starting Gaussian ###"\n')
    ff.write("g16 < ./{}_tddft.com\n".format(s))
    ff.write('echo "### All Done ###"\n')
    ff.write("\n")
