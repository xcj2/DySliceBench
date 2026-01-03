import sys
from collections import defaultdict
from heapq import *

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    to=defaultdict(list)
    n=int(input())
    for _ in range(n-1):
        a,b,c=MI()
        a,b=a-1,b-1
        to[a].append([b,c])
        to[b].append([a, c])
    q,k=MI()
    k-=1
    dist=[-1]*n
    hp=[]
    heappush(hp,[0,k])
    while hp:
        d,u=heappop(hp)
        if dist[u]!=-1:continue
        dist[u]=d
        for v,c in to[u]:
            if dist[v]!=-1:continue
            heappush(hp,[d+c,v])
    for _ in range(q):
        u,v=MI1()
        print(dist[u]+dist[v])

main()