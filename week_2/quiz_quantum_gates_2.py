# %%
from sympy import BlockMatrix, I, Identity, Matrix, Pow, ZeroMatrix, block_collapse, sqrt
from sympy.interactive.printing import init_printing

# %%
init_printing(use_unicode=False)

# %%
# Problem 3
inv_root_2 = Pow(sqrt(2), -1, evaluate=False)

# %%
not_gate = Matrix([[0, 1], [1, 0]])
U1 = BlockMatrix([[Identity(2), ZeroMatrix(2, 2)], [ZeroMatrix(2, 2), not_gate]])
U1

# %%
psi1 = inv_root_2 * BlockMatrix([[Matrix([[1], [0]])], [Matrix([[1], [0]])]])
psi1

# %%
block_collapse(U1 * psi1)

# %%
# Problem 4
phase_gate = Matrix([[1, 0], [0, I]])
U2 = BlockMatrix([[Identity(2), ZeroMatrix(2, 2)], [ZeroMatrix(2, 2), phase_gate]])
U2

# %%
psi2 = inv_root_2 * BlockMatrix([[Matrix([[1], [0]])], [Matrix([[0], [1]])]])
psi2

# %%
block_collapse(U2 * psi2)
