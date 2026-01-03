from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    def dfs(u=0,cnt=1):
        if cnt==n:return 1
        res=0
        for cu in to[u]:
            if vis[cu]:continue
            vis[cu]=True
            res+=dfs(cu,cnt+1)
            vis[cu]=False
        return res

    n,m=MI()
    to=defaultdict(list)
    for _ in range(m):
        a,b=MI1()
        to[a].append(b)
        to[b].append(a)
    vis=[False]*n
    vis[0]=True
    print(dfs())

main()