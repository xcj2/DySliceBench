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
    if num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

N,M = II()
if M>0:
    L,R,D = Line(M,3)
else:
    print('Yes')
    exit()

pt = edges_to_pt(L,R,N)
label,group = scc(N,pt,pt)

x = []
used = [False]*label
for i in range(N):
    if not used[group[i]]:
        x.append(i)
        used[group[i]] = True

pt_l = [[] for _ in range(N)]
for i in range(M):
    pt_l[L[i]-1].append((R[i]-1,D[i]))
    pt_l[R[i]-1].append((L[i]-1,-D[i]))

check_visited = [False]*N
l = [None]*N 
for v in x:
    check_visited[v] = True
    l[v] = 0
    S = [v]
    while S:
        v1 = S.pop()
        for i in pt_l[v1]:
            if check_visited[i[0]] == False:
                check_visited[i[0]] = True
                l[i[0]] = l[v1] + i[1]
                S.append(i[0])
            else:
                if l[i[0]] == l[v1] + i[1]:
                    continue
                else:
                    print('No')
                    exit()

print('Yes')