# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc045/tasks/arc061_a

"""
import sys
from sys import stdin
from itertools import combinations
input = stdin.readline


def prepare_eq(S, c):
    # c番目の数字の後に+を入れた数式を生成する (0起算)
    if len(c) == 0:
        return S

    eq = ''
    for i, s in enumerate(S):
        eq += s
        if i == c[0]:
            eq += '+'
            c = c[1:]
            if len(c) == 0:
                eq += S[i+1:]
                break
    return eq


def solve(S):
    total = 0
    for i in range(len(S)):
        for c in combinations(range(len(S)-1), i): # 0個〜文字列の長さ-1個までの+記号を追加して、数式を生成する
            eq = prepare_eq(S, c)
            total += eval(eq)   #  その数式の値を加算
    return total


def main(args):
    S = input().strip()
    ans = solve(S)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
