def cmb(n, r, mod):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n%mod

    X = Y = 1
    for i in range(n - r + 1, n + 1):
        X *= i
        X %= mod
    for i in range(1, r + 1):
        Y *= i
        Y %= mod
    return (X * RepeatingSquare(Y, mod - 2, mod)) % mod

def RepeatingSquare(n, p, mod):
    if p == 0:
        return 1
    elif p%2 == 0:
        t = RepeatingSquare(n, p//2, mod)
        return (t * t) % mod
    return n * RepeatingSquare(n, p - 1, mod)

def solve(mod):
    n, a, b = [int(_) for _ in input().split()]
    nb = cmb(n, b, mod)
    na = cmb(n, a, mod)
    return RepeatingSquare(2, n, mod) - 1 - na - nb

if __name__ == '__main__':
    MOD = 10 ** 9 + 7
    print(solve(MOD)%MOD)
