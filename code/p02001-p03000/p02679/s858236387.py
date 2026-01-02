import sys
from collections import defaultdict
readline = sys.stdin.readline

N = int(readline())
AB = [list(map(int, readline().split())) for i in range(N)]

C = [(a,b) for a,b in AB if (a==0 and b==0)]
AB = [(a,b) for a,b in AB if not (a==0 and b==0)]
P = 1000000007
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

def gcd(_a,_b):
    a,b = abs(_a), abs(_b)
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    while a % b != 0:
        a, b = b, a % b
    
    return b

def norm(a,b):
    g = gcd(a,b)
    a,b = a//g, b//g
    if a < 0:
        a,b = -a, -b
    if a == 0 and b < 0:
        b = -b
    return a,b

dic = defaultdict(int)
for a,b in AB:
    a,b = norm(a,b)
    dic[(a,b)] += 1

ans = len(C)
keys = list(dic.keys())

x = 1
for a,b in keys:
    n = dic[(a,b)]
    if n != 0:
        p,q = norm(b, -a)
        m = dic[(p,q)]
        x = x * (mod_pow(2, n) + mod_pow(2, m) - 1)
        x %= P
        dic[(p,q)] = 0
        dic[(a,b)] = 0
x -= 1
ans += x
ans %= P
print(ans)