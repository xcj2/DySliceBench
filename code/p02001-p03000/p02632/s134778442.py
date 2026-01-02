import sys
input = sys.stdin.readline


def read():
    K = int(input().strip())
    S = input().strip()
    return K, S


def binom_preprocess(n, MOD=10**9+7):
    f = [0 for i in range(n+1)]  # n!
    invf = [0 for i in range(n+1)]  # (n!)^-1
    f[0] = 1
    f[1] = 1
    invf[0] = 1
    invf[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] * i % MOD
    invf[n] = pow(f[n], MOD-2, MOD)
    for i in range(n, 2, -1):
        invf[i-1] = invf[i] * i % MOD
    return f, invf


def binom(n, k, f, invf, MOD=10**9+7):
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return (f[n] * invf[k] % MOD) * invf[n-k] % MOD


def solve(K, S, MOD=10**9+7):
    T = len(S)
    f, invf = binom_preprocess(K+T+1)
    ans = 0
    for i in range(K+1):
        ans += pow(25, i, MOD) * binom(T-1+i, i, f, invf, MOD) * pow(26, K-i, MOD)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
