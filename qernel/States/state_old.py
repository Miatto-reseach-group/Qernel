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
from BaseClasses import BaseState
import numpy as np
from typing import Union, Tuple
from numbers import Number

class State(BaseState):

    def __init__(self, ket=None, dm=None):
        super().__init__()
        if ket is not None:
            self._ket = ket
        if dm is not None:
            self._dm = dm

    # numpy representation
    def __array__(self):    
        return self.ket if self.isPure else self.dm

    # multiplication by scalar
    def __mul__(self, number: Number):
        if self.ket is not None:
            return self.__class__.from_ket(self.ket * number)
        elif self.dm is not None:
            return self.__class__.from_density_matrix(self.dm * number)

    def __rmul__(self, number: Number):
        return self.__mul__(number)

    # division by scalar
    def __truediv__(self, number: Number):
        if self.ket is not None:
            return self.__class__.from_ket(self.ket / number)
        elif self.dm is not None:
            return self.__class__.from_density_matrix(self.dm / number)

    # equality comparison
    def __eq__(self, other:State):
        if isinstance(other, State):    
            if self.ket is not None and other.ket is not None:
                return np.allclose(self.ket, other.ket)
            elif self.dm is not None and other.dm is not None:
                return np.allclose(self.dm, other.dm)
        return False

    def __str__(self):
        return f'Purity={self.purity}, num_subsystems={self.num_subsystems}, dimension={self.dimension}'

    @property
    def dimensions(self) -> Tuple[int]:
        if self.isPure:
            return self.ket.shape
        else:
            return self.dm.shape[::2] # assumes out-in index order

    @property
    def num_subsystems(self) -> int:
        return len(self.dimension)

    @property
    def purity(self) -> float:
        if self._isPure:
            return 1.0
        else:
            return np.sum(self.dm * self.dm.T)

    @property
    def isPure(self):
        if self._isPure is None: # remember to reset if state changes
            self._isPure = np.isclose(self.purity, 1.0)
        return self._isPure

    @staticmethod
    def _diagonalize(mat):
        val, vec = np.linalg.eigh(mat)
        return val, vec[..., np.argsort(val)]

    @staticmethod
    def _svd(mat):
        u, s, vh = np.linalg.svd(mat)
        return u, s, vh

    @property
    def ket(self):
        if self._ket is not None:
            return self._ket
        else:
            if self.isPure:
                if self._ket is None:
                    val, vec = self._diagonalize(self.dm)
                    self._ket = vec[-1]
                return self._ket

    @ket.setter
    def ket(self, ket):
        self._ket = ket
        self._isPure = True

    @property
    def dm(self):
        if self._dm is None:
            self._dm = np.tensordot(np.conj(self.ket), self.ket, 0)
            self._dm_decomposed = False
        return self._dm

    # @dm.setter
    # def dm(self, dm):
    #     pass

    @property
    def vectorized(self):
        D = int(np.prod(self.dimension))
        if self.isPure:
            return np.reshape(self, D**2)
        else:
            return np.reshape(self, (D,D))

    @property
    def entanglement(self):
        if self.isPure:
            if self.num_subsystems == 2:
                prob = np.linalg.eigvalsh(self.trace(keep=[0]))
                return -sum(p*np.log2(p) for p in prob if not np.isclose(p,0.0))
            else:
                raise NotImplementedError("didn't implement multipartite entanglement yet")
        else:
            raise NotImplementedError("didn't implement mixed state entanglement yet")

    #########
    # Methods
    #########

    def trace(self, keep:List[int] = []) -> Union[State, Number]:
        if keep == []:
            if self.isPure:
                return np.linalg.norm(self)**2
            else:
                return np.trace(self.vectorized)
        else:
            indices = list(range(2*self.num_subsystems))
            for d in set(range(self.num_subsystems)).difference(keep):
                indices[d + self.num_subsystems] = indices[d]
            return self.from_density_matrix(np.einsum(self.dm, indices))
                
    
    
    