import os
import glob
import pandas as pd
import numpy as np


def hartree_to_ev(x):
    return (x*27.2113825435)

def read_csv_concat(path='./'):
	csv_files = glob.glob(os.path.join(path, "*.csv"))
	data_gen = pd.DataFrame({})
	for f in csv_files:
	    # read the csv file
	    df = pd.read_csv(f)
	    data_gen = pd.concat((data_gen, df), axis=0)
	    # print the location and filename
	    #print('Location:', f)
	    print('File Name:', f.split("\\")[-1])
	return (data_gen)
	
def NormalizeData(data, min_data, max_data):
    
    return (data - min_data) / (max_data - min_data)
