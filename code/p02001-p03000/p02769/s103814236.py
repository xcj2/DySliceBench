g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

def nCr(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod

def prep(n, mod):
    for i in range(2, n):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)


def main():
    n, k = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    prep(10**6, mod)
    a = nCr(n + n - 1, n - 1, mod)
    if k < n:
        t = 0
        for x in range(k + 1):
            t = (t + nCr(n, x, mod) * nCr(n - 1, x, mod)) % mod
        print(t)
    else:
        print(a)
    


main()
