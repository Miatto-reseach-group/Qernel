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

import numpy as np
from Ket import *
#from DensityMatrix import *

#seeding for reproducibility
np.random.seed(42)

#Creating Kets and DMs
a = np.array([-0.5+0.32j, 0.1+0.89j, 0.4+0.23j])
b = np.array([-0.3+0.32j, 0.2+0.89j, 0.5+21j])

ket_a = Ket(a)
ket_b = Ket(b)
print('Ket A: ',  ket_a)
print('Ket B: ',  ket_b)


c = ket_a + ket_b
print('Ket A+B: ',  c)

d = ket_a - ket_b
print('Ket A-B: ',  d)

e = ket_a * 2
print('Ket A*2: ',  e)

f = 2.5 * ket_a
print('Ket 2.5*A: ',  f)

g = ket_a / 3
print('Ket A/3: ',  g)

h = ket_a ** 5
print('Ket A**5: ',  h)

print('A == A: ',  ket_a == ket_a)
print('A == B: ',  ket_a == ket_b)
print('A != B: ',  ket_a != ket_b)
print('A != A: ',  ket_a != ket_a)

print('A.array', ket_a.array)
print('A.shape', ket_a.shape)
print("A.normalise.is_pure ", ket_a.normalise().is_pure)
print("A.normalise().is_valid_QS ", ket_a.normalise().is_valid_QS)
print("A.is_valid_QS ", ket_a.is_valid_QS)

tmp_dict = {ket_a : "Yay!"}
print('dict?', tmp_dict[ket_a])

print("A.normalise() ", ket_a.normalise())









"""
dm_a = DensityMatrix(a)
dm_b = DensityMatrix(b)

#Performing operations

#addition
print(ket_a + ket_b) #superposition
print(dm_a + dm_b) #convex sum

#substraction
print(ket_a - ket_b) #superposition
print(dm_a - dm_b) #convex sum


"""