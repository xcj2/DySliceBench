import sys
readline = sys.stdin.readline

N, M, K = map(int, readline().split())
P = 998244353
def mod_prod(a,b):
    return a * b % P

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
        n = n // 2
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

ans = 0
_n = N - 1
for k in range(K + 1):
    a = N - k
    # N-1 Comb k
    if k == 0:
        comb = 1
    elif k == 1:
        comb = _n
    else:
        comb = comb * mod_div((_n - k + 1), k) % P
    b = M * mod_pow(M-1, a-1) % P
    b = b * comb % P
    ans += b
    ans %= P


print(ans)