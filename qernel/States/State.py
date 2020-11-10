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


class State():
    """
    Class of a quantum state, either pure or mixed
    """
    def __init__(self, ket=None, dm=None):
        super().__init__() #??? super of what?
        self._dm = None
        self._ket = None



    ##############
    # Properties #
    ##############
    @property
    def ket(self, ket: np.array):
        return self._ket

    @property
    def dens_mat(self, ket: np.array):
        return self._ket

    @property
    def is_pure(self):
        """
        :return: returns a boolean indicating whether the state is pure or not, True if state is pure, false otherwise
        :rtype: boolean
        """
        return false #TODO: implement what tests it for real looking at dm? ket?

    @property
    def is_valid(self):
        """
        :return: returns a boolean indicating whether the state is valid or not, True valid, false otherwise
        :rtype: boolean
        """
        return false  # TODO: implement what tests it for real looking at dm? ket?

