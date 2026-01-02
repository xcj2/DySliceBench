import sys
sys.setrecursionlimit(1000000)

def get_root(s):
    if s != root[s]:
        root[s] = get_root(root[s])
        return root[s]
    return s

def unite(s, t):
    root_s = get_root(s)
    root_t = get_root(t)
    if not root_s == root_t:
        if rank[s] == rank[t]:
            root[root_t] = root_s
            rank[root_s] += 1
        elif rank[s] > rank[t]:
            root[root_t] = root_s
        else:
            root[root_s] = root_t

def same(s, t):
    if get_root(s) == get_root(t):
        return True
    else:
        return False

n, m = map(int, input().split())
root = [i for i in range(n)]
rank = [1 for _ in range(n)]
size = [1 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    if not same(a - 1, b - 1):
        unite(a - 1, b - 1)
x = [0] * n
ans = 0
for i in range(n):
    j = get_root(i)
    x[j] += 1
    ans = max(ans, x[j])
print(ans)
"""

from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visit[s] = 1
    cnt = 1
    while q:
        p = q.popleft()
        for j in G[p]:
            if visit[j] == 0:
                q.append(j)
                visit[j] = 1
                cnt += 1
    global ans
    ans = max(ans, cnt)
    return

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visit = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if visit[i] == 0:
        bfs(i)
print(ans)
"""