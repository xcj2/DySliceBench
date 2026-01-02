H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(list(s))

# 隣接のマスをループで表すために必要
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def is_street(s, t):
    """
    道であること（壁ではないこと）を確認
    """
    return S[s][t] == '.'

def count(maze):
    """
    最大のコストを探索
    """
    r = -1
    for i in range(H):
        for j in range(W):
            r = max(r, maze[i][j])
    return r

def bfs(h, w):
    """
    h: スタート位置（高さ）
    w: スタート位置（横）
    """
    m = []  # スタート地点からの距離が入る
    for i in range(H):
        s = [-1] * W
        m.append(s)
    m[h][w] = 0  # スタート地点は0

    q = [[h, w]]
    while len(q) != 0:
        t, u = q.pop(0)
        cost = m[t][u]

        for i in range(4):
            ni = t + di[i]
            nj = u + dj[i]
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if not is_street(ni, nj): 
                continue
            if m[ni][nj] != -1:
                continue

            m[ni][nj] = cost + 1
            q.append([ni, nj])

    max_cost = count(m)
    return max_cost

ans = -1
# 壁以外のすべてのマスをスタートにして探索
for i in range(H):
    for j in range(W):
        if is_street(i, j):
            c = bfs(i, j)
            ans = max(ans, c)

print(ans)
