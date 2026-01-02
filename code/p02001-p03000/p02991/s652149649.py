import sys
sys.setrecursionlimit(300000)
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
adj = [list() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda s: int(s) - 1, sys.stdin.readline().split())
    adj[u].append(v)
S, T = map(lambda s: int(s) - 1, sys.stdin.readline().split())

q = deque([(0, S, 0)])
seen = {S}
while len(q) > 0:
    dim, v, cnt = q.popleft()
    if v == T and dim == 0:
        print(cnt // 3)
        exit(0)
    ndim = (dim + 1) % 3
    for nxt in adj[v]:
        if (ndim * N + nxt) not in seen:
            q.append((ndim, nxt, cnt + 1))
            seen.add(ndim * N + nxt)
print(-1)