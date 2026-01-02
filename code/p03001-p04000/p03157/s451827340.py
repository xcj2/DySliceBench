def main():
    """
    1 <= H, W <= 400
    |Si| = W  (#, .)
    """
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = f(H, W, S)
    print(ans)


def f(H, W, S):
    ans1 = editorial(H, W, S)
    ans2 = f_rec(H, W, S)

    assert ans1 == ans2
    return ans1


def editorial(H, W, S):
    """
    ある地点からの黒と白のマスの数
    黒から白への行き方は
    黒の数から白の数
    """
    from collections import deque
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    color = [[S[i][j] == "#" for j in range(W)]
             for i in range(H)]
    used = [[False] * W for i in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if used[i][j]:
                continue
            used[i][j] = True

            b, w = 0, 0
            que = deque([(i, j)])
            while que:
                ci, cj = que.pop()
                if color[ci][cj]:
                    b += 1
                else:
                    w += 1

                for d in range(4):
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    in_range = 0 <= ni < H and 0 <= nj < W
                    if not in_range:
                        continue
                    if used[ni][nj]:
                        continue
                    if color[ci][cj] == color[ni][nj]:
                        continue

                    used[ni][nj] = True
                    que.append((ni, nj))

            ans += b * w

    return ans


def f_rec(H, W, S):
    import sys
    sys.setrecursionlimit(10 ** 9)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def rec(h, w, vis):
        vis[h][w] = True
        bl, wh = 0, 0
        if S[h][w] == "#":
            bl += 1
        else:
            wh += 1

        for i in range(4):
            ny = h + dy[i]
            nx = w + dx[i]
            in_range = 0 <= ny < H and 0 <= nx < W
            if in_range and not vis[ny][nx] and S[ny][nx] != S[h][w]:
                n_bl, n_wh = rec(ny, nx, vis)
                bl += n_bl
                wh += n_wh

        return bl, wh

    vis = [[False] * W for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            bl, wh = rec(h, w, vis)
            ans += bl * wh

    return ans


def TLE_pypy3(H, W, S):
    """
    c1 to c2:
        c1: black(#), c2: white(.)
        c1 - not c1 - c1 - c2

    上下左右に隣り合うマスへの移動を繰り返し
    a to b: N * N = 400 ^ 2 = 1.6 * 10^5
    Nb to Nw == Nw to Nb

    あるマスからどこまで進めるか（直線）
    North <-> South
    West  <-> East

    a to b: ok
    b to c: ok
    a to c: ok (3段論法)

    """
    # south, north, east, west
    d = zip([0, 0, 1, -1],
            [1, -1, 0, 0])
    d = list(d)
    to = {"#": ".", ".": "#"}

    b = []
    for _ in range(H):
        b2 = []
        for _ in range(W):
            b2.append([None] * 4)
        b.append(b2)

    blacks = {}
    for y in range(H):
        for x in range(W):
            src = S[y][x]
            if src == "#":
                blacks[(y, x)] = -1

            for i, (dx, dy) in enumerate(d):
                nx = x + dx
                ny = y + dy

                valid = 0 <= nx < W and 0 <= ny < H
                if not valid:
                    continue

                if S[ny][nx] == to[src]:
                    b[y][x][i] = (ny, nx)

    ans = 0
    # #からなので、候補
    for (y, x), _ in blacks.items():
        # 黒から辿り、１ターンでー候補白を見つけ黒へたどる、次のターンの黒を見つける
        bs = [(y, x)]
        # 辿った黒白のマスをまた辿らないようにする
        used_bs = {}
        used_ws = {}
        while bs:
            by, bx = bs.pop()
            used_bs[(by, bx)] = None

            # 黒から白
            whites = []
            for pos in b[by][bx]:
                if pos and pos not in used_ws:
                    ans += 1
                    whites.append(pos)
                    used_ws[pos] = None

            # 白から黒
            for wy, wx in whites:
                for pos in b[wy][wx]:
                    if pos and pos not in used_bs:
                        bs.append(pos)

    return ans


if __name__ == '__main__':
    main()
