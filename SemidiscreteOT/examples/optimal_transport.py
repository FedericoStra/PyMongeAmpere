# PyMongeAmpere
# Copyright (C) 2014 Quentin Merigot, CNRS
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import SemidiscreteOT as sdot
import numpy as np

# source: uniform measure on the square with sidelength 2
X = np.array([[-1,-1],
              [1, -1],
              [1, 1],
              [-1,1]], dtype=float);
T = sdot.delaunay_2(X, np.zeros(4));
mu = np.ones(4)/4;
dens = sdot.Density_2(X, mu, T);

# target is a random set of points, with random weights
N = 100;
Y = np.random.rand(N, 2)*2 - 1;
nu = 10 + np.random.rand(N);
nu = (dens.mass() / np.sum(nu)) * nu;

# print "mass(nu) = %f" % sum(nu)
# print "mass(mu) = %f" % dens.mass()

# 
w = sdot.optimal_transport_2(dens, Y, nu)

print("The potential is:")
print(w)
