import numpy as np

pi = np.pi
i = 1j

H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])


def to_binary_list_fixed(n):
    return [int(b) for b in format(n, f'0{3}b')]


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

def apply_controlled_rotation(binary_of_control_vec, target_vec, k):
    """
    control_vec: 2x1 vector for control qubit
    target_vec:  2x1 vector for target qubit
    k: rotation degree R_k
    """
    phase = np.exp(2j * np.pi / (2**k))
    U = np.array([[1, 0], 
                  [0, phase]])
    #If control_vec is 1:
    if binary_of_control_vec == 1:
        return U @ target_vec
    else:
        return target_vec

def apply_hadamard_to_list(list):
    for i in range (len(list)):
        list[i] = H @ list[i]
    return list

def test_if_unitary(matrix):
    matrix_dagger = matrix
    matrix[0][1], matrix[1][0] = matrix_dagger[1][0], matrix_dagger[0][1]
    matrix_dagger = matrix_dagger.conj()
    identity = matrix_dagger @ matrix
    return identity
    
#-----------------------------------------------------------------------------------------------------
# ========================= QFT on 3 Qubits (No Swaps) =========================
# 
# Qubit order: q2 = Most Significant Bit, q1 = middle, q0 = Least Significant Bit
#
#        ┌───┐         ┌────────┐           ┌────────┐
# q2: ───┤ H ├────■────┤ R2(c=q1) ├────■────┤ R2(c=q0) ├────────
#        └───┘    │    └────────┘      │    └────────┘
#                 │                    │
#        ┌───┐    │        ┌────────┐  │
# q1: ───┤ H ├────■────────┤ R2(c=q0)├───────────────
#        └───┘    │        └────────┘
#                 │
#        ┌───┐    │
# q0: ───┤ H ├────■────────────────────────────────────
#        └───┘
#
# Legend:
#   H        — Hadamard gate
#   Rk       — Phase rotation by 2π / 2^k
#   c=qX     — Controlled by qubit qX
#   ■        — Control point
# ============================================================================

#Get basis state of system
a = int(input("Enter basis state of system: "))

#Represent basis state of system in individual binary states
binaryinputs = to_binary_list_fixed(a)
print("Binary:", binaryinputs)

#Convert basis states to matrixes 
matrixbinaryinputs = change_to_matrix(binaryinputs)

#Apply Hadamard gate to every basis state
matrixbinaryinputs = apply_hadamard_to_list(matrixbinaryinputs)
print(matrixbinaryinputs)

# Apply rotation gate (control q1) to most signifcant digit
matrixbinaryinputs[0] = apply_controlled_rotation(binaryinputs[1], matrixbinaryinputs[0], 1)
print("After R1 on matrixbinaryinputs[0]:\n", matrixbinaryinputs[0])

# Apply rotation gate (control q2) to most signifcant digit
matrixbinaryinputs[0] = apply_controlled_rotation(binaryinputs[2], matrixbinaryinputs[0], 2)
print("After R2 on matrixbinaryinputs[0]:\n", matrixbinaryinputs[0])

# Apply rotation gate (control q2) to middle significant digit
matrixbinaryinputs[1] = apply_controlled_rotation(binaryinputs[2], matrixbinaryinputs[1], 1)
print("After R2 on matrixbinaryinputs[1]:\n", matrixbinaryinputs[1])

print()
for i in matrixbinaryinputs:
    print(i)

#Test if gates used
for k in range(3):
    phase = np.exp(2j * np.pi / (2**k))
    U = np.array([[1, 0], 
                [0, phase]])

    print(test_if_unitary(U))