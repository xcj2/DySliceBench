import sys
from collections import defaultdict, deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, X, Y = MI()

aaa = [None] * (N + 1)
for v0 in range(1, N + 1):
    dx = [0] * N
    seen = set()
    seen.add(v0)
    q = deque()
    q.append((v0, -1, 0))
    while len(q) > 0:
        v, p, dist = q.popleft()

        dx[v - 1] = dist
        next = []
        if v > 1: next.append(v - 1)
        if v < N: next.append(v + 1)
        if v == X: next.append(Y)
        if v == Y: next.append(X)
        for next_v in next:
            if next_v not in seen:
                q.append((next_v, v, dist + 1))
                seen.add(next_v)
    d = defaultdict(int)
    for x in dx:
        d[x] += 1
    aaa[v0] = d

for k in range(1, N):
    ans = 0
    for i in range(1, N + 1):
        ans += aaa[i][k]
    print(ans // 2)