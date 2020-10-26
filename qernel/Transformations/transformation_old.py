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

from __future__ import annotations
from BaseClasses import BaseTransformation
import numpy as np
from typing import Union, List
from numbers import Number

class Transformation(BaseTransformation):
    
    @classmethod
    def from_unitary(cls, unitary:np.array) -> Transformation:
        """
        Class method to construct a transformation object from its unitary representation.
        Arguments:
            unitary (array): the unitary representation of the transformation (can be a tensor of rank 2N).
        Returns:
        transf (Transformation): a unitary transformation initialized from its unitary matrix representation
        """
        transf = cls.__new__(cls)
        transf.__init__()
        transf._unitary = unitary
        transf._isUnitary = True
        return transf

    def from_choi(cls, choi:np.array) -> Transformation:
        pass

    def __init__(self):
        pass

    def __array__(self):
        if self._isUnitary:
            return self._unitary
    