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


def dfs(graph: list, node: int, start: int) -> list:
    # 未探索のノードは距離INF
    INF = float("inf")
    dist = [INF] * node

    # 始点ノードの距離を0とし、dfsのためのstackを作成
    dist[start] = 0
    stack = [(0, start)]

    while stack:
        cost, cur_node = stack.pop()

        # 未探索のノードをstackに入れる
        for nex_cost, nex_node in graph[cur_node]:
            if dist[nex_node] != INF:
                continue
            else:
                dist[nex_node] = dist[cur_node] + nex_cost
                stack.append((dist[nex_node], nex_node))

    return dist


n, m, p = li()
edges = []
for _ in range(m):
    ai, bi, ci = li()
    ai -= 1
    bi -= 1
    ci -= p
    edges.append((ai, bi, ci))

# グラフ構築
one2n = [[] for _ in range(n)]
n2one = [[] for _ in range(n)]
for ai, bi, _ in edges:
    one2n[ai].append((ci, bi))
    n2one[bi].append((ci, ai))

# 1から到達可能な点を抽出
one2n_dist = dfs(one2n, n, 0)
one2n_reachable = set()
for i, di in enumerate(one2n_dist):
    if di != float('inf'):
        one2n_reachable.add(i)

# Nから到達可能な点を抽出
n2one_dist = dfs(n2one, n, n-1)
n2one_reachable = set()
for i, di in enumerate(n2one_dist):
    if di != float('inf'):
        n2one_reachable.add(i)

one2n_path = one2n_reachable & n2one_reachable


# ベルマンフォード
INF = float('inf')
dist = [-INF]*n
dist[0] = 0

for _ in range(n):
    for ai, bi, ci in edges:
        if ai in one2n_path and bi in one2n_path and dist[ai] + ci > dist[bi]:
            dist[bi] = dist[ai] + ci

aftern = dist[n-1]

modified = False

for ai, bi, ci in edges:
    if ai in one2n_path and bi in one2n_path and dist[ai] + ci > dist[bi]:
        modified = True

# N+1回で更新されていれば-1
if modified:
    print(-1)
else:
    print(max(0, aftern))