#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from itertools import accumulate
INF = float("inf")


def bit(n, k):
    return (n >> k) & 1


def bit_sum(n):
    wa = 0
    while n > 0:
        wa += n & 1
        n >>= 1
    return wa


def border(x):
    # xを二進数で与えた時、ビットの立っている位置のリストを1-indexで返す
    c = 0
    ans = []
    while x > 0:
        c += 1
        if x & 1:
            ans.append(c)
        x >>= 1
    return ans


def main():

    H, W, K = map(int, input().split())
    S = [[0]*W for _ in range(H)]
    for h in range(H):
        S[h][:] = [int(c) for c in input()]
    acc = [[0]+list(accumulate(S[h])) for h in range(H)]

    min_kaisu = +INF
    for h in range(1 << (H-1)):
        # hは分割方法を与える
        # hで与えられる分割方法は、どのような分割なのかを得る。
        startend = border(h)
        flag = False

        division = [0]
        # x番目でW方向に分割すると仮定する
        for x in range(1, W+1):
            # xの位置で分割したとき、左の領域のホワイトチョコレートの数
            # まずは行ごとに求める
            white = [acc[i][x] - acc[i][division[-1]] for i in range(H)]
            # 領域ごとに加算するし、最大値を撮る
            white_sum = [sum(white[s:e])
                         for s, e in zip([0]+startend, startend+[H])]
            # print(bin(h), division, x, white_sum)
            white_max = max(white_sum)
            # Kよりも大きくなるなら、事前に分割するべきであった。
            if white_max > K:
                division.append(x-1)
                # 分割してもなおK以下を達成できないケースを除外する
                white = [acc[i][x] - acc[i][division[-1]] for i in range(H)]
                white_sum = [sum(white[s:e])
                             for s, e in zip([0]+startend, startend+[H])]
                white_max = max(white_sum)
                if white_max > K:
                    flag = True
                    break
        if flag:
            continue
        # hによる分割も考慮する
        division_tot = len(division)-1 + bit_sum(h)
        min_kaisu = min(division_tot, min_kaisu)
    print(min_kaisu)
    return


if __name__ == '__main__':
    main()
