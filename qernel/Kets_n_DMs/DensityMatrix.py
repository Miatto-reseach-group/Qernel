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


#############################################
###             Class                     ###
#############################################
class DensityMatrix():

    #############################################
    ###             Dunder Methods            ###
    #############################################
    def __init__(self, dm: np.array):
        super().__init__()
        self._dm = dm

    def __hash__(self) -> int: #TODO strenghten this hash function! How can we improve it?
        return hash((self._dm.shape[0], np.sum(self._dm)))

    def __str__(self) -> str:
        return 'DM: ' + np.array_str(self._dm)

    def __repr__(self):
            return {'dm': np.array_str(self._dm)}

    def __add__(self, other: Ket) -> DensityMatrix:
        pass

    def __sub__(self, other: Ket) -> DensityMatrix:
        pass

    def __mul__(self, scalar: numeric) -> DensityMatrix:
        pass

    def __rmul__(self, scalar: numeric) -> DensityMatrix:
        pass

    def __truediv__(self, scalar: numeric) -> DensityMatrix:
        pass

    def __pow__(self, scalar: numeric) -> DensityMatrix: #TODO fix it, what goes wrong?!
        pass

    def __eq__(self, other: DensityMatrix, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
        """
        Determines whether two density matrices are equal up to numerical precision
        :param self: the current ket
        :type self: DensityMatrix
        :param other: the ket to be compared with
        :type other: DensityMatrix
        :param rtol: numpy's relative tolerance
        :type rtol: float
        :param atol: numpy's absolute tolerance
        :type atol: float
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: DensityMatrix
        """
        return np.allclose(self._dm, other._dm, rtol=rtol, atol=atol)

    #############################################
    ###               Properties              ###
    #############################################
    @property
    def is_pure(self) -> bool:
        """
        Tells whether a DensityMatrix is pure or not
        :return: a boolean telling whether the ket is pure or not
        """
        pass

    @property
    def purity(self) -> float:
        """
        Returns the purity of a densityMatrix
        :return: a float representing the purity of the ket
        """
        pass

    @property
    def is_valid_QS(self) -> bool:
        """
        Tells whether a DensityMatrix is a valid quantum state by checking whether
         it is normalised or no
        :return: a boolean telling whether the ket is pure or not
        """
        return self.__eq__(self.normalise())

    @property
    def array (self) -> np.array:
        return self._dm

    @property
    def shape (self): #TODO what's the type of shape, a tuple of how many ints?!
        return self._ket.dm


    #############################################
    ###               Methods                 ###
    #############################################
    def normalise(self) -> DensityMatrix:
        """
        Returns the normalised DensityMatrix, now a valid quantum state
        :return: the normalised Ket
        """
        pass

    def complex_conjugate(self) -> DensityMatrix:
        """
        Performs the complex conjugate on DensityMatrix
        :return: complet conjugate of DensityMatrix
        """
        return pass

    def conjugate_transpose(self) -> DensityMatrix:
        """
        Performs conjugate transpose on the DensityMatrix, turning it into a bra
        :return: conjugate transpose of input DensityMatrix, a.k.a. a Bra
        """
        pass

    def inner_prod(self, other: DensityMatrix) -> numeric:
        """
        Performs inner product (dot product) on two DensityMatrices
        :return: a scalar resulting from the inner product of the two DensityMatrices
        """
        pass


