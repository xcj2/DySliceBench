# -*- coding: utf-8 -*-
from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def inpl(): return list(map(int, input().split()))

N, M, P = inpl()
INF = 10**12
G = [[] for _ in range(N)]
E = []
G2 = [[] for _ in range(N)]
rG2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = inpl()
    G[a-1].append([b-1, -c+P])
    G2[a-1].append(b-1)
    rG2[b-1].append(a-1)
    E.append([a-1, b-1, -c+P])


def SCC(G, rG):
    N = len(G)
    def dfs(i):
        nonlocal t, rorder, searched
        searched[i] = True
        for j in G[i]:
            if not searched[j]:
                dfs(j)
        rorder[t] = i
        t += 1

    def rdfs(i):
        nonlocal t, group, g
        group[i] = g
        for j in rG[i]:
            if group[j] == -1:
                rdfs(j)

    t = 0
    rorder = [-1]*N
    searched = [0]*N
    group = [-1]*N

    for i in range(N):
        if not searched[i]:
            dfs(i)
    g = 0
    for i in range(N-1, -1, -1):
        if group[rorder[i]] == -1:
            rdfs(rorder[i])
            g += 1
    return group, g


def belman_ford(V, edges, r):
    "If glaph contains negative cycles then return True"
    D = [INF]*(V)
    D[r] = 0
    if V == 1:
        return False, [0]
    OK = True
    for _ in range(V-1):
        update = False
        for s, t, d in edges:
            if D[t] > D[s] + d:
                D[t] = D[s] + d
                update = True
        if not update:
            OK = False
    return OK, D

group, gsize = SCC(G2, rG2)
groups = [[] for _ in range(gsize)]
for i in range(N):
    groups[group[i]].append(i)

score = [10**12 for _ in range(N)]
negative_groups = [0]*N


for g in range(gsize):
    ggs = set(groups[g])
    s = groups[g][0]
    score[s] = 0
    Q = deque([s])
    while Q:
        p = Q.popleft()
        for q, c in G[p]:
            if not q in ggs:
                continue
            if score[p] + c < score[q]:
                score[q] = score[p] + c
                Q.append(q)
        if score[s] < 0:
            for g in ggs:
                negative_groups[g] = 1
            break

s = 0
Q = deque([s])
reach1 = [0]*N
reach1[0] = 1

while Q:
    p = Q.popleft()
    for q in G2[p]:
        if not reach1[q]:
            reach1[q] = 1
            Q.append(q)

s = N-1
Q = deque([s])
reachN = [0]*N
reachN[-1] = 1

while Q:
    p = Q.popleft()
    for q in rG2[p]:
        if not reachN[q]:
            reachN[q] = 1
            Q.append(q)

NEGATIVE, D = belman_ford(N, E, 0)

if any([reach1[i]&reachN[i]&negative_groups[i] for i in range(N)]) or reach1[-1]==0:
    print(-1)
else:
    print(max(0, -D[-1]))
