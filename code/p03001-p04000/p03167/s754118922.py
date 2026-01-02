import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


H, W = na()

A_array = [ns() for _ in range(H)]

mod = 10 ** 9 + 7

ans = [[0] * W for _ in range(H)]

ans[0][0] = 1
for i in range(1, W):
    if A_array[0][i] == "#":
        continue
    ans[0][i] = ans[0][i-1]

for i in range(1, H):
    if A_array[i][0] == "#":
        continue
    ans[i][0] = ans[i-1][0]


for i in range(1, H):
    for j in range(1, W):
        if A_array[i][j] == "#":
            continue
        ans[i][j] = (ans[i-1][j] + ans[i][j-1]) % mod

print(ans[H-1][W-1])
