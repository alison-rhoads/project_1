import numpy as np
import math

volume = 8 #angstroms cubed
number_of_atoms = 100

atoms_cube_root = (number_of_atoms ** (1./3))
volume_cube_root = (volume ** (1./3))
atom_spacing = math.ceil(volume_cube_root / atoms_cube_root)

#create empty 3d array

gasn_box = np.empty((number_of_atoms,number_of_atoms, number_of_atoms)

#create vector representing atom coordinates

atom_vector = np.linspace(0, 2, number_of_atoms)

#repeat and translate the vector and add to 3d array

for length in range(0, 2, atom_spacing):
    shift_vector_horiz = np.roll(atom_vector, atom_spacing, 0)
    gasn_box = np.append(shift_vector_horiz, gasn_box, 0)
for length in range(0, 2, atom_spacing):                                        
    shift_vector_vert = np.roll(atom_vector, atom_spacing, 1)
    gasn_box = np.append(shift_vector_horiz, gasn_box, 1)

#create list with atomic number of atoms in array

atomic_number = [18] * number_of_atoms
