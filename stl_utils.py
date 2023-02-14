import numpy as np
from stl import mesh

# Creates a cube mesh at given coordinates with given scale
def cube_at_coords(x: float, y: float, z: float, scale: float = 0.5) -> mesh.Mesh:

    # Define the 8 vertices of the cube at given coordinates
    vertices = np.array([\
        [x-scale, y-scale, z-scale],
        [x+scale, y-scale, z-scale],
        [x+scale, y+scale, z-scale],
        [x-scale, y+scale, z-scale],
        [x-scale, y-scale, z+scale],
        [x+scale, y-scale, z+scale],
        [x+scale, y+scale, z+scale],
        [x-scale, y+scale, z+scale]])

    # Define the 12 triangles composing the cube
    faces = np.array([\
        [0,3,1],
        [1,3,2],
        [0,4,7],
        [0,7,3],
        [4,5,6],
        [4,6,7],
        [5,1,2],
        [5,2,6],
        [2,3,6],
        [3,7,6],
        [0,1,5],
        [0,5,4]])

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype = mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]

    return cube