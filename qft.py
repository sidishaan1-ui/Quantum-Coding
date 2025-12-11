import numpy as np
from qiskit.visualization import plot_bloch_vector

pi = np.pi
i = 1j

# Hadamard gate
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])


# Convert integer n into a fixed 3-bit binary list
# Example: n = 5 → "101" → [1, 0, 1]
def to_binary_list_fixed(n):
    return [int(b) for b in format(n, f'0{3}b')]


# Convert each binary digit into a 2×1 computational basis vector:
#   0 → |0> → [[1], [0]]
#   1 → |1> → [[0], [1]]
# This prepares the qubits as actual column vectors.

def change_to_matrix(list_input):
    list_output = []
    for i in list_input:
        if i == 0:
            y = np.array([[1],
                          [0]])
        else:
            y = np.array([[0],
                          [1]])
        list_output.append(y)
    return list_output    


# Controlled phase rotation R_k applied to target qubit.
# Inputs: integer 0 or 1, 2×1 vector of the target qubit, rotation index
# R_k gate:
#     R_k = diag(1, exp(2πi / 2^k))
# Only applies if the control qubit is |1>.

def apply_controlled_rotation(binary_of_control_vec, target_vec, k):
    phase = np.exp(2j * np.pi / (2**k))
    U = np.array([[1, 0], 
                  [0, phase]])
    if binary_of_control_vec == 1:     # control = |1>
        return U @ target_vec
    else:
        return target_vec              # no operation if control = |0>


# Apply the Hadamard gate to each qubit vector
def apply_hadamard_to_list(list):
    for i in range (len(list)):
        list[i] = H @ list[i]
    return list


# Manual test for unitarity: U†U = I
def test_if_unitary(matrix):
    #Take conjugate transpose of given gate
    conjt_matrix = matrix.conj().T

    # Returns U†U
    identity = conjt_matrix @ matrix
    return identity

# ========================= QFT on 3 Qubits (No Swaps) ===================
# 
# Qubit order used here:
#     q2 = Most Significant Bit
#     q1 = Middle Bit
#     q0 = Least Significant Bit
#
# QFT Circuit Structure (no final swap network):
#
#        ┌───┐         ┌────────┐           ┌────────┐
# q2: ───┤ H ├────■────┤ R1(c=q1) ├────■────┤ R2(c=q0) ├────────
#        └───┘    │    └────────┘      │    └────────┘
#                 │                    │
#        ┌───┐    │        ┌────────┐  │
# q1: ───┤ H ├────■────────┤ R1(c=q0)├───────────────
#        └───┘    │        └────────┘
#                 │
#        ┌───┐    │
# q0: ───┤ H ├────■────────────────────────────────────
#        └───┘
# ========================================================================
# Keyboard input of basis state to transform
# ========================================================================

a = int(input("Enter basis state of system: "))

# Convert integer to binary list
binaryinputs = to_binary_list_fixed(a)
print("Binary:", binaryinputs)

# Convert each binary digit into a 2×1 qubit vector
matrixbinaryinputs = change_to_matrix(binaryinputs)

# Apply Hadamards to q2, q1, q0
matrixbinaryinputs = apply_hadamard_to_list(matrixbinaryinputs)
print(matrixbinaryinputs)

# ------------------------------------------------------------------------
# Follow above circuit

# R1 on the most significant qubit, controlled by q1
matrixbinaryinputs[0] = apply_controlled_rotation(binaryinputs[1], matrixbinaryinputs[0], 1)
print("After R1 on matrixbinaryinputs[0]:\n", matrixbinaryinputs[0])

# R2 on the most significant qubit, controlled by q0
matrixbinaryinputs[0] = apply_controlled_rotation(binaryinputs[2], matrixbinaryinputs[0], 2)
print("After R2 on matrixbinaryinputs[0]:\n", matrixbinaryinputs[0])

# R1 on the middle qubit, controlled by q0
matrixbinaryinputs[1] = apply_controlled_rotation(binaryinputs[2], matrixbinaryinputs[1], 1)
print("After R1 on matrixbinaryinputs[1]:\n", matrixbinaryinputs[1])

# Print the final 3-qubit state (still separable because this is not full QFT)
print()
for i in matrixbinaryinputs:
    print(i)

# Test unitarity of gates

#Each controlled rotation gate
for k in range(3):
    phase = np.exp(2j * np.pi / (2**k))
    U = np.array([[1, 0], 
                  [0, phase]])
    print(test_if_unitary(U))

# Hadamard — will show numerical error ≈ 10^-17
print(test_if_unitary(H))