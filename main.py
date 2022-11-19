import math
import random
from Matrix import Matrix

import numpy as np


def DFT(x):
    N = len(x)
    X = [0.0] * N
    for n in range(N):
        for k in range(N):
            X[n] += x[k] * math.e ** (-2j * math.pi * n * k / N)

    return X


def DFT_slow(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def DFT_with_matrix(x):
    x_matrix = Matrix(x)
    N = len(x)
    n = Matrix([[x for x in range(N)]])
    k = n.get_transposed_matrix()
    M = (-2j * math.pi * k * n / N).exp()
    return M * x_matrix


def main():
    x = [random.sample(range(0, 100000), 1024)]
    X = DFT_with_matrix(x)

    pass


if __name__ == "__main__":
    main()
