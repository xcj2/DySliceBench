# ABC132D - Blue and Red Balls
def get_fact_and_inv(lim: int) -> tuple:
    # compute tables of factorials and inverse factorials (1-idx)
    fact = [1] * (lim + 1)
    x = 1
    for i in range(1, lim + 1):
        x = (x * i) % MOD
        fact[i] = x

    inv = [1] * (lim + 1)
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    x = inv[-1]
    for i in range(lim - 1, 0, -1):
        x = (x * (i + 1)) % MOD
        inv[i] = x
    return fact, inv


def comb(n: int, r: int) -> int:
    # compute nCr (n! / r!(n - r)!)
    return (fact[n] * inv[r] * inv[n - r]) % MOD


def main():
    global MOD, fact, inv
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    fact, inv = get_fact_and_inv(N)
    ans = []
    for i in range(1, K + 1):
        if N - K - i + 1 >= 0:
            x = (comb(N - K + 1, i) * comb(K - 1, i - 1)) % MOD
        else:
            x = 0
        ans.append(x)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()