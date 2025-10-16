import numpy as np

# Single-qubit gates
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])
I = np.eye(2)  # Identity matrix

# Tensor (Kronecker) product for two qubits
H_I = np.kron(H, I)  # Hadamard on first qubit only

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
