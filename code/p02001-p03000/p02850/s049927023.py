from collections import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfs(u=0,pu=-1,pc=-1):
        c=1
        for i,cu in to[u]:
            if cu==pu:continue
            if c==pc:c+=1
            ans[i]=c
            dfs(cu,u,c)
            c+=1

    to=defaultdict(list)
    n=int(input())
    for i in range(n-1):
        a,b=map(int1,input().split())
        to[a].append([i,b])
        to[b].append([i, a])
    ans=[-1]*(n-1)
    dfs()
    print(max(ans))
    print(*ans,sep="\n")

main()