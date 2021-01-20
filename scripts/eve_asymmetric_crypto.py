# This is Eve's script for intercepting messages on Day 8
import math

# Eve overhears N, E (the public key) and the encrypted message C
N = 1_739_198_341
E = 43

# C is encrypted message
C = 832_962_398


# The key to explain here is that if n is big, this function takes millennia. The only reason Eve can crack
# this message is that we were working with small prime numbers. It's exponential, possibly O(2^(n/2))
# (Doesn't look exponential, but the divide operator is expensive with large numbers too)
def prime_factors(n):
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            return p, n // p


P, Q = prime_factors(N)
print(f"P={P}, Q={Q}")

Z = (P - 1) * (Q - 1)
print(f"Z={Z}")

# We have all the info we need to find the private key, D
D = pow(E, -1, Z)
print(f"D={D}")

M = pow(C, D, N)
print(f"Secret message M = {M}")
