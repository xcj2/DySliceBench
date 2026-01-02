import sys
readline = sys.stdin.readline

P = 998244353
def mod_prod(a,b):
    return (a % P) * (b % P) % P

def mod_fact(a):
    ret = 1
    for i in range(a):
        ret = ret * (i + 1) % P
    return ret

def mod_pow(a, n):
    ret = 1
    while n > 0:
        if n % 2 == 1:
            ret = ret * a % P
        a = a * a % P
        n = n >> 1
    return ret

def mod_div(a, b):
    b_inv = mod_pow(b, P - 2)
    return a * b_inv % P

def mod_comb(a,b):
    ret = 1
    b = min(b, a - b)
    for i in range(b):
        ret *= a - i
        ret %= P
    ret = mod_div(ret, mod_fact(b))
    return ret

def solve():
    A, B, C, D = map(int, readline().split())

    dp = [[0] * D for i in range(C)]

    dp[A - 1][B - 1] = 1

    for i in range(C):
        for j in range(D):
            if i >= A or j >= B:
                dp[i][j] = (
                    (dp[i - 1][j] * (j + 1) if i > 0 else 0)
                    + (dp[i][j - 1] * (i + 1) if j > 0 else 0)
                    - (dp[i - 1][j - 1] * i * j if i > 0 and j > 0 else 0)
                   ) % P
    print(dp[-1][-1])

solve()