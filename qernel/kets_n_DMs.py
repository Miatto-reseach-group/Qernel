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
from .tensor import *


#############################################
###             Class                     ###
#############################################
class Kets_n_DMs(Tensor):

    #############################################
    ###               Properties              ###
    #############################################
    @property
    @abstractmethod
    def is_pure(self) -> bool:
        """
        Tells whether a Ket/DM or is pure or not
        """
        pass

    @property
    @abstractmethod
    def purity(self) -> float:
        """
        Returns the purity of a Ket/DM
        """
        pass

    @property
    @abstractmethod
    def is_valid_QS(self) -> bool:
        """
        Tells whether a Ket/DM is a valid quantum state
        """
        pass


