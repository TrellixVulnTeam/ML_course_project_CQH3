import glob, os
import pickle
import numpy as np
import matplotlib.pyplot as plt


def unpickle(file_path):
    """ Function from documentation
    see: https://www.cs.toronto.edu/~kriz/cifar.html
    return:
        d: dictionary containing the data
    """
    with open(file_path, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


def get_data(filename):
    # each row is a RVB img : [32x32 entries, 32x32, 32x32]
    print(f'file {filename} processed')
    batch = unpickle(filename)
    return batch[b'data'], batch[b'labels']

    
