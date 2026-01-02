import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

# nの階乗のリスト
def fact(n:int, mod:int) -> list:
    fac = [1,1]
    res = 1
    for i in range(2,n+1):
        res = res*i%mod
        fac.append(res)
    return fac

from bisect import bisect_left
from collections import Counter

MOD = 10**9+7

n,m = li()
a = sorted(list(li()))
b = sorted(list(li()))
aset = set(a)
bset = set(b)

mini = min(a[0], b[0])

ans = 1
for i in range(mini,m*n+1):
    if i in set(a) and i in set(b):
        continue
    
    elif i in set(a):
        idx = bisect_left(b, i)
        ans *= (m-idx)
        ans %= MOD
    
    elif i in set(b):
        idx = bisect_left(a, i)
        ans *= (n-idx)
        ans %= MOD
    
    else:
        idxi = bisect_left(a, i)
        idxj = bisect_left(b, i)
        ans *= ((n-idxi)*(m-idxj) - (m*n-i))
        ans %= MOD
        
fac = fact(mini, MOD)
ans *= fac[mini-1]
ans %= MOD

# 重複判定
db = False
acnt = Counter(a)
bcnt = Counter(b)
for k,v in acnt.items():
    if v > 1:
        db = True
        break
    
for k,v in bcnt.items():
    if v > 1:
        db = True
        break
    
print(0) if db else print(ans)