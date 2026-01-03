from collections import deque
N, M = map(int, input().split())
E1 = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E1[a-1].append((b-1, -c))
    E2[b-1].append((a-1, -c))

def BFS(n, E, i0=0):
    Q = deque([i0])
    D = [-1] * n
    D[i0] = 0
    while Q:
        x = Q.popleft()
        for c, w in E[x]:
            if D[c] == -1:
                D[c] = D[x] + 1
                Q.append(c)
    return D

def bellman_ford(n, E, s=0):
    D = [1<<100] * n
    D[s] = 0
    f = 1
    while f:
        f = 0
        for i in range(n):
            if not B[i]: continue
            for j, c in E[i]:
                if not B[j]: continue
                if D[i] < 1<<100 and D[j] > D[i] + c:
                    D[j] = D[i] + c
                    f = 1
    return D

def bellman_ford_check(n, E, s=0):
    D = [0] * n
    for k in range(n):
        for i in range(n):
            if not B[i]: continue
            for j, c in E[i]:
                if not B[j]: continue
                if D[j] > D[i] + c:
                    D[j] = D[i] + c
                    if k == n-1: return 1
    return 0

B1 = BFS(N, E1, 0)
B2 = BFS(N, E2, N-1)
B = [0 if B1[i] < 0 or B2[i] < 0 else 1 for i in range(N)]

if bellman_ford_check(N, E1):
    print("inf")
else:
    D = bellman_ford(N, E1)
    print(-D[-1])
