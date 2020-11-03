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
import numpy as np



class Ket():

    def __init__(self, ket: np.array):
        super().__init__()
        self._ket = None

    @classmethod
    def __add__(cls, ket: Ket):
        """
        Superposes two kets
        :param ket: the ket to be superposed to the current one
        :type ket: Ket
        :return: a new State with a ket corresponding to the superposition of the states given as input
        :rtype: State
        """
        return State(np.sum(self, ket )) #TODO what about the density matrix of this state?