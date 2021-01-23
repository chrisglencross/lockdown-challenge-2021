P = 1000000007  # edit this
Q = 2210070043  # edit this

N = P * Q
print(f"N={N} -- tell Bob this")

Z = (P - 1) * (Q - 1)
print(f"Z={Z}")

print("Pick a different number between 1 and Z")
E = 49979693  # edit this to be a different prime number between 1 and Z
print(f"E={E} (public key)")

D = pow(E, -1, Z)
print(f"D={D} (private key)")

C = 653470184995596571  # edit this - this is the message that Bob sends you
M = pow(C, D, N)
print(f"Secret message M = {M}")
