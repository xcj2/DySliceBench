# import sys
# input = sys.stdin.readline
import itertools
import collections
from decimal import Decimal
from functools import reduce


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    H, W, k = input_list()
    maze = [list(input()) for _ in range(H)]
    ans = 0
    for row_bit in itertools.product(range(2), repeat=H):
        for col_bit in itertools.product(range(2), repeat=W):
            cnt = 0
            for row in range(H):
                for col in range(W):
                    if maze[row][col] == "#" and (row_bit[row] and col_bit[col]):
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


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
