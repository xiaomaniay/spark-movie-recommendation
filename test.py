# Pearson correlation calculation
import math
import numpy as np


def PearsonCorrelation(A, B):
    a, b = np.array(A), np.array(B)
    mean_a, mean_b = np.mean(a), np.mean(b)
    dev_a, dev_b = a - mean_a, b - mean_b
    var_a, var_b = np.power(dev_a, 2), np.power(dev_b, 2)

    corr = np.sum(dev_a * dev_b) / np.sqrt(np.multiply(np.sum(var_a), np.sum(var_b)))

    return corr


if __name__ == "__main__":
    A = [0,4,2]
    B = [5,4,1]
    print(PearsonCorrelation(A, B))
