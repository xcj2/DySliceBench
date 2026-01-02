import functools, operator


def read():
    N, A, B = list(map(int, input().strip().split()))
    return N, A, B


table = []

def solve(N, A, B, MOD=10**9+7):
    n = (pow(2, N, MOD) + MOD - 1) % MOD
    a = nCk(N, A, MOD)
    b = nCk(N, B, MOD)
    return (n + MOD + MOD - a - b) % MOD


def factorial(n, MOD=10**9+7):
    return functools.reduce(lambda x, y: (x*y) % MOD, range(1, n+1))



def modinv(n, p):
    """
    逆元のmod pを求める
    """
    if n >= p:
        raise ValueError('p must be larger than n')
    return pow(n, p-2, p)


def nCk(n, k, MOD=10**9+7):
    r = 1
    kmin = min(k, n-k)
    for i in range(1, kmin+1):
        r = (r * modinv(i, MOD)) % MOD
    for i in range(n-kmin+1, n+1):
        r = r * i % MOD
    return r

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
