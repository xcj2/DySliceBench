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

def main():
    n=inp()
    if n%2==0:
        x=( n*(n-1) )//2
        print(x-(n//2))
    else:
        x=( n*(n-1) )//2
        print(x-((n-1)//2))
    for i in range(1,n):
        for j in range(i+1,n+1):
            if n%2==0:
                if i+j!=n+1:
                    print(i,j)
            else:
                if i+j!=n:
                    print(i,j)
    
if __name__ == "__main__":
    main()


