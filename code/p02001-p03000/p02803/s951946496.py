H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(list(s))

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

    q = [[h, w]]  # キュー
    while len(q) != 0:
        t, u = q.pop(0)
        cost = m[t][u]

        # 上
        uh = t-1
        uw = u
        if uh >= 0 and m[uh][uw] == -1 and is_street(uh, uw):
            m[uh][uw] = cost + 1
            q.append([uh, uw])

        # 下
        sh = t+1
        sw = u
        if sh < H and m[sh][sw] == -1 and is_street(sh, sw):
            m[sh][sw] = cost + 1
            q.append([sh, sw])

        # 左
        lh = t
        lw = u-1
        if lw >= 0 and m[lh][lw] == -1 and is_street(lh, lw):
            m[lh][lw] = cost + 1
            q.append([lh, lw])


        rh = t
        rw = u+1
        if rw < W and m[rh][rw] == -1 and is_street(rh, rw):
            m[rh][rw] = cost + 1
            q.append([rh, rw])

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
