from random import randint

def fisher_yates_shuffle(arr : [object]):
    """ Randomly shuffle an array in place
    """
    for i in range(len(arr)-1, 0, -1):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
