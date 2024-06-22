# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Week 1: Programming Assignment
# ## Imports

# %%
import time

# %% [markdown]
# ## Brute-Force with Sieving


# %%
# Check if n is divisible by i. Also keep a counter that checks how many times
# we call this function.
# Important: In your code you must use this function to check divisibility.
def count_calls(f):
    def inner_fun(*args, **kwargs):
        inner_fun.num_calls += 1
        return f(*args, **kwargs)

    inner_fun.num_calls = 0
    return inner_fun


@count_calls
def is_divisible(n, i):
    return n % i == 0


def find_smallest_factor(n):
    # Reset the counter
    is_divisible.num_calls = 0

    # Check divisibility by 2, 3, 5 and 7
    for i in [2, 3, 5, 7]:
        if is_divisible(n, i):
            print(f"Divisible by {i}")
            return i

    # Start search for factors at i = 11
    i = 11

    # Sieve using primes 3, 5, 7
    primes = [3, 5, 7]

    while i < n:
        mod_values = [i % p for p in primes]
        if all(r != 0 for r in mod_values):
            if is_divisible(n, i):
                return i
        i += 2

    # We did not find a factor. n is prime.
    return None


# %%
p = find_smallest_factor(77)
print(f"Number of calls to is_divisible = {is_divisible.num_calls}")
assert p == 7, f"Did not find prime factor 7, instead your algorithm finds {p}"
assert (
    is_divisible.num_calls <= 5
), f"Your algorithm must find a prime factor for 77 using less than 5 divisibility checks"

# %%
p = find_smallest_factor(3589)
print(f"Found prime factor {p}")
print(f"Number of calls to is_divisible = {is_divisible.num_calls}")
assert p == 37, f"Did not find prime factor 37, instead your algorithm finds {p}"
assert (
    is_divisible.num_calls <= 13
), f"Your algorithm must find a prime factor for 3589 with less than 13 divisibility checks"

# %%
n = 7907 * 7607
p = find_smallest_factor(n)
print(f"Found factor = {p}")
print(f"Number of calls to is_divisible = {is_divisible.num_calls}")
assert p == 7607, f"Did not find prime factor 7607, instead your algorithm finds {p}"
assert (
    is_divisible.num_calls <= 1743
), f"Your algorithm must find a prime factor with <= 1743 divisibility checks"

# %%
list_of_semiprimes = [
    1401,
    3748486951520329,
    3752606281089349,
    3754961171936341,
    3756235832941861,
    3758054142736489,
    3768343025255113,
    3770908285338889,
    3789270035360209,
    3792097195306729,
    3804080660868409,
    3809734753698301,
    3816606928381453,
    3818949174736609,
    3820870509943561,
    3822840857074201,
    3852076309133401,
    3876127995012697,
    3892629672990589,
    3910648469842633,
    3920999805125773,
    3921744925134109,
    3924792228588397,
    3931145554413457,
    3932125632305329,
    3935928816760081,
    3961247632016713,
    3975676605218881,
    3982569750752293,
    3982848113442193,
    3985942367371729,
    3986200067461861,
    3990055553157829,
    3993390558390133,
    3997252998788437,
    3998135901643693,
    4005313130491789,
    4024933426550977,
    4036354165122421,
    4038083373106021,
    4053866502851821,
    4067306572005253,
    4078847544271369,
    4091861946912889,
    4099243035596617,
    4133788979088253,
    4134939693320221,
    4142398487623213,
    4144730958670993,
    4148739776756977,
    4179773852763409,
    4185730146333961,
    4190837552528629,
    4194890965293781,
    4244075651161417,
    4254595003500757,
    4299385948797673,
    4301923741074121,
]

# %% [markdown]
# ## Pollard's Rho Algorithm


# %%
def gcd(m, n):
    if m < n:
        m, n = n, m
    while n > 0:
        m, n = n, m % n
    return m


# Use f to generate pseudo random numbers
def f(x, n):
    return (x * x + 1) % n


# %%
# By default try 100,000 numbers
def pseudo_random_gcd_factorization(n, m=100000):
    x = 2
    for _ in range(m):
        d = gcd(x, n)
        if d != 1:
            return d
        x = f(x, n)
    return None


# %%
timeout = 15  # seconds
num_factored = 0

for n in list_of_semiprimes:
    t0 = time.perf_counter()
    p = pseudo_random_gcd_factorization(n)
    if p is not None:
        assert n % p == 0, f"prime factor {p} is incorrect"
        assert p != 1 and p != n, f"factor {p} cannot be trivial"
        print(f"{n} = {p} * {n // p}")
        num_factored += 1
    else:
        print(f"Failed to factor {n}")
    t1 = time.perf_counter()
    timeout -= t1 - t0
    if timeout < 0:
        break

print(f"{num_factored} numbers were factored within 15 seconds")


# %%
# Use g to generate a second pseudo random sequence
def g(x, n):
    return f(f(x, n), n)


# %%
# By default try 100,000 numbers
def pseudo_random_difference_gcd_factorization(n, m=100000):
    x, y = 2, 2
    for _ in range(m):
        x, y = f(x, n), g(y, n)
        diff = x - y if x > y else y - x
        d = gcd(diff, n)
        if d != 1:
            return d
    return None


# %%
timeout = 15  # seconds
num_factored = 0

for n in list_of_semiprimes:
    t0 = time.perf_counter()
    p = pseudo_random_difference_gcd_factorization(n)
    if p is not None:
        assert n % p == 0, f"prime factor {p} is incorrect"
        assert p != 1 and p != n, f"factor {p} cannot be trivial"
        print(f"{n} = {p} * {n // p}")
        num_factored += 1
    else:
        print(f"Failed to factor {n}")
    t1 = time.perf_counter()
    timeout -= t1 - t0
    if timeout < 0:
        break

print(f"{num_factored} numbers were factored within 15 seconds")


# %%
def pollards_rho_factor(n, a=1):
    def f(x):
        return (x * x + a) % n

    x = f(2)
    y = f(f(2))

    while x != y:
        diff = x - y if x > y else y - x
        d = gcd(diff, n)
        if d != 1:
            return d
        x = f(x)
        y = f(f(y))

    print("Failed")
    return None


# %%
timeout = 15  # seconds
num_factored = 0

for n in list_of_semiprimes:
    t0 = time.perf_counter()
    p = pollards_rho_factor(n)
    if p is not None:
        assert n % p == 0, f"prime factor {p} is incorrect"
        assert p != 1 and p != n, f"factor {p} cannot be trivial"
        print(f"{n} = {p} * {n // p}")
        num_factored += 1
    else:
        print(f"Failed to factor {n}")
    t1 = time.perf_counter()
    timeout -= t1 - t0
    if timeout < 0:
        break

print(f"{num_factored} numbers were factored within 15 seconds")
