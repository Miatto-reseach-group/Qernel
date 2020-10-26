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
from abc import ABC
from typing import Union, List, Optional
from numbers import Number

from rich import print # cooler print
import numpy as np


class BaseState(ABC):
    """
    Abstract class of a quantum state
    """
    # _ket: Optional[np.array]
    # _dm: Optional[np.array]

    def __init__(self):
        super().__init__()
        self._isPure = None
        self._dm = None
        self._ket = None

    @property
    def ket(self, ket:np.array):
        return self._ket

    
    
    ############
    # Properties
    ############
    @property
    def isPure(self) -> bool:
        raise NotImplementedError('`isPure` not yet implemented')

    @property
    def ket(self) -> np.array:
        raise NotImplementedError('`ket` not yet implemented')

    @property
    def dm(self) -> np.array:
        raise NotImplementedError('`dm` not yet implemented')

    @property
    def purity(self) -> float:
        raise NotImplementedError('`purity` not yet implemented')

    @property
    def num_subsystems(self) -> int:
        raise NotImplementedError('`num_subsystems` not yet implemented')

    @property
    def dimensions(self) -> List[int]:
        raise NotImplementedError('`dimensions` not yet implemented')
    
    ##########
    # Methods
    ##########

    def trace(self, subsystems:list = []) -> Union(Number, BaseState):
        raise NotImplementedError('`trace()` not yet implemented')

    ################
    # Dunder methods
    ################

    def __add__(self, other:BaseState) -> BaseState:
        raise NotImplementedError('you should implement __add__ to compute superpositions or convex sums')

    def __mul__(self, other:Union[Number, BaseState]) -> Union[Number, BaseState]:
        raise NotImplementedError('you should implement __mul__ and __rmul__ to multiply by scalars')

    def __array__(self) -> np.array:
        if self.isPure:
            return self.ket
        else:
            return self.dm



class BaseTransformation(ABC):
    def __init__(self):
        super().__init__()

    @property
    def isUnitary(self):
        raise NotImplementedError('')

    @property
    def generator(self):
        raise NotImplementedError('')

    def __mul__(self, other):
        raise NotImplementedError('')

    def __rmul__(self, other):
        raise NotImplementedError('')

    def __call__(self, *args):
        raise NotImplementedError('')

    

class BaseMeasurement(ABC):
    def __init__(self):
        super().__init__()

    @property
    def isProjective(self):
        raise NotImplementedError('')

    @property
    def basis(self):
        raise NotImplementedError('')

    def outcome_probabilities(self, state: BaseState):
        raise NotImplementedError('')

    def measure(self, state: BaseState):
        raise NotImplementedError('')

    
