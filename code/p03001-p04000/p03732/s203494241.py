# -*- coding: utf-8 -*-
"""
https://abc060.contest.atcoder.jp/tasks/arc073_b

"""
import sys
from sys import stdin
input = stdin.readline


def normal_dp(items, N, W):
    dp = [[0] * (W+1) for _ in range(N+1)]

    for y in range(1, N+1):
        w = items[y-1][0]
        v = items[y-1][1]
        for x in range(1, W+1):
            if x >= w:
                dp[y][x] = max(dp[y-1][x-w] + v, dp[y-1][x])
            else:
                dp[y][x] = dp[y-1][x]
    return dp[-1][-1]


def solve(items, N, W):
    items.sort(reverse=True)

    c_items = [[] for _ in range(4)] #  同じ重さのアイテムをまとめたもの、vで降順ソート済。[0]が一番軽いアイテムで[3]が+3だけ重い。
    min_w = items[-1][0]
    for w, v in items:
        c_items[w - min_w].append(v)
    for l in c_items:
        l.append(0)

    # ある重さのアイテムをn個選択したときのベストなvの値を計算しておく
    accumulated_v = [[0] for _ in range(4)]
    for i in range(4):
        for j, v in enumerate(c_items[i], start=1):
            accumulated_v[i].append(accumulated_v[i][-1] + v)

    total_values = []
    for iw0 in range(len(c_items[0])):
        for iw1 in range(len(c_items[1])):
            for iw2 in range(len(c_items[2])):
                for iw3 in range(len(c_items[3])):
                    total_w = (iw0 * min_w) + (iw1 * (min_w+1)) + (iw2 * (min_w+2)) + (iw3 * (min_w+3))
                    if total_w <= W:
                        total_v = accumulated_v[0][iw0] + accumulated_v[1][iw1] + accumulated_v[2][iw2] + accumulated_v[3][iw3]
                        total_values.append(total_v)
    return max(total_values)



def main(args):
    items = []
    N, W = map(int, input().split())
    for _ in range(N):
        w, v = map(int, input().split())
        items.append([w, v])
    items.sort()
    ans = solve(items, N, W)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
