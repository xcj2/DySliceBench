import math


def div_with_mod(x, y, mod):
    # Fermat's little theorem
    return x*pow(y, mod - 2, mod)


def comb(n, r, mod):
    # calculates C(n,r) with mod (assuming mod is prime)
    nc = n
    for rc in range(1, r):
        nc -= 1
        n = n*nc % mod
        r = r*rc % mod

    return div_with_mod(n, r, mod)


def solve():
    N = int(input())
    list = [chr(ord("a")+i) for i in range(10)]

    def dfs(w, i):
        if len(w) == N:
            return print(w)

        for j in range(i):
            dfs(w+list[j], i)

        dfs(w + list[i], i + 1)

    dfs("", 0)


# Solve
if __name__ == "__main__":
    solve()
