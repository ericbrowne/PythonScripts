## Eric Browne
## University of Denver
## Masters in Data Science
## Python Functions that might be useful

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



###   Functions   ###

''' Z Normalize'''
def z_normalize(x):
    m= x.mean()
    std = x.std(ddof = 0)
    return (x-m)/std

'''iterate over groupby object'''
def iter_group(group_df):
    for name, sub_df in group_df:
        print(name, '\n', sub_df)
