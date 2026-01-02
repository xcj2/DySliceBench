H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(list(s))

def is_street(s, t):
    return S[s][t] == '.'

def count(maze):
    r = -1
    for i in range(H):
        for j in range(W):
            r = max(r, maze[i][j])
    return r

def bfs(h, w):
    m = []
    for i in range(H):
        s = [-1] * W
        m.append(s)
    m[h][w] = 0

    q = [[h, w]]
    while len(q) != 0:
        t, u = q.pop(0)
        cost = m[t][u]

        # 上
        ue = [t-1, u]
        if ue[0] >= 0 and m[ue[0]][ue[1]] == -1 and is_street(ue[0], ue[1]):
            m[ue[0]][ue[1]] = cost + 1
            q.append(ue)

        shita = [t+1, u]
        if shita[0] < H and m[shita[0]][shita[1]] == -1 and is_street(shita[0], shita[1]) :
            m[shita[0]][shita[1]] = cost + 1
            q.append(shita)

        hidari = [t, u-1]
        if hidari[1] >= 0 and m[hidari[0]][hidari[1]] == -1 and is_street(hidari[0], hidari[1]):
            m[hidari[0]][hidari[1]] = cost + 1
            q.append(hidari)

        migi = [t, u+1]
        if migi[1] < W and m[migi[0]][migi[1]] == -1 and is_street(migi[0], migi[1]):
            m[migi[0]][migi[1]] = cost + 1
            q.append(migi)
    # print(m)
    max_cost = count(m)
    return max_cost

ans = -1
for i in range(H):
    for j in range(W):
        if is_street(i, j):
            c = bfs(i, j)
            ans = max(ans, c)

print(ans)
