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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

#強連結成分分解
#label：グループ数
#group[i]：i個目のノードが所属するグループ
def scc(N, G, RG):
    used = [False]*N
    group = [None]*N
    order = []
    def dfs(S):
        i_order = []
        temp_order = []
        level = 0
        while S:
            v1 = S.pop()
            if used[v1[0]]:
                continue
            if v1[1]<level:
                for _ in range(len(temp_order)-v1[1]):
                    x = temp_order.pop()
                    i_order.append(x)
                level = v1[1]
            level += 1
            if not used[v1[0]]:
                for v1_to in G[v1[0]]:
                    if not used[v1_to]:
                        S.append((v1_to,level))
                temp_order.append(v1[0])
                used[v1[0]] = True
        for t in reversed(temp_order):
            i_order.append(t)
        return i_order
    for i in range(N):
        if not used[i]:
            i_order = dfs([(i,0)])
            order += i_order
    def rdfs(S,col):
        used[S[0]] = True
        while S:
            v1 = S.pop()
            for v1_to in RG[v1]:
                if not used[v1_to]:
                    used[v1_to] = True
                    S.append(v1_to)
            group[v1] = col
    used = [False]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs([s], label)
            label += 1
    return label, group

N,M = II()
X,Y,Z = Line(M,3)
 
graph = [[] for _ in range(N)]
for i in range(M):
    graph[X[i]-1].append(Y[i]-1)
    graph[Y[i]-1].append(X[i]-1)
    
label,group = scc(N,graph,graph)
print(label)