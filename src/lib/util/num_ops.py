############################################################
###############  Toolkit for Numeric Operations  ###########
############################################################
import numpy as np
from collections import Counter
import statistics 
from scipy.stats import pearsonr

def mode(arr):
    """return mode of the array
    Args:
        arr: 

    Return: 
    """
    try:
        return statistics.mode(arr)
    except:
        c = Counter(arr)
        return c.most_common(1)[0][0]

def max_index(arr):
    """return the index item that have the max value 
    Args:
        arr: 

    Return: 
    """
    return max((v, k) for (k, v) in enumerate(arr))[1]

def correlation_two_vec(v1, v2):
    """return the pearson correlation value of two vectors
    Args:
        v1: 
        v2: 

    Return: 
    """
    return pearsonr(v1, v2)[0]
