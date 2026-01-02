# import sys
# input = sys.stdin.readline
import itertools
import collections


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    h, w = input_list()
    grids = [list(input()) for i in range(h)]
    dist = [[-1]*w for _ in range(h)]

    black_cells = collections.deque()
    for hi in range(h):
        for wi in range(w):
            if grids[hi][wi] == '#':
                black_cells.append((hi, wi))
                dist[hi][wi] = 0

    print(bfs(h, w, black_cells, dist))


def bfs(H, W, black_cells, dist):
    d = 0
    while black_cells:
        h, w = black_cells.popleft()
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            if dist[new_h][new_w] == -1:
                dist[new_h][new_w] = d + 1
                black_cells.append((new_h, new_w))
    return d


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
