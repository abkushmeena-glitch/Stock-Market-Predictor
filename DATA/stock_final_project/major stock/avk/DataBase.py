# coding: utf-8

# In[2]:

import sys
import warnings
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"
if not sys.warnoptions:
    warnings.simplefilter('ignore')
#     Adam optimizer
    
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from datetime import timedelta
from tqdm import tqdm
import yfinance as yf




sns.set()
tf.compat.v1.random.set_random_seed(1234)
tf.compat.v1.disable_eager_execution()

start = '2014-01-01'
end = '2023-12-21'
stock = 'GOOG'

df = yf.download(stock, start, end)
df.reset_index(inplace=True)
df.head()
print(df.head())

