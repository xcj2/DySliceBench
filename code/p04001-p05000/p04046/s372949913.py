# ARC058D - いろはちゃんとマス目 / Iroha and a Grid (ABC042D)
def get_fact(lim):
    # compute a toble of factorials (1-idx)
    fact = [1] * (lim + 1)
    x = 1
    for i in range(1, lim + 1):
        x = (x * i) % MOD
        fact[i] = x
    return fact


def get_inv(lim):
    # compute a toble of inverse factorials (1-idx)
    inv = [1] * (lim + 1)
    inv[lim] = pow(fact[lim], MOD - 2, MOD)
    x = inv[lim]
    for i in range(lim - 1, 0, -1):
        x = (x * (i + 1)) % MOD
        inv[i] = x
    return inv


def comb(n: int, r: int) -> int:
    # compute nCr (n! / r!(n - r)!)
    return fact[n] * inv[n - r] * inv[r]


def main():
    global MOD, fact, inv
    H, W, A, B = tuple(map(int, input().split()))
    MOD = 10 ** 9 + 7
    fact = get_fact(H + W)
    inv = get_inv(H + W)
    x, y, a = H - A - 1, W + A - 2, A - 1  # fixed variables
    ans = sum(comb(x + i, i) * comb(y - i, a) for i in range(B, W)) % MOD
    print(ans)


if __name__ == "__main__":
    main()