import sys
input = sys.stdin.buffer.readline


def convolve(a, b):
    """配列a, bの畳み込みをNTT(number-theoretical transform)によって計算する。
    res[k] = (sum{i = 0..k} a[i] * b[k - i]) % MOD
    """
    MOD = 998244353
    ROOT = 5

    def ntt(a, inverse=False):
        # バタフライ演算用の配置入れ替え
        for i in range(n):
            j = 0
            for k in range(log_sz):
                j |= (i >> k & 1) << (log_sz - 1 - k)
            if i < j:
                a[i], a[j] = a[j], a[i]

        h = pow(ROOT, (MOD - 1) * pow(n, MOD - 2, MOD) % MOD, MOD)
        if inverse:
            h = pow(h, MOD - 2, MOD)

        # バタフライ演算
        m = 1
        while m < n:
            zeta_pow = 1
            zeta = pow(h, n // (2 * m), MOD)
            for j in range(m):
                for k in range(0, n, 2 * m):
                    s = a[j + k]
                    t = a[j + k + m] * zeta_pow
                    a[j + k] = (s + t) % MOD
                    a[j + k + m] = (s - t) % MOD
                zeta_pow *= zeta
                zeta_pow %= MOD
            m <<= 1

        # 逆変換時には配列のサイズの逆元をかける
        if inverse:
            n_inv = pow(n, MOD - 2, MOD)
            for i in range(n):
                a[i] *= n_inv
                a[i] %= MOD
        return a

    def intt(a):
        return ntt(a, inverse=True)

    n = 1 << (len(a) + len(b) - 1).bit_length()
    log_sz = n.bit_length() - 1
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))

    # in-placeで計算を進めることに注意
    ntt(a), ntt(b)
    for i, val in enumerate(b):
        a[i] *= val
        a[i] %= MOD
    intt(a)

    return a


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


print(*convolve(a, b)[:n + m - 1])