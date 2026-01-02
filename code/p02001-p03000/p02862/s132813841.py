MAX = 1000000
MOD = 1000000007

fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX


def com_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def com(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def resolve():
    com_init()
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0 or max(X, Y) > min(X, Y) * 2:
        print(0)
        return
    c = (X + Y) // 3
    X -= c
    Y -= c
    print(com(X + Y, X))
    
    
if __name__ == '__main__':
    resolve()