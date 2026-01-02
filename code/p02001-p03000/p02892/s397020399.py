import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()
S = []
for _ in range(N):
    S.append(list(map(int, input())))

pt = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j]==1:
            pt[i].append(j)

def bfs(pt,v):
    used = [[False]*N for _ in range(N)]
    d = [-1]*N
    d[v] = 0
    q = [v]
    c = 1
    while q:
        flag = False
        q1 = []
        for i in q:
            for j in pt[i]:
                if d[j]==-1:
                    used[i][j] = True
                    used[j][i] = True
                    flag = True
                    d[j] = c
                    q1.append(j)
                else:
                    if used[i][j]==False and d[j]!=c:
                        return -float('inf')
                    else:
                        if used[i][j]==False and d[j]==c:
                            used[i][j] = True
                            used[j][i] = True
        q = q1
        if flag:
            c += 1
    return c

ans = -1
for i in range(N):
    x = bfs(pt,i)
    if x>ans:
        ans = x

print(ans)