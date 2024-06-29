# %%
from math import gcd


# %%
def mod_exp(b: int, e: int, m: int) -> int:
    result = 1
    for _ in range(e):
        result = (b * result) % m
    return result


# %%
def find_order(b: int, m: int) -> int | None:
    for e in range(1, m):
        if mod_exp(b, e, m) == 1:
            return e
    return None


# %%
# Problem 1
find_order(7, 15)

# %%
# Problem 2
mod_exp(7, 10, 55)

# %%
s = (mod_exp(7, 10, 55) + 1) % 55
s

# %%
gcd(55, s)
