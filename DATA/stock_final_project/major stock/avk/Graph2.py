# coding: utf-8

# In[1]:


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


# In[3]:


# Plot the closing price with moving averages
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA100'] = df['Close'].rolling(window=100).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()


# Plotting closing price vs MA50 and MA100
plt.figure(figsize=(15, 5))
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['MA50'], label='MA 50')
plt.plot(df['Date'], df['MA100'], label='MA 100')
plt.title('Closing Price vs 50-day and 100-day Moving Averages')
plt.legend()
plt.show()


# In[ ]:




