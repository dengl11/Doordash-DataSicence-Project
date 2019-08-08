import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

boston = datasets.load_boston()
X, y = shuffle(boston.data, boston.target, random_state=13)
print(X)
