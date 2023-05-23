"""
In this code, we are following the 
[LSTM by Example using Tensorflow](https://towardsdatascience.com/lstm-by-example-using-tensorflow-feb0c1968537) document.
"""



import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import pad_sequences
