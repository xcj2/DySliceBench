import math
import sys
sys.setrecursionlimit(int(10**9))

mod = 10**9 + 7

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def fact(n):
    if n == 1: 
        return 1
    else:
        return (fact(n-1)*n)%mod

def comb(n, k):
    ans = 1
    for i in range(k):
        ans *= (n-i)
        ans //= i+1
    return ans % mod

n, a, b = map(int, input().split())
now = 1
for i in range(a):
    now = (now*(n-i))%mod
cnka = (now * power(math.factorial(a),mod-2) )% mod
for i in range(a,b):
    now = (now*(n-i))%mod
cnkb = (now * power(math.factorial(b),mod-2) )% mod

ans = power(2, n)%mod - cnka - cnkb - 1
print(ans % mod)