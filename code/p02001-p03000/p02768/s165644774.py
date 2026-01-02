def pow2(n, mod):
    p = 2
    r = 1
    while n:
        if n % 2:
            r = r * p % mod
        p = (p * p) % mod
        n //= 2
    return r

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

def nCr(n, r, mod):
    t = 1
    r = min(r, n - r)
    for i in range(n - r + 1, n + 1):
        t = t * i % mod
    return t * g2[r] % mod



def prep(n, mod):
    for i in range(2, n):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

def main():
    n, a, b = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    prep(2 * (10 ** 5) + 1, mod)
    print((pow2(n, mod) - 1 - nCr(n, a, mod) - nCr(n, b, mod))% mod)


main()
