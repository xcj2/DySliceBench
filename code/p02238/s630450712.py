# -*- coding: utf-8 -*-
import sys
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()


c=0
def main():
    N=int(input())
    edge=[[] for _ in range(N)]
    for i in range(N):
        l=list(map(lambda x:int(x)-1,input().split()))
        for x in l[2:]:
            edge[i].append(x)
    d=[-1]*N
    f=[-1]*N
    used=[False]*N
    def dfs(v):
        global c
        used[v]=True
        d[v]=c
        for nv in edge[v]:
            if not used[nv]:
                c+=1
                dfs(nv)
        c+=1
        f[v]=c
    global c
    while not all(used):
        for i in range(N):
            if not used[i]:
                c+=1
                dfs(i)

    for i in range(N):
        print(i+1,d[i],f[i])
    
                

if __name__ == '__main__':
    main()

