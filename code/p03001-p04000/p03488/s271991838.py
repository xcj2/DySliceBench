# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc082/tasks/arc087_b

"""
import sys
from sys import stdin
input = stdin.readline


def check_x(forwards):
    n = sum(forwards[::2])      #  x軸方向への最大移動量
    dpx = [False] * (n * 2 + 1) #  真ん中を0として、±両方向のdp領域を確保
    dpx[forwards[0] + n] = True #  最初は0からプラス方向に移動

    for f in forwards[2::2]:
        if f == 0:
            continue
        n_move = dpx[f:] + [False]*f
        p_move = [False]*f + dpx[:-f]
        t = [a or b for a, b in zip(n_move, p_move)]
        dpx = t
    return dpx, n


def check_y(forwards):
    n = sum(forwards[1::2])
    dpy = [False] * (n * 2 + 1)
    dpy[n] = True

    for f in forwards[1::2]:
        if f == 0:
            continue
        n_move = dpy[f:] + [False]*f
        p_move = [False]*f + dpy[:-f]
        t = [a or b for a, b in zip(n_move, p_move)]
        dpy = t
    return dpy, n


def solve(s, gx, gy):
    forwards = [len(x) for x in s.split('T')] #  進む歩数情報の数字に変換
    dpx, zx = check_x(forwards)
    dpy, zy = check_y(forwards)

    if zx < abs(gx):
        return 'No'
    if zy < abs(gy):
        return 'No'
    if dpx[gx + zx] is True and dpy[gy + zy] is True:
        return 'Yes'
    else:
        return 'No'


def main(args):
    s = input().strip()
    gx, gy = map(int, input().split())
    # s = 'F'
    # gx, gy = -1, 0
    ans = solve(s, gx, gy)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
    
