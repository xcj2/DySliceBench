n, a, b = map(int, input().split())
m = max(a, b)
mod = 10 ** 9 + 7

def binary(n):
    return bin(n)[2:]

# バイナリ法
def pow_by_binary_exponentiation(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y

ans = pow_by_binary_exponentiation(2, n, mod)
ans -= 1

N = max(a, b)
fact = [1] * (N + 1)

for i in range(N):
    fact[i + 1] = fact[i] * (i + 1) % mod


def comb(r):
    c = n
    for i in range(1, r):
        c = (c * (n - i)) % mod
    c = c * pow_by_binary_exponentiation(fact[r], mod - 2, mod) % mod
    return c

ans = (ans - comb(a)) % mod
ans = (ans - comb(b)) % mod
print(ans)
