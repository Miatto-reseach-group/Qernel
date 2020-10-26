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

from state import State
import numpy as np

ket = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
pure_dm = np.outer(ket,np.conj(ket))
max_mix = np.array([[0.5,0],[0,0.5]])

def test_pure_ket_returns_ket():
    psi = State(ket = ket)
    assert np.allclose(psi.ket, ket)

def test_mixed_dm_returns_dm():
    psi = State(dm = max_mix)
    assert np.allclose(psi.dm, max_mix)

def test_pure_state_returns_dm():
    psi = State(ket=ket)
    assert np.allclose(psi.dm, np.outer(ket, np.conj(ket)))

def test_pure_dm_returns_ket():
    psi = State(dm = pure_dm)
    assert np.allclose(psi.ket, ket)

def test_mixed_dm_cannot_return_ket():
    psi = State(dm = max_mix)
    assert psi.ket is None



def test_ket_count_subsystems():
    psi = State(ket = np.einsum('a,b,c', ket, ket, ket))
    assert psi.num_subsystems == 3

def test_dm_count_subsystems():
    psi = State(dm = np.einsum('ab,cd,ef', dm, dm, dm))
    assert psi.num_subsystems == 3

def test_pure_dimension():
    psi = State.from_ket(np.einsum('a,b', ket, ket))
    assert psi.dimensions == (2,2)

def test_mixed_dimension():
    psi = State.from_density_matrix(np.einsum('ab,cd', dm, dm))
    assert psi.dimension == [2,2]

def test_multiply_state():
    psi = State.from_ket(ket)
    assert np.allclose(psi*7.2, ket*7.2)
    assert np.allclose(7.2*psi, 7.2*ket)

def test_divide_state():
    psi = State.from_ket(ket)
    assert np.allclose(psi/7.2, ket/7.2)

def test_equality():
    psi1 = State.from_ket(ket)
    psi2 = State.from_ket(ket)
    assert psi1 == psi2

def test_equality_dm():
    psi1 = State.from_density_matrix(dm)
    psi2 = State.from_density_matrix(dm)
    assert psi1 == psi2

def test_equality_ket_dm():
    psi1 = State.from_ket(ket)
    psi2 = State.from_density_matrix(np.outer(np.conj(ket), ket))
    assert psi1 == psi2

def test_trace_dm():
    psi = State.from_density_matrix(dm)
    assert np.isclose((0.5*psi).trace(), 0.5)

def test_trace_ket():
    psi = State.from_ket(ket)
    assert np.isclose((0.5*psi).trace(), 0.25)

def test_entanglement():
    psi = State.from_ket(np.sqrt(0.5)*np.identity(2)) # hack to obtain state |00> + |11> / sqrt(2)
    assert np.isclose(psi.entanglement, 1.0)