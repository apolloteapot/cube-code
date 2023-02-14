import numpy as np
from stl import mesh
import qrcode
import random
from stl_utils import cube_at_coords

# Generate the QR Code from the text file
qr = qrcode.QRCode()

with open(f'text.txt', 'r', encoding = 'utf-8') as f:
    qr.add_data(f.read())

qr_matrix = np.array(qr.get_matrix())
size = qr_matrix.shape[0]
print(size)

# Generate the coordinates of each voxel of the QRCode before scattering
coords: list[np.ndarray] = []

for y, z in np.ndindex((size, size)):
    if qr_matrix[y, z]:
        coords.append(np.array([0, y, z]))

# Define the observation point for scattering
obs_p = np.array([100, size / 2, size / 2])

# Scatter each voxel of the scatteredQRCode randomly and save to a list of meshes
meshes: list[mesh.Mesh] = []

def p_on_param_eq(p0: np.ndarray, p1: np.ndarray, t: float):
    return p0 + (p1 - p0) * t

for coord in coords:
    t = round(random.uniform(1.0, 1.5), 2)
    new_coord = p_on_param_eq(obs_p, coord, t)
    meshes.append(cube_at_coords(*new_coord, scale = 0.5 * t))

# Generate and save .stl model
mesh.Mesh(np.concatenate([m.data for m in meshes])).save('web/cubes-1.stl')