# -*- coding: utf-8 -*-
"""
D - equeue
https://atcoder.jp/contests/abc128/tasks/abc128_d

"""
import sys


def dig_lr(n, q, lr='L'):
    # 左(もしくは右)側から最大でn回操作した時の結果の最大値を求める
    res = [0]
    for di in range(1, min(n, len(q))+1): #  diは最大で掘る回数
        bu = n - di             #  埋める方に使用する操作回数
        dig = list(q[:di]) if lr == 'L' else list(q[-di:])
        dig.sort()
        while bu and dig and dig[0] < 0: #  マイナスのアイテムが手元にあればマイナスが大きい方から埋める
            dig.pop(0)
            bu -= 1
        res.append(sum(dig))
    return max(res)


def solve(N, K, V):
    ans = [0]
    limit = sum([v for v in V if v > 0]) #  価値がプラスのアイテムだけ取り出せたときの合計(理論上ベストな結果)
    # K操作回の操作を左右で(左:0 右:K), (左:1 右:K-1), ...,  (左:K 右:0),のように割り振っていき、
    # 左・右からゲットできる値の合計値を計算する
    for left in range(K+1):
        right = K - left
        l_dig = dig_lr(left, V, 'L')
        r_dig = dig_lr(right, V, 'R')
        ans.append(min(limit, l_dig+r_dig))
    return max(ans)


def main(args):
    N, K = map(int, input().split())
    V = [int(v) for v in input().split()]
    ans = solve(N, K, V)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
