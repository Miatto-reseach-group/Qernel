#     Copyright (C) 2020 Miatto research group.

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

#############################################
###             Imports                   ###
#############################################
from __future__ import annotations #for returning current Type
from typing import TypeVar, Union
import numpy as np
from abc import ABC, abstractmethod

#TODO: so what type do we return here since we can't instantiate the class!?
class Tensor(ABC):
    def __init__(self, tensor: np.array):
        self._arr = tensor

    def __array__(self) -> np.array:
        return self._arr

    def __hash__(self) -> int: #TODO strenghten this hash function! How can we improve it?
        return hash((self.shape[0], np.sum(self)))

    def __str__(self) -> str:
        return 'Tensor: ' + np.array_str(self._arr)

    def __repr__(self):
            return 'Tensor: ' + np.array_str(self._arr)

    #TODO : do we want to allow sub/add of scalars element-wise? np does
    def __add__(self, other: Tensor) -> np.array:
        """
        sum of two tensors
        """
        return np.add(self, other)

    def __sub__(self, other: Tensor) -> np.array:
        """
        subtraction of two tensors
        """
        return np.subtract(self, other)

    def __mul__(self, scalar: numeric) -> np.array:
        """
        multiplication of tensor by a scalar
        """
        return np.multiply(self, scalar)

    def __rmul__(self, scalar: numeric) -> np.array:
        """
        right multiplication of tensor by a scalar
        """
        return np.multiply(scalar, self)

    def __truediv__(self, scalar: numeric) -> np.array:
        """
        division of tensor by a scalar
        """
        return np.divide(self, scalar)

    def __pow__(self, scalar: numeric) -> np.array: #TODO fix it, what goes wrong?!
        """
        power of tensor by a scalar
        """
        return np.power(self, scalar)

    def __eq__(self, other: Tensor, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
        """
        equality comparison of two tensors
        """
        return np.allclose(self, other, rtol=rtol, atol=atol)

    #############################################
    ###               Methods                 ###
    #############################################

    @property
    @abstractmethod
    def normalise(self) -> Tensor:
        """
        Returns the normalised Ket/DM, now a valid quantum state
        """
        pass

    @property
    def complex_conjugate(self) -> np.array:
        """
        Performs the complex conjugate on Tensor
        """
        return np.conj(self)

    def dagger(self) -> np.array:
        """
        Performs conjugate transpose on the Tensor
        """
        return np.transpose(np.conj(self))

    #TODO check whether this is what we really want
    def inner(self, other: Union[Tensor, numeric]) -> Union[numeric, np.array]:
        """
        Performs inner product (dot product) on:
         ket scalar
         ket ket
         operator operator
        """
        return np.dot(self, other)

    #TODO check whether this is what we really want
    def outer(self, other: Union[Tensor, numeric]) -> Union[numeric, np.array]:
        """
        Performs iouter product (dot product) on:
         ket scalar
         ket ket
         operator operator
        """
        return np.outer(other, self)

