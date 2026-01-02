import sys
readline = sys.stdin.readline

n, a, b = map(int, readline().split())
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


ans = mod_pow(2, n) - 1 - mod_comb(n, a) - mod_comb(n, b)
ans %= P
print(ans)