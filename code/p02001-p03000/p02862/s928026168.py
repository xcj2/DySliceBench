from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7

def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a=inp()
        a-=1
        g[i].append(a)
        g[a].append(i)
    return n,g
def graphm():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(m):
        a,b,w=inpm()
        a-=1
        b-=1
        g[a].append((b,w))
        g[b].append((a,w))
    return n,m,g

def dijkstra(s,n,g): # sからの最短距離 頂点数n
    s -= 1
    que = []
    d = [10**15 for _ in range(n)]
    d[s] = 0
    heappush( que,(0,s) )
    while len(que)>0:
        p =  heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in range(len(g[v])):
            edge = g[v][i]
            if d[edge[0]] > d[v] + edge[1]:
                d[edge[0]] = d[v] + edge[1]
                heappush( que,(d[edge[0]] , edge[0]) )
    return d

def combi(x,y):
    a=1
    while x>0:
        a=(a*x)%mod
        x-=1
    z=x-y
    while y>0:
        a=(a*pow(y,mod-2,mod))%mod
        y-=1
    while z>0:
        a=(a*pow(z,mod-2,mod))%mod
        z-=1
    return int(a)
    
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def main():
    x,y=inpm()
    if x<y:
        x,y=y,x
    if x>2*y:
        print(0)
        return
    d=x-y
    n=(x-2*d)*(1/3)
    if n%1!=0:
        print(0)
        return
    n=int(n)
    a=n+d
    b=n    
    
    res = 1
    for i in range(1,a+b+1):
        res = res*i%mod
    for i in range(1,a+1):
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):
        res = res*mod_inv(i,mod)%mod
    print(res)

if __name__ == "__main__":
    main()


