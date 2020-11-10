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

#seeding for reproducibility
np.random.seed(42)

#Creating Kets and DMs
a = ([-0.5+0.32j, 0.5+0.89j])
b = ([-0.3+0.32j, 0.2+0.89j, 0.5+21j])

ket_a = Ket(a)
ket_b = Ket(b)

dm_a = DensityMatrix(a)
dm_b = DensityMatrix(b)

#Performing operations
print(ket_a + ket_b)
print(dm_a + dm_b)

