import sys
n, a, b = map(int, input().split())
mod = 10**9 + 7
sys.setrecursionlimit(10**9)

def f(x):
    if x == 0:
        return 1
    elif x % 2 == 0:
        return (f(x // 2) ** 2) % mod
    else:
        return (f(x - 1) * 2) % mod
def comb(n,k,p):
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) %p
    b=factorial(k) %p
    c=factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p
    # 互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    # [x,y]
    return [w[0], w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m

def nCm(a):
    ans = 1
    for i in range(a):
        ans *= n - i
        ans %= mod
    for i in range(1, a+1):
        ans *= mod_inv(i, mod)
        ans %= mod
    return ans

base = f(n)
comb_a = nCm(a)
comb_b = nCm(b)
print((base - comb_a - comb_b - 1) % mod)
