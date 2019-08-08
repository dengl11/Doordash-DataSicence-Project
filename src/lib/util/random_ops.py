# random operations
# ----------------------------------------------------------------------------
from operator import itemgetter
import random


def sample_dic(dic, k = 3):
    """return a down-sampled dictionary
    Args:
        dic: 

    Kwargs:
        k: 

    Return: 
    """
    k = min(k, len(dic))
    random_keys = random.sample(dic.keys(), k)
    return {(k, dic[k]) for k in random_keys}

