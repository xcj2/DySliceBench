import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import deque

# 入力
n = ni()
graph = [[] for _ in range(n*n)]

# グラフを構築
ins = [0]*(n*n)
for i in range(n):
    jlist = list(li_())
    for j1, j2 in zip(jlist[:-1], jlist[1:]):
        node1 = max(i, j1)*n + min(i, j1)
        node2 = max(i, j2)*n + min(i, j2)
        graph[node1].append(node2)
        ins[node2] += 1

# 最長経路
visited = [False]*(n*n)
for i in range(n):
    visited[i*n + i] = True

# 入次数0をqueに詰める
que = deque()
for i, insi in enumerate(ins):
    if insi == 0:
        que.append((i, 1))

# queがなくなるまで距離を記録
dist = [0]*(n*n)
while que:
    cur, d = que.popleft()

    visited[cur] = True
    dist[cur] = d
    for nex in graph[cur]:
        if not visited[nex]:
            ins[nex] -= 1
            if ins[nex] == 0:
                que.append((nex, d+1))

# 訪れてないノードがあれば-1
ok = True
for vi in visited:
    if not vi:
        ok = False


ans = 0
for di in dist:
    ans = max(ans, di)

print(-1 if not ok else ans)