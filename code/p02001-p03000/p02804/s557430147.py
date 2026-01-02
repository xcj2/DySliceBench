MOD = 10 ** 9 + 7

def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = MOD
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

def prep(n):
    for i in range(2, n):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)


def main():
    n, k = map(int, input().split())
    A = sorted(map(int, input().split()))
    c = 1
    ma = 0
    prep(n)
    for i, (amax, amin) in enumerate(zip(A[k - 1:], reversed(A[:n - k + 1])), k - 1):
        ma = (ma + cmb(i, k - 1, MOD) * (amax - amin)) % MOD
    print(ma)

main()
