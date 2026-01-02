# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc085/tasks/abc085_c

"""
import sys
from sys import stdin
input = stdin.readline


def calc_yukichi(n, total):
    # 五千円札と一万円札をn枚使用して、ちょうどtotal円にするときの諭吉の枚数を返す
    gap = total - (5000 * n)
    if gap < 0:
        return -1
    yukichi = gap // 5000
    ichiyou = n - yukichi
    if ichiyou >= 0:
        return yukichi
    else:
        return -1


def solve(N, Y):
    # N枚の紙幣で、ちょうどY円になるような組み合わせを探す
    dp = [[False] * (2*N+1) for _ in range(N+1)] #  x軸は5000円単位
    dp[0][0] = True             #  0枚で0円

    if Y / 1000 == N:           #  1000円札のみのケース
        return 0, 0, N

    for y in range(1, N+1):
        for x in range(y-1, y*2):
            if dp[y-1][x]:
                dp[y][x+1] = True
                dp[y][x+2] = True

                if (x+1)*5000 + (N-y)*1000 == Y or (x+2)*5000 + (N-y)*1000 == Y:
                    hideyo = N - y
                    nokori = Y - hideyo * 1000
                    yukichi = calc_yukichi(y, nokori)
                    ichiyou = N - yukichi - hideyo
                    if yukichi >= 0 and ichiyou >= 0:
                        return yukichi, ichiyou, hideyo

    return -1, -1, -1           #  有効な組み合わせが見つからなかった


def main(args):
    N, Y = map(int, input().split())
    # N, Y = 2, 2000
    ans = solve(N, Y)
    print(*ans)


if __name__ == '__main__':
    main(sys.argv[1:])
