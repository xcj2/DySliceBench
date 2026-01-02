# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc080/tasks/abc080_d

"""
import sys
from sys import stdin
from heapq import heappop, heappush, heappushpop
input = stdin.readline


def prep_programs(programs, C):
    # 同じチャンネルで連続録画する場合はまとめる
    channels = [[] for _ in range(C+1)]
    res = []

    programs.sort()
    for s, t, c in programs:    #  チャンネルごとに録画したい番組を分ける
        channels[c].append([s, t])

    for i in range(1, C+1):      #  zipでずらして処理できるように、ダミーの番組を追加
        channels[i].append([-1, -1])

    # チャンネルごとに連続する番組があれば一つの録画枠にまとめる
    for i in range(1, C+1):
        prev_start = channels[i][0][0]
        for a, b in zip(channels[i], channels[i][1:]):
            if a[1] == b[0]:
                pass
            else:
                res.append([prev_start, a[1], i])
                prev_start = b[0]
    res.sort()
    return res                  #  まとめた録画リスト


def solve(programs, N, C):
    P = prep_programs(programs, C)

    max_used = 1                #  必要な録画機の台数
    R = []

    heappush(R, 0)
    for s, t, c in P:
        end_time = heappushpop(R, t)
        if end_time >= s:       #  番組の録画時間になった時に前の番組が終わっていない (チャンネルが違う場合は、前の録画終了と次の録画開始が同時でも2台必要)
            heappush(R, end_time)
            max_used = len(R)
    return max_used


def main(args):
    programs = []
    N, C = map(int, input().split())
    for _ in range(N):
        s, t, c = map(int, input().split())
        programs.append([s, t, c])
    ans = solve(programs, N, C)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
