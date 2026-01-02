
def binary(n):
    return bin(n)[2:]


def pow_by_binary_exponentiation(a, x, n):  # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y


N, a, b = map(int, input().split())

mod = 10**9+7
fact = [1]
fact_inv = [1]
for i in range(max(a, b)):
    new_fact = fact[-1]*(i+1) % mod
    fact.append(new_fact)


def mod_comb_k(n, k, mod):
    ret = 1
    for i in range(k):
        ret *= (n-i)
        ret %= mod
    return ret * pow(fact[k], mod-2, mod) % mod


A = pow_by_binary_exponentiation(2, N, mod) - 1

A -= mod_comb_k(N, a, mod)
A -= mod_comb_k(N, b, mod)
print(A % mod)
