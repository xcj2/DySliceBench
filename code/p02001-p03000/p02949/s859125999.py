from collections import deque
N, M, P = map(int, input().split())
E1 = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E1[a-1].append((b-1, P-c))
    E2[b-1].append((a-1, P-c))

def BFS(n, E, i0=0):
    Q = deque([i0])
    D = [-1] * n
    D[i0] = 0
    while Q:
        x = Q.popleft()
        for c, d in E[x]:
            if D[c] == -1:
                D[c] = D[x] + 1
                Q.append(c)
    return D

def bellman_ford_chk(n, E, s=0):
    D = [0] * n
    for k in range(n):
        for i in range(n):
            for j, c in E[i]:
                if D[j] > D[i] + c:
                    D[j] = D[i] + c
                    if k == n-1: return 1
    return 0
def bellman_ford_calc(n, E, s=0):
    D = [1<<100] * n
    D[s] = 0
    f = 1
    while f:
        f = 0
        for i in range(n):
            for j, c in E[i]:
                if D[i] < 1<<100 and D[j] > D[i] + c:
                    D[j] = D[i] + c
                    f = 1
    return D
D1 = BFS(N, E1, 0)
D2 = BFS(N, E2, N-1)
L = [i for i in range(N) if D1[i] >= 0 and D2[i] >= 0]

NN = len(L)
LL = [-1] * N
for i in range(NN):
    LL[L[i]] = i

E3 = [[(LL[a], c) for a, c in E1[i] if LL[a] >= 0] for i in range(N) if LL[i] >= 0]
if bellman_ford_chk(NN, E3, 0):
    print(-1)
else:
    print(max(-bellman_ford_calc(NN, E3, 0)[-1], 0))