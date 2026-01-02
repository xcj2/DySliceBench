import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfsv(u,pu=-1,d=0):
        dist[u]=d
        for cu in to[u]:
            if cu==pu:continue
            dfsv(cu,u,d+1)

    def dfsu(u,pu=-1,d=0):
        res=dist[u]
        for cu in to[u]:
            if cu==pu:continue
            if dist[cu]>d+1:
                ret=dfsu(cu,u,d+1)
                if ret>res:res=ret
        return res

    to=defaultdict(list)
    n,u,v=MI()
    u,v=u-1,v-1
    for _ in range(n-1):
        a,b=MI1()
        to[a].append(b)
        to[b].append(a)
    dist=[0]*n
    dfsv(v)
    #print(dist)
    print(dfsu(u)-1)




main()