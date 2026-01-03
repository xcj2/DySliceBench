import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
mod=10**9+7
n=int(input())
l=[0]*(n+1)
for i in range(2,n+1):
    c=Counter(prime_factorize(i)).items()
    for a,b in c:
        l[a]+=b
ans=1
for v in l:
    ans*=(v+1)
    ans=ans%mod
print(ans%mod)