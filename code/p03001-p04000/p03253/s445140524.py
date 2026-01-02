import collections as col
import math as ma

MOD = 10**9 + 7
def inv(a): return pow(a, MOD-2, MOD)
def comb(n,r,MOD):
    ans = 1
    for i in range(r): # r-i==0でbreak
        ans *= n-i
        ans *= inv(r-i)
        ans %= MOD
    return ans

def prime(n):
    ans = []
    for i in range(2, int(n**0.5)+1):
        while not n%i: n //= i; ans.append(i)
    if n != 1: ans.append(n)
    return ans

n,m = map(int,input().split())
cnt = col.Counter(prime(m))

ans = 1
for key,val in cnt.items():
    #ans *= comb(val + n-1, n-1)
    ans *= comb(val + n-1, n-1, MOD)
    ans %= MOD
print(ans)

