MOD = 10 ** 9 + 7


def solveBrute(K, S):
    # On the i-th iteration, dp[j] counts all strings of length i which contains S[:j] as a subsequence

    N = len(S)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N + K):
        nextDp = [0] * (N + 1)
        for j in range(N):
            nextDp[j] += dp[j] * 25
            nextDp[j + 1] += dp[j]
        nextDp[N] += dp[N] * 26

        dp = nextDp
        for j in range(N + 1):
            dp[j] %= MOD
        # print(dp)

    return dp[N]


def solveBrute2(K, S):
    import numpy as np

    def matrixPower(mat, k):
        assert k >= 0
        if k == 0:
            return np.eye(mat.shape[0], dtype=np.int64)
        if k == 1:
            return mat
        temp = matrixPower(mat, k // 2)
        ret = (temp @ temp) % MOD
        if k % 2:
            return (ret @ mat) % MOD
        return ret

    # For intution, can interpret the bruteforce as a matrix multiplication:
    # {{0, 0, 0, 1}} . MatrixPower[{{25, 0, 0, 0}, {1, 25, 0, 0}, {0, 1, 25, 0}, {0, 0, 1, 26}}, 8] . {{1}, {0}, {0}, {0}}
    # https://www.wolframalpha.com/input/?i=%7B%7B0%2C+0%2C+0%2C+1%7D%7D+.+MatrixPower%5B%7B%7B25%2C+0%2C+0%2C+0%7D%2C+%7B1%2C+25%2C+0%2C+0%7D%2C+%7B0%2C+1%2C+25%2C+0%7D%2C+%7B0%2C+0%2C+1%2C+26%7D%7D%2C+8%5D+.+%7B%7B1%7D%2C+%7B0%7D%2C+%7B0%7D%2C+%7B0%7D%7D

    N = len(S)

    mat = 25 * np.eye(N + 1, dtype=np.int64,)
    mat[N][N] += 1
    for i in range(N):
        mat[i + 1][i] = 1

    vec = np.zeros((N + 1, 1), dtype=np.int64)
    vec[0] = 1

    res = matrixPower(mat, N + K) @ vec
    return int(res[N]) % MOD


def solve(K, S):
    def modInverse(a, p):
        # Fermat's little theorem, a**(p-1) = 1 mod p
        return pow(a, p - 2, p)

    # Precompute all factorials
    fact = [1]
    for i in range(1, 2 * (10 ** 6) + 1):
        fact.append((fact[-1] * i) % MOD)

    def nCr(n, r, p=MOD):
        # Modulo binomial coefficients
        return (fact[n] * modInverse(fact[r], p) * modInverse(fact[n - r], p)) % p

    total = 0
    N = len(S)
    for i in range(N, N + K + 1):
        total += nCr(N + K, i) * pow(25, N + K - i, MOD)
        total %= MOD
    return total


(K,) = [int(x) for x in input().split()]
S = input()
ans = solve(K, S)
# assert ans == solveBrute(K, S) == solveBrute2(K, S)
print(ans)
