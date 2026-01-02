import sys

def f(r, c, fact, revfact, mod):
    return (fact[r + c] * revfact[r] * revfact[c]) % mod

def g(r, c, fact, revfact, mod):
    if r == c == 0: return 1
    elif r == 0: return c + 1
    elif c == 0: return r + 1
    ans = 0
    for i in range(1, c + 2):
        ans += f(r, i, fact, revfact, mod)
        ans %= mod
    return ans

def solve():
    input = sys.stdin.readline
    r1, c1, r2, c2 = map(int, input().split())
    mod = 7 + 10 ** 9
    fact = [1] * (5 + r2 + c2)
    revfact = [1] * (5 + r2 + c2)
    for i in range(1, 5 + r2 + c2): fact[i] = (i * fact[i-1]) % mod
    revfact[4 + r2 + c2] = pow(fact[4 + r2 + c2], mod - 2, mod)
    for i in reversed(range(1, 4 + r2 + c2)): revfact[i] = ((i + 1) * revfact[i + 1]) % mod

    ans = g(r2, c2, fact, revfact, mod) - g(r2, c1 - 1, fact, revfact, mod) - g(r1 - 1, c2, fact, revfact, mod) + g(r1 - 1, c1 - 1, fact, revfact, mod)
    print((ans + mod) % mod)

    return 0

if __name__ == "__main__":
    solve()