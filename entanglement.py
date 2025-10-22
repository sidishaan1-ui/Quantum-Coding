import numpy as np

# Single-qubit gates
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])
I = np.identity(2)  # Identity matrix

'''We are going to need an identity matrix to make the Hadamard gate
    work with a 1x4 dimension matrix (tensor product of two qubits).
    This will make the Hadamard gate 4x4 so we can actually apply it
    to the system.'''

# Tensor (Kronecker) product for two qubits
'''I've learned that the Kronecker (or Tensor) product is very useful
     for multi-qubit systems. It combines the two possible combinations
    of one qubit (0,1) with another to create four combinations (00, 01, 10, 11).
    You multiply the first term of matrix A by the first of matrix B,
    the first term of matrix A by the second of matrix B, second.... etc.
'''

H_I = np.kron(H, I)  # Hadamard on first qubit only
'''Order matters! If it was the other way around, than the second qubits would be
    put into superpostion'''
'''A Hadamard gate only needs to be applied to the first qubit because the CNOT gate
    will correlate the two qubits regardless of both of them being in superposition
    or only one. The probabilities of 00 and 11 are 50/50 in both scenarios...'''

# CNOT gate (control = qubit 0, target = qubit 1)
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# Start in |00>
state = np.array([1, 0, 0, 0])  # column vector as 1D array

# Apply H⊗I
after_H = H_I @ state

# Apply CNOT
after_CNOT = CNOT @ after_H

print("After H⊗I:", after_H)
print("After CNOT:", after_CNOT)