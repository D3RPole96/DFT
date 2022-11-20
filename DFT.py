import math
import random
from Matrix import Matrix
import matplotlib.pyplot as plt

import numpy as np


def DFT_original(x):
    N = len(x)
    X = [0.0] * N
    for n in range(N):
        for k in range(N):
            X[n] += x[k] * math.e ** (-2j * math.pi * n * k / N)
            print(math.e ** (-2j * math.pi * n * k / N))

    return X


def DFT_trigonometric(x):
    N = len(x)
    X = [0.0] * N
    for n in range(N):
        for k in range(N):
            X[n] += x[k] * (math.cos(2 * math.pi * k * n / N) - 1j * math.sin(2 * math.pi * k * n / N))

    return X


def DFT_numpy(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def DFT(x):
    x_matrix = Matrix(x)
    N = len(x[0])
    n = Matrix([[x for x in range(N)]])
    k = n.get_transposed_matrix()
    M = (-2j * math.pi * k * n / N).exp()
    return (M * x_matrix.get_transposed_matrix()).get_transposed_matrix().matrix[0]
