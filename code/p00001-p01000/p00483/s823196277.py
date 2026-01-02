# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0560

"""
import sys
from sys import stdin
input = stdin.readline


def solve(M, N, K, field):
    dp_J = [[0] * (N+1) for _ in range(M+1)]
    dp_O = [[0] * (N+1) for _ in range(M+1)]
    dp_I = [[0] * (N+1) for _ in range(M+1)]
    for y in range(M):
        t_J = [0] * (N+1)
        t_O = [0] * (N+1)
        t_I = [0] * (N+1)
        for x in range(N):
            land = field[y][x]
            if land == 'J':
                t_J[x+1] = t_J[x] + 1
                t_O[x+1] = t_O[x]
                t_I[x+1] = t_I[x]
            elif land == 'O':
                t_J[x+1] = t_J[x]
                t_O[x+1] = t_O[x] + 1
                t_I[x+1] = t_I[x]
            else:
                t_J[x+1] = t_J[x]
                t_O[x+1] = t_O[x]
                t_I[x+1] = t_I[x] + 1

        for x in range(1, N+1):
            dp_J[y+1][x] = dp_J[y][x] + t_J[x]
            dp_O[y+1][x] = dp_O[y][x] + t_O[x]
            dp_I[y+1][x] = dp_I[y][x] + t_I[x]

    for _ in range(K):
        result = [0, 0, 0]
        y1, x1, y2, x2 = map(int, input().split())
        result[0] = dp_J[y2][x2] - dp_J[y1-1][x2] - dp_J[y2][x1-1] + dp_J[y1-1][x1-1]
        result[1] = dp_O[y2][x2] - dp_O[y1-1][x2] - dp_O[y2][x1-1] + dp_O[y1-1][x1-1]
        result[2] = dp_I[y2][x2] - dp_I[y1-1][x2] - dp_I[y2][x1-1] + dp_I[y1-1][x1-1]
        print(' '.join(map(str, result)))


def solve2(M, N, K, field):
    dp_J = [[0] * (N+1) for _ in range(M+1)]
    dp_O = [[0] * (N+1) for _ in range(M+1)]
    for y in range(M):
        t_J = [0] * (N+1)
        t_O = [0] * (N+1)
        for x in range(N):
            land = field[y][x]
            if land == 'J':
                t_J[x+1] = t_J[x] + 1
                t_O[x+1] = t_O[x]
            elif land == 'O':
                t_J[x+1] = t_J[x]
                t_O[x+1] = t_O[x] + 1
            else:
                t_J[x+1] = t_J[x]
                t_O[x+1] = t_O[x]

        for x in range(1, N+1):
            dp_J[y+1][x] = dp_J[y][x] + t_J[x]
            dp_O[y+1][x] = dp_O[y][x] + t_O[x]


    for _ in range(K):
        result = [0, 0, 0]
        y1, x1, y2, x2 = map(int, input().split())
        result[0] = dp_J[y2][x2] - dp_J[y1-1][x2] - dp_J[y2][x1-1] + dp_J[y1-1][x1-1]
        result[1] = dp_O[y2][x2] - dp_O[y1-1][x2] - dp_O[y2][x1-1] + dp_O[y1-1][x1-1]
        result[2] = (x2 - x1 + 1) * (y2 - y1 + 1) - result[0] - result[1]
        print(' '.join(map(str, result)))


def main(args):
    M, N = map(int, input().split())
    K = int(input())
    field = [input().strip() for _ in range(M)]
    solve2(M, N, K, field)


if __name__ == '__main__':
    main(sys.argv[1:])
    