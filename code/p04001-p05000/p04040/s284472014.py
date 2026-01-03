"""
fast way to compute a combination using inverse factorials
O(N) to construct tables -> O(1) to compute each combination
"""


def get_fact_and_inv(limit: int, MOD: int) -> tuple:
    """Compute mod tables of factorials and inverse factorials (1-indexed)."""
    factorials = [0] * (limit + 1)
    factorials[0] = 1
    x = 1
    for i in range(1, limit + 1):
        x = (x * i) % MOD
        factorials[i] = x

    inverse_factorials = [1] * (limit + 1)
    inverse_factorials[-1] = pow(factorials[-1], MOD - 2, MOD)
    x = inverse_factorials[-1]
    for i in range(limit - 1, 0, -1):
        x = (x * (i + 1)) % MOD
        inverse_factorials[i] = x
    return factorials, inverse_factorials


def mod_comb(n: int, r: int, MOD: int) -> int:
    """Compute nCr % MOD using a mod table of inverse factorials."""
    return fact[n] * inv[r] * inv[n - r] % MOD


# e.g. ARC058D - いろはちゃんとマス目 / Iroha and a Grid (ABC042D)
def main():
    global fact, inv
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7
    fact, inv = get_fact_and_inv(H + W, MOD)
    x, y, a = H - A - 1, W + A - 2, A - 1  # fixed variables
    f = lambda i: mod_comb(x + i, i, MOD) * mod_comb(y - i, a, MOD) % MOD
    ans = sum(f(i) for i in range(B, W)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
