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
    # ord("a") Unicode コードポイントを返す
    codepoint = ord("a")

    def dfs(word, dep):
        if len(word) == N:
            return print(word)

        for i in range(dep):
            dfs(word + chr(codepoint+i), dep)

        dfs(word + chr(codepoint+dep), dep+1)

    dfs("a", 1)


# Solve
if __name__ == "__main__":
    solve()
