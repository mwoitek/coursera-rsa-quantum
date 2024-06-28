# %%
from itertools import product

from sympy import Matrix, Pow, eye, latex, simplify
from sympy.interactive.printing import init_printing
from sympy.physics.quantum import TensorProduct

# %%
init_printing(use_unicode=False)

# %%
# Problem 3
vals = [0, 1]
triples = list(product(vals, repeat=3))
triples

# %%
for b1, b2, b3 in triples:
    xor_1 = int(bool(b1) != bool(b2))
    xor_2 = int(bool(xor_1) != bool(b3))
    print(f"{b1}\t{b2}\t{b3}\t{xor_1}\t{xor_2}")

# %%
for b1, b2, b3 in triples:
    xor_1 = int(bool(b1) != bool(b2))
    xor_2 = int(bool(xor_1) != bool(b3))
    print(f"{b1}{b2}{b3} -> {b1}{xor_1}{xor_2}")

# %%
U = Matrix(
    [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
    ]
)
U

# %%
U.adjoint()

# %%
print(latex(U.adjoint()))

# %%
U.inv()

# %%
print(latex(U.inv()))

# %%
assert U.adjoint() == U.inv()

# %%
U_squared = simplify(U * U)
U_squared

# %%
print(latex(U_squared))

# %%
toffoli_gate = Matrix(
    [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]
)
toffoli_gate

# %%
controlled_x_2 = Matrix(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
)
controlled_x_3 = TensorProduct(controlled_x_2, eye(2))
controlled_x_3

# %%
assert controlled_x_3.adjoint() == controlled_x_3.inv()  # pyright: ignore

# %%
print(latex(controlled_x_3))

# %%
# This should return a matrix with all elements equal to zero.
# Maybe I made a mistake, but it seems that this problem is ill-formulated.
# If that's really the case, it wouldn't be the first time.
simplify(U - controlled_x_3 * toffoli_gate)

# %%
print(latex(simplify(U - controlled_x_3 * toffoli_gate)))

# %%
# Problem 5
one_half = Pow(2, -1, evaluate=False)
unif_superpos = one_half * Matrix([[1], [1], [1], [1]])
unif_superpos

# %%
ancillary = Matrix([[1], [0]])
psi = TensorProduct(unif_superpos, ancillary)
psi

# %%
psi_prime = toffoli_gate * psi
psi_prime
