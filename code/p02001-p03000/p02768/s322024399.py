import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     


def power_func(a,n,p):
  bi=str(format(n,"b"))#2進表現に
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

comb = [0 for _ in range(2*10**5 + 2)]
comb[0] = 1

for i in range(2*10**5+1):
    comb[i]

def NCMMod(n, a):
    cur = n
    for i in range(2, a+1):
        cur = cur * (n-i+1) // i
    return cur % mod


fac = [-1] * (10**7+1)
finv = [-1] * (10**7+1)
inv = [-1] * (10**7+1)

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
initNCMMod(2*10**5 + 1)

def main():
    n, a, b = LI()
    comb[1] = n
    n_pow = power_func(2, n, mod)
    for i in range(2, 2*10**5+1):
        comb[i] = comb[i-1] * (n-i+1) * inv[i] % mod
    ans = n_pow - 1
    ans %= mod
    ans = ans - comb[a] - comb[b]
    ans %= mod
    print(ans)

main()

