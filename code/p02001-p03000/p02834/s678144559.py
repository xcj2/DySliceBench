import sys
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N, u, v = MI()
nl = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = MI()
    nl[a - 1].append(b - 1)
    nl[b - 1].append(a - 1)


def distance(v0):
    dist = [0] * N
    q = deque([(v0, -1, 0)])
    while len(q) > 0:
        v, p, d = q.popleft()
        dist[v] = d
        for next_v in nl[v]:
            if next_v != p:
                q.append((next_v, v, d + 1))
    return dist


t = distance(u - 1)
a = distance(v - 1)
initial_dist = t[v - 1]

ans = 0
for i in range(N):
    if a[i] > t[i]:
        ans = max(ans, a[i] - 1)
ans = max(ans, initial_dist - 1)
print(ans)
