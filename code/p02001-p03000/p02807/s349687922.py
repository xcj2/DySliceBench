import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

def fact(a,M=mod):
    ans = 1
    for i in range(2,a+1):
        ans = (ans*i)%M
    return ans

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]

def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

N = I()
x = LI()

nfact = fact(N-1)
pn = nfact
cumpn = nfact
ans = nfact*(x[1]-x[0])
for i in range(1,N-1):
    pn -= nfact*mod_inv(i)*mod_inv(i+1)
    pn %= mod
    cumpn += pn
    ans += cumpn*(x[i+1]-x[i])
    ans %= mod

print(ans)