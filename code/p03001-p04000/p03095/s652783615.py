import collections

mod = 1000000007

def add(a, b):
    return (a + b) % mod

def sub(a, b):
    return (a + mod - b) % mod

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))

def solve():
    N=int(input())
    S=list(input())
    c=collections.Counter(S)
    ans=1
    for k in c.keys():
        ans = mul(ans,c[k]+1)
    return sub(ans,1)

print(solve())
