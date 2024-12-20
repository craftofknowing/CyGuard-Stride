import matplotlib.pyplot as plt
#%matplotlib inline

import numpy as np
import re
import pandas as pd
import seaborn as sns
from collections import Counter
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
"""
Split arrays or matrices into random train and test subsets

This function shuffles the data and splits it into a training set and a test set according to a given test size. If ``stratify`` is specified, the values in the ``stratify`` array are used to perform a stratified split. The default is to use a random split.

Parameters
----------
test_size : float or int, default=None
    If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If ``train_size`` is also None, it will be set to 0.25.

train_size : float or int, default=None
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from IPython.display import display
import os

print(os.getcwd())


RANDOM_SEED = 655

