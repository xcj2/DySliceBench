import sys
readline = sys.stdin.readline

n, k = map(int, readline().split())
P = 10**9 + 7

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


if k >= n - 1:
    ans = mod_comb(n + n - 1, n - 1)
    print(ans)
else:
    ans = 0

    a = mod_comb(n, 0)
    b = mod_comb(n - 1, 0)
    ans = a * b % P
    for i in range(1, k + 1):
        a = mod_prod(a, (n - i + 1)) 
        a = mod_div(a, i)
        b = mod_prod(b, (n - 1 - i + 1))
        b = mod_div(b, i)
        ans += a * b % P
        ans %= P
    print(ans)