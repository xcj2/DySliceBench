N = int(input())
s = [0]*N
l = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    s[i] = (a, b)
 
for i in range(N):
    c, d = map(int, input().split())
    l[i] = (c, d)




V = N*2 # 頂点数
MAX_V = V

G = [0]*MAX_V # グラフの隣接リスト表現
for i in range(MAX_V):
    G[i] = []
match = [0]*MAX_V # マッチングのペア
used = [False]*MAX_V # DFSで既に調べたかのフラグ

# uとvを結ぶ辺をグラフに追加する
def addEdge(u, v):
    G[u].append(v)
    G[v].append(u)


##
for a in range(N):
    (rx, ry) = s[a]
    for b in range(N):
        (bx, by) = l[b]
        if rx < bx and ry < by:
            addEdge(a, b+N)


# 増加パスをDFSで探す
def dfs(v):
    used[v] = True
    for i in range(len(G[v])):
        u = G[v][i]
        w = match[u]
        if w < 0 or not used[w] and dfs(w):
            match[v] = u
            match[u] = v
            return True
    return False

# 二部グラフの最大マッチングを求める
def bipartiteMatching():
    res = 0
    for i in range(len(match)):
        match[i] = -1
    for v in range(V):
        if match[v] < 0:
            for i in range(len(used)):
                used[i] = False
            if dfs(v):
                res += 1
    return res

print(bipartiteMatching())

