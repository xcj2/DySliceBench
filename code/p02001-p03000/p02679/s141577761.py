import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from math import gcd
from collections import defaultdict


n = readint()

mod = 1000000007

d = defaultdict(int)

for i in range(n):
    a,b = readints()
    g = gcd(a,b)
    if g!=0:
        a//=g
        b//=g
    if a<0:
        a*=-1
        b*=-1
    elif a==0 and b<0:
        b*=-1
    d[(a,b)]+=1

ans = 1
k = tuple(d.keys())
ans2 = 0
for x in k:
    if x[0]>0:
        if x[1]>0:
            ans *= pow(2,d[x],mod)+pow(2,d[(x[1],-x[0])],mod)-1
        elif x[1]<0:
            if d[(-x[1],x[0])]==0:
                ans *= pow(2, d[x], mod)
        else:
            ans *= pow(2,d[x],mod)+pow(2,d[(x[1],x[0])],mod)-1
    else:
        if x[1]==0:
            ans2 += d[x]
        else:
            if d[(x[1], x[0])] == 0:
                ans *= pow(2, d[x], mod)
    ans %= mod

print((ans+ans2+mod-1)%mod)




