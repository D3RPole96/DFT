from typing import Callable

from DFT import DFT, IDFT
from numpy import allclose

class Function:
    def __init__(self, function: Callable[[float], float], period: float):
        self.dft = None
        self.function = function
        self.period = period

    def __get_values(self, signal_length: int) -> list[float]:
        x = []
        for i in range(signal_length):
            x.append(self.function(self.period / signal_length * i))

        return x

    def get_DFT(self, signal_length: int) -> list[float]:
        x = self.__get_values(signal_length)

        self.dft = DFT(x)
        values = []

        for value in self.dft[:len(self.dft) // 2 + 1]:
            if abs(value.real) > 1e-9:
                values.append(abs(value.real) / (signal_length / 2))
            elif abs(value.imag) > 1e-9:
                values.append(abs(value.imag) / (signal_length / 2))
            else:
                values.append(0)

        return values

    def get_IDFT(self, signal_length: int) -> list[float]:
        if self.dft is None:
            _ = self.get_DFT(signal_length)

        return IDFT(self.dft)
