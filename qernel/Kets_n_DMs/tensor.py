import numpy as np

class Tensor:
    def __init__(self, tensor: np.array):
        self._array = tensor

    def __array__(self):
        return self._array