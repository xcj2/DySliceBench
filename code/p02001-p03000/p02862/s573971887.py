import math
import itertools

def read():
    X, Y = list(map(int, input().strip().split()))
    return X, Y

def init_mod_combinations(MAX=500000, MOD=1000000007):
    fac = [0 for _ in range(MAX)]
    finv = [0 for _ in range(MAX)]
    inv = [0 for _ in range(MAX)]
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return fac, finv, inv

def mod_combinations(n, k, MOD=1000000007):
    fac, finv, inv = init_mod_combinations(MAX=n+1, MOD=MOD)
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD


def solve(X, Y):
    # X = 2p + q, Y = p + 2q
    p = (2 * X - Y) // 3
    q = (2 * Y - X) // 3
    if 2*p+q!=X or p+2*q!=Y:
        # 到達不可能
        return 0
    # p+q 回の移動で到達可能
    # 移動パターンの総数は(p+q)Cp
    return mod_combinations(p+q, p)

if __name__ == '__main__':
    inputs = read()
    output = solve(*inputs)
    print("%d" % output)
