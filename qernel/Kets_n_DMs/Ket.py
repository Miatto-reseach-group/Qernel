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

    ###########
    # Imports #
    ###########
from __future__ import annotations
import numpy as np

class Ket():

    def __init__(self, ket: np.array):
        super().__init__()
        self._ket = ket

    def __str__(self):
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
        :rtype: State
        """
        return np.add(self._ket, other._ket)

    def __sub__(self, other: Ket) -> Ket:
        """
        Superposes two kets
        :param self: the current ket
        :type self: Ket
        :param other: the ket to be superposed to the current one
        :type other: Ket
        :return: a ket obtained by element-wise substraction, not normalised!
        :rtype: State
        """
        return np.subtract(self._ket, other._ket)

    def __mul__(self, scalar: numeric) -> Ket:
        """
        Superposes two kets
        :param self: the current ket
        :type self: Ket
        :param scalar: the ket to be superposed to the current one
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not normalised!
        :rtype: State
        """
        return self._ket * scalar

    def __rmul__(self, scalar: numeric) -> Ket:
        """
        Superposes two kets
        :param self: the current ket
        :type self: Ket
        :param scalar: the ket to be superposed to the current one
        :type scalar: numeric
        :return: a ket obtained by element-wise scalar multiplication, not normalised!
        :rtype: State
        """
        return scalar * self._ket

