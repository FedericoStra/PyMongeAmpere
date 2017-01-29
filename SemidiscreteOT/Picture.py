# SemidiscreteOT
# Copyright (C) 2017  Federico Stra
# Copyright (C) 2014  Quentin Merigot

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import Image


def to_grayscale(gmat):
    i8 = np.clip(255*data, 0, 255).astype(np.uint8)
    return Image.fromarray(i8)


def to_rgb(rmat, gmat, bmat):
    r8 = np.clip(255*rmat, 0, 255).astype(np.uint8)
    g8 = np.clip(255*gmat, 0, 255).astype(np.uint8)
    b8 = np.clip(255*bmat, 0, 255).astype(np.uint8)
    return Image.fromarray(np.dstack((r8, g8, b8)))

def laguerre_diagram_to_image(dens, Y, w, colors, bbox, ww, hh):
    nc = colors.shape[1]
    A = ma.rasterize_2(dens, Y, w, colors, bbox[0], bbox[1], bbox[2], bbox[3], ww, hh);

    if (nc == 1):
        img = to_grayscale(A[0].T)
        return img
    elif (nc == 3):
        img = to_rgb(A[0].T,A[1].T,A[2].T)
    else:
        raise ValueError("laguerre_diagram_to_image: number of color channels should be 1 or 3")
    return img
