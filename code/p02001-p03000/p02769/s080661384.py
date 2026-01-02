from itertools import accumulate
import numpy as np
MOD = 10 ** 9 + 7


def cumprod(A, mod=MOD):
    L = len(A)
    Lsq = int(L ** 0.5 + 1)
    A = np.resize(A, Lsq ** 2).reshape((Lsq, Lsq))
    for i in range(1, Lsq):
        A[:, i] *= A[:, i - 1]
        A[:, i] %= mod
    for i in range(1, Lsq):
        A[i] *= A[i - 1][-1]
        A[i] %= mod
    return A.ravel()[:L]


def make_fact_and_inv(U, mod=MOD):
    """
    0~Nまでのサイズ(N+1)の階乗およびその逆元の配列を返す
    """
    tmp = np.arange(U, dtype=np.int64)
    tmp[0] = 1
    fact = cumprod(tmp, mod)
    tmp = np.arange(U, 0, -1, dtype=np.int64)
    tmp[0] = pow(int(fact[-1]), mod - 2, mod)
    inv = cumprod(tmp, mod)[::-1]
    return fact, inv


fact, inv = make_fact_and_inv(2 * 10 ** 5 + 10)


def nCr(n, r, mod=MOD):
    if r < 0 or r > n or n < 0:
        return 0
    return fact[n] * inv[r] % mod * inv[n - r] % mod


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = []
    for i in range(min(N - 1, K) + 1):
        val = nCr(N, i) * nCr(N - 1, i) % MOD
        ans.append(val)

    answer = 0
    while ans:
        answer = (answer + ans.pop()) % MOD
    print(answer)
