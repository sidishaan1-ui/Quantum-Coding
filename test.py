import numpy as np


H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

def test_if_unitary(matrix):
    matrix_dagger = matrix
    matrix[0][1], matrix[1][0] = matrix_dagger[1][0], matrix_dagger[0][1]
    matrix_dagger = matrix_dagger.conj()
    identity = matrix_dagger @ matrix
    print(identity)

def test_if_unitary_b(matrix):
    conjt_matrix = matrix.conj().T
    identity = conjt_matrix @ matrix
    return identity
test_if_unitary(H)
print(test_if_unitary_b(H))