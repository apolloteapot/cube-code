import numpy as np
from stl import mesh
from PIL import Image
import random
from stl_utils import cube_at_coords

# Convert binary image to 2d array
im = Image.open('image.png')
pixels = [1 if pixel < 128 else 0 for pixel in im.getdata()]
pixels = np.array(pixels).reshape((im.size[1], im.size[0]))
pixels = np.rot90(pixels, 2)
print(pixels.shape)

# Generate the coordinates of each voxel of the image before scattering
coords: list[np.ndarray] = []

for y, z in np.ndindex((pixels.shape[0], pixels.shape[1])):
    if pixels[y, z]:
        coords.append(np.array([0, y, z]))

# Define the observation point for scattering
obs_p = np.array([400, pixels.shape[0] / 2, pixels.shape[1] / 2])

# Scatter each voxel of the scattered image randomly and save to a list of meshes
meshes: list[mesh.Mesh] = []

def p_on_param_eq(p0: np.ndarray, p1: np.ndarray, t: float):
    return p0 + (p1 - p0) * t

for coord in coords:
    t = round(random.uniform(1.0, 2.5), 2)
    new_coord = p_on_param_eq(obs_p, coord, t)
    meshes.append(cube_at_coords(*new_coord, scale = 0.5 * t))

# Generate and save .stl model
mesh.Mesh(np.concatenate([m.data for m in meshes])).save('web/cubes-2.stl')