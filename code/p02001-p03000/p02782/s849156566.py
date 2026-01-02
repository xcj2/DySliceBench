# F - Many Many Paths
def get_factorials(lim: int, MOD: int) -> list:
    """Compute a table of factorials (1-indexed)."""
    factorials = [1] * (lim + 1)
    x = 1
    for i in range(1, lim + 1):
        x = (x * i) % MOD
        factorials[i] = x
    return factorials


def mod_comb_with_pow(n: int, k: int, MOD: int) -> int:
    """Compute nCr % MOD using pow(), not an inverse factorial table."""
    return fact[n] * pow(fact[k], MOD - 2, MOD) * pow(fact[n - k], MOD - 2, MOD) % MOD


def main():
    global fact
    MOD = 10 ** 9 + 7
    R1, C1, R2, C2 = map(int, input().split())
    fact = get_factorials(2 * 10 ** 6 + 10, MOD)
    f = lambda x, y: mod_comb_with_pow(x, y, MOD)
    ans = (f(C1 + R1, R1) - f(C1 + R2 + 1, R2 + 1) - f(C2 + R1 + 1, R1) + f(C2 + R2 + 2, R2 + 1)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
