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



class DensityMatrix():

    def __init__(self, dm: np.array):
        super().__init__()
        self._dm = None

    @classmethod
    def __add__(cls, dm: DensityMatrix):
        """
        Performs a convex sum on two density matrices.
        :param dm: the density to be added to the current one
        :type dm: DensityMatrix
        :return: a new State with density matrix corresponding to the convex sum of the states given as input
        :rtype: State
        """
        return State(dm = np.sum(self, dm)) #TODO what about the ket of this state?
