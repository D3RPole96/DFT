import math
from Matrix import Matrix


def DFT(x: list[float]) -> list[complex]:
    x_matrix = Matrix([x])
    N = len(x)
    n = Matrix([[x for x in range(N)]])
    k = n.get_transposed_matrix()
    M = (-2j * math.pi * k * n / N).exp()

    return (M * x_matrix.get_transposed_matrix()).get_transposed_matrix().matrix[0]


def IDFT(X: list[complex]) -> list[float]:
    X_matrix = Matrix([X])
    N = len(X)
    n = Matrix([[X for X in range(N)]])
    k = n.get_transposed_matrix()
    M = (1 / N) * (2j * math.pi * k * n / N).exp()

    return (M * X_matrix.get_transposed_matrix()).get_transposed_matrix().matrix[0]
