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
from __future__ import annotations
import numpy as np
from .tensor import Tensor
from .kets_n_DMs import Kets_n_DMs


#############################################
###             Class                     ###
#############################################
class Ket(Kets_n_DMs):
    def __init__(self, tensor: np.array):
        super().__init__(tensor)

    def __str__(self) -> str:
        return 'Ket: ' + np.array_str(self._arr)
    #TODO: is it ok to have same for str and repr?
    def __repr__(self):
            return 'Ket: ' + np.array_str(self._arr)

    def __add__(self, other: Tensor) -> Tensor:
        """
        sum of two tensors
        """
        #return super(Ket, self).__add__(other)
        return Ket(super().__add__(other))



    #############################################
    ###               Properties              ###
    #############################################
    @property
    def is_pure(self) -> bool:
        """
        Tells whether a Ket/DM or is pure or not
        """
        True

    @property
    def purity(self) -> float:
        """
        Returns the purity of a Ket/DM
        """
        1.0

    @property
    def is_valid_QS(self) -> bool:
        """
        Tells whether a Ket/DM is a valid quantum state
        """
        return self.__eq__(self.normalise())

    #############################################
    ###               Methods                 ###
    #############################################
    @property
    def normalise(self) -> Ket:
        """
        Returns the normalised Ket/DM, now a valid quantum state
        """
        return Ket(self / np.linalg.norm(self))

    @property
    def complex_conjugate(self) -> Ket:
        """
        Performs the complex conjugate on Tensor
        """
        return Ket(np.conj(self))

    def dagger(self) -> Ket:
        """
        Performs conjugate transpose on the Tensor
        """
        return np.transpose(np.conj(self))

    # TODO check whether this is what we really want
    def inner(self, other: Union[Tensor, numeric]) -> Union[numeric, Tensor]:
        """
        Performs inner product (dot product) on:
         ket scalar
         ket ket
         operator operator
        """
        return np.dot(other, self)

    # TODO check whether this is what we really want
    def outer(self, other: Union[Tensor, numeric]) -> Union[numeric, Tensor]:
        """
        Performs iouter product (dot product) on:
         ket scalar
         ket ket
         operator operator
        """
        return np.outer(other, self)
