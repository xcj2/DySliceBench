import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfs(u,pu=-1,pc=-1):
        c=0
        for cu in to[u]:
            if cu==pu:continue
            c+=1
            if c==pc:c+=1
            ei=etoi[(u,cu)]
            e_color[ei]=c
            dfs(cu,u,c)

    to=defaultdict(list)
    n=int(input())
    etoi={}
    for i in range(n-1):
        a,b=map(int1,input().split())
        to[a].append(b)
        to[b].append(a)
        etoi[(a,b)]=etoi[(b,a)]=i
    #print(etoi)
    e_color=[-1]*(n-1)
    max_deg_u=max(to.items(),key=lambda x:len(x[1]))[0]
    dfs(max_deg_u)
    print(max(e_color))
    print(*e_color,sep="\n")

main()