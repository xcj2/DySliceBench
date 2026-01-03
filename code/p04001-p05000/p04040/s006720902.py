"""
fast way to compute a combination using inverse factorials
O(N) to construct tables -> O(1) to compute each combination
"""


def get_factorials(limit: int, MOD: int) -> list:
    """Compute a mod table of factorials (1-indexed)."""
    factorials = [0] * (limit + 1)
    factorials[0] = 1
    x = 1
    for i in range(1, limit + 1):
        x = (x * i) % MOD
        factorials[i] = x
    return factorials


def mod_comb_with_pow(n: int, k: int, MOD: int) -> int:
    """Compute nCr % MOD using pow()."""
    return fact[n] * pow(fact[k], MOD - 2, MOD) * pow(fact[n - k], MOD - 2, MOD) % MOD


# e.g. ARC058D - いろはちゃんとマス目 / Iroha and a Grid (ABC042D)
def main():
    global fact, inv
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7
    fact = get_factorials(H + W, MOD)
    x, y, a = H - A - 1, W + A - 2, A - 1  # fixed variables
    f = lambda i: mod_comb_with_pow(x + i, i, MOD) * mod_comb_with_pow(y - i, a, MOD)
    ans = sum(f(i) for i in range(B, W)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
