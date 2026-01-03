# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc057/tasks/abc057_b

"""
import sys
from sys import stdin
input = stdin.readline


def calc_dist(s, c):
    return abs(s[0] - c[0]) + abs(s[1] - c[1])


def solve(students, checkpoints):
    ans = []

    for s in students[1:]:
        dist = [float('inf')]
        for c in checkpoints[1:]:
            d = calc_dist(s, c)
            dist.append(d)
        min_dist = min(dist)
        cp_num = dist.index(min_dist )
        ans.append(cp_num)
    return ans


def main(args):
    students = [[0, 0]]
    N, M = map(int, input().split())
    for _ in range(N):
        a, b = map(int, input().split())
        students.append([a, b])
    checkpoints = [[0, 0]]
    for _ in range(M):
        c, d = map(int, input().split())
        checkpoints.append([c, d])
    ans = solve(students, checkpoints)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main(sys.argv[1:])
