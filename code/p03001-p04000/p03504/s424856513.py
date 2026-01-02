# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc080/tasks/abc080_d

"""
import sys
from sys import stdin
from heapq import heappop, heappush, heappushpop
input = stdin.readline


def prep_programs(programs):
    # 同じチャンネルで連続録画する場合はまとめる
    channels = [[] for _ in range(31)]
    res = []

    for s, t, c in programs:
        channels[c].append([s, t])

    for i in range(1, 31):
        channels[i].append([-1, -1])

    for i in range(1, 31):
        prev_start = channels[i][0][0]
        for a, b in zip(channels[i], channels[i][1:]):
            if a[1] == b[0]:
                pass
            else:
                res.append([prev_start, a[1], i])
                prev_start = b[0]
    return res


def solve(programs, N, C):
    programs.sort()
    programs = prep_programs(programs)
    programs.sort()

    max_used = 1
    R = []

    heappush(R, 0)
    for s, t, c in programs:
        end_time = heappushpop(R, t)
        if end_time >= s:
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
