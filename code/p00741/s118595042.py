import os

import itertools
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def solve(H, W):
    C = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    def ok(h, w):
        return 0 <= h < H and 0 <= w < W

    def dfs(h, w):
        C[h][w] = 0
        for dh, dw in itertools.product([-1, 0, 1], repeat=2):
            if ok(h + dh, w + dw) and C[h + dh][w + dw] == 1:
                dfs(h + dh, w + dw)

    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == 1:
                dfs(i, j)
                ans += 1
    return ans


while True:
    W, H = list(map(int, sys.stdin.readline().split()))
    if W == H == 0:
        break
    print(solve(H, W))

