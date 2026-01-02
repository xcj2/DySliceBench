MAX = 2100
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
    N, K = map(int, input().split())
    R = N - K

    for i in range(K):
        print(com(K-1, i) * com(R+1, i+1) % MOD)
        

if __name__ == "__main__":
    resolve()