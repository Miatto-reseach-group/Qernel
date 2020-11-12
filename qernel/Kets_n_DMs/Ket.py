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
class Ket():

    #############################################
    ###             Dunder Methods            ###
    #############################################
    def __init__(self, ket: np.array):
        super().__init__()
        self._ket = ket

    def __hash__(self) -> int: #TODO strenghten this hash function! How can we improve it?
        return hash((self._ket.shape[0], np.sum(self._ket)))

    def __str__(self) -> str:
        return 'Ket: ' + np.array_str(self._ket)

    def __repr__(self):
            return {'ket': np.array_str(self._ket)}

    def __add__(self, other: Ket) -> Ket:
        """
        Superposes two kets
        :param self: the current ket
        :type self: Ket
        :param other: the ket to be superposed to the current one
        :type other: Ket
        :return: a ket obtained by element-wise sum, not normalised!
        :rtype: Ket
        """
        return Ket(np.add(self._ket, other._ket))

    def __sub__(self, other: Ket) -> Ket:
        """
        Superposes two kets
        :param self: the current ket
        :type self: Ket
        :param other: the ket to be superposed to the current one
        :type other: Ket
        :return: a ket obtained by element-wise substraction, not
                normalised!
        :rtype: Ket
        """
        return Ket(np.subtract(self._ket, other._ket))

    def __mul__(self, scalar: numeric) -> Ket:
        """
        Multiplies a ket by a scalar
        :param self: the current ket
        :type self: Ket
        :param scalar: the ket to be superposed to the current one
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: Ket
        """
        return Ket(self._ket * scalar)

    def __rmul__(self, scalar: numeric) -> Ket:
        """
        Multiplies a ket by a scalar
        :param self: the current ket
        :type self: Ket
        :param scalar: scalar combined element-wise with the ket
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: Ket
        """
        return Ket(scalar * self._ket)

    def __truediv__(self, scalar: numeric) -> Ket:
        """
        Divides a ket by a scalar
        :param self: the current ket
        :type self: Ket
        :param scalar: scalar combined element-wise with the ket
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: Ket
        """
        return Ket(self._ket / scalar)

    def __pow__(self, scalar: numeric) -> Ket: #TODO fix it, what goes wrong?!
        """
        Raises a ket to a power
        :param self: the current ket
        :type self: Ket
        :param scalar: scalar combined element-wise with the ket
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: Ket
        """
        return Ket(np.power(self._ket, scalar))

    def __eq__(self, other: Ket, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
        """
        Determines whether two kets are equal up to numerical precision
        :param self: the current ket
        :type self: Ket
        :param other: the ket to be compared with
        :type other: Ket
        :param rtol: numpy's relative tolerance
        :type rtol: float
        :param atol: numpy's absolute tolerance
        :type atol: float
        :return: a ket obtained by element-wise scalar multiplication, not
                normalised!
        :rtype: Ket
        """
        return np.allclose(self._ket, other._ket, rtol=rtol, atol=atol)

    #############################################
    ###               Properties              ###
    #############################################
    @property
    def is_pure(self) -> bool:
        """
        Tells whether a ket is pure or not
        :return: a boolean telling whether the ket is pure or not
        """
        return True

    @property
    def is_valid_QS(self) -> bool:
        """
        Tells whether a ket is a valid quantum state by checking whether
         it is normalised or no
        :return: a boolean telling whether the ket is pure or not
        """
        return self.__eq__(self.normalise())

    @property
    def array (self) -> np.array:
        return self._ket

    @property
    def shape (self): #TODO what's the type of shape, a tuple of how many ints?!
        return self._ket.shape


    #############################################
    ###               Methods                 ###
    #############################################
    def normalise(self) -> Ket:
        return Ket(self._ket / np.linalg.norm(self._ket))



