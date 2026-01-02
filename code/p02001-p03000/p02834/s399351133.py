import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, u, v = mapint()
query = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = mapint()
    query[a-1].append(b-1)
    query[b-1].append(a-1)

from collections import deque
def dfs(start):
    Q = deque([start])
    dist = [10**18]*N
    dist[start] = 0
    while Q:
        now = Q.pop()
        for nx in query[now]:
            if dist[nx]>=10**18:
                dist[nx] = dist[now] + 1
                Q.append(nx)
    return dist

taka = dfs(u-1)
aoki = dfs(v-1)
ans = 0

for i in range(N):
    t, a = taka[i], aoki[i]
    if t<=a:
        ans = max(ans, a-1)
print(ans)