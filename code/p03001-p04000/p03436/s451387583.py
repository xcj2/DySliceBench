from collections import deque


dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]


H, W = map(int, input().split())
G = [input() for _ in range(H)]


# 色を変える前のマップ上の白色マスを数える
def count_white():
    res = 0
    for i in range(H):
        for j in range(W):
            if G[i][j] == '.':
                res += 1
    return res


# 色を変えずにスタートからゴールまでの最短歩数を数える
def minimum_step():
    dist = [[0] * W for _ in range(H)]
    dist[0][0] = 1
    que = deque([[0, 0]])

    # BFS
    while que:
        h, w = que.popleft()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if G[nh][nw] == '#':
                continue
            if dist[nh][nw]:
                continue
            dist[nh][nw] = dist[h][w] + 1
            que.append([nh, nw])
    return dist[H - 1][W - 1]


def main():
    step = minimum_step()
    print(count_white() - step if step else -1)

if __name__ == "__main__":
    main()