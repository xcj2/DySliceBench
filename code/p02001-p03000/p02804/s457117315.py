from collections import deque


def read():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return N, K, A

def sample():
    from random import randint
    N, K = 10**5, 10**4
    A = [randint(-10**9, 10**9) for i in range(N)]
    return N, K, A

def nCk_mod_v2_preprocess(n, p=10**9+7):
    f = [0 for i in range(n+1)]  # n!
    invf = [0 for i in range(n+1)]  # (n!)^-1
    f[0] = 1
    f[1] = 1
    invf[0] = 1
    invf[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] * i % p
        invf[i] = pow(f[i], p-2, p)
    return f, invf

def nCk_mod(n, k, f, invf, p=10**9+7):
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return (f[n] * invf[k] % p) * invf[n-k] % p

def solve(N, K, A, MOD=10**9+7):
    A = list(sorted(A, reverse=True))
    qmax = deque()
    qmin = deque()
    f, invf = nCk_mod_v2_preprocess(N, p=MOD)
    for i in range(1, N+1):
        # p = nCr(N-i-1, K-1)
        p = nCk_mod(N-i, K-1, f, invf)
        qmax.append(p * A[i-1] % MOD)
        qmin.append(p * A[N-i] % MOD)
    return (MOD + sum(qmax) - sum(qmin)) % MOD

if __name__ == '__main__':
    inputs = read()
    #inputs = sample()
    print("{}".format(solve(*inputs)))
