#!/Users/zheng/anaconda/bin/python

import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series 
import matplotlib.pyplot as pyplot 


# read data to DataFrame
colName = ['day','mpid','gl','numItem','num','queued','gms']
data = pd.read_csv('/Users/zheng/pig/conv_volume.csv', names = colName, parse_dates = [0] )

# data clean
# remove zero item
data = data[data.numItem > 0]

# remove old day's data
data = data[data.day > '2015-04-22']

bb = data.groupby(['day'])['num','queued','gms'].sum()
