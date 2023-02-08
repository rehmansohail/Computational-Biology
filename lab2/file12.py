import numpy as np

def find_central_atom(pdb_file):
    coordinates = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                coordinates.append([x, y, z])
    coordinates = np.array(coordinates)
    center = coordinates.mean(axis=0)
    return center

pdb_file = "codeinput.pdb"
central_atom = find_central_atom(pdb_file)
#the output is the central atom coordinates in the codeinput.pdb file
print(central_atom)