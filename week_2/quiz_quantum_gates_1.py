# %%
from sympy import I, Integer, Matrix, Pow, Symbol, conjugate, cos, eye, pprint, simplify, sin, sqrt
from sympy.interactive.printing import init_printing

# %%
init_printing(use_unicode=False)

# %%
inv_root_2 = Pow(sqrt(2), -1, evaluate=False)
inv_root_2

# %%
hadamard = inv_root_2 * Matrix([[1, 1], [1, -1]])
hadamard

# %%
# Problem 1
ket_0 = Matrix([[1], [0]])
ket_0

# %%
ket_1 = Matrix([[0], [1]])
ket_1

# %%
ket_minus = inv_root_2 * (ket_0 - ket_1)
ket_minus

# %%
simplify(hadamard * ket_minus)

# %%
# Problem 2
u_op = Matrix([[1, 0], [0, I]])
u_op

# %%
assert u_op * ket_0 == ket_0
u_op * ket_0

# %%
assert u_op * ket_1 == I * ket_1
u_op * ket_1

# %%
assert u_op.adjoint() == u_op.inv()
u_op.adjoint()

# %%
# Problem 3
ket_phi = inv_root_2 * (ket_0 + ket_1)
ket_phi

# %%
ket_psi = inv_root_2 * (ket_0 + I * ket_1)
ket_psi

# %%
simplify(hadamard * ket_phi)

# %%
psi_prime = simplify(hadamard * ket_psi)
psi_prime

# %%
c0 = psi_prime[0, 0]
c0

# %%
simplify(conjugate(c0) * c0)

# %%
c1 = psi_prime[1, 0]
c1

# %%
simplify(conjugate(c1) * c1)


# %%
# Problem 4
def identify_unitary(matrices):
    unitary = []
    for matrix in matrices:
        if simplify(matrix * matrix.adjoint()) == eye(2):
            unitary.append(matrix)
    return unitary


# %%
theta = Symbol("theta", real=True)
matrices = [
    inv_root_2 * Matrix([[1, 1], [1, 0]]),
    Matrix([[0, 1], [1, 0]]),
    Matrix([[cos(theta), sin(theta)], [Integer(-1) * sin(theta), cos(theta)]]),
    inv_root_2 * Matrix([[1, 1], [1, -1]]),
    inv_root_2 * Matrix([[I, -I], [1, 1]]),
]

for i, matrix in enumerate(matrices, start=1):
    print(f"Matrix {i}:")
    pprint(matrix)

# %%
unitary = identify_unitary(matrices)
for matrix in unitary:
    assert simplify(matrix * matrix.adjoint()) == eye(2)
    assert simplify(matrix.adjoint() * matrix) == eye(2)
    pprint(matrix)

# %%
# This matrix is not accepted as a correct answer
# So I'll inspect the results
matrix = matrices[-1]
matrix

# %%
assert simplify(matrix * matrix.adjoint()) == eye(2)
matrix.adjoint()

# %%
assert simplify(matrix * matrix.inv()) == eye(2)
matrix.inv()

# %%
assert matrix.adjoint() == matrix.inv()
# This matrix is unitary! The instructor is wrong. This isn't the first time.
