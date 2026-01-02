#!/usr/bin/env python3
import sys
import itertools
import collections
from queue import Queue
import functools
import math
INF = 10**9


def solve(N: int, K: int, x: "List[int]"):
    x_neg = ([-xx for xx in x if xx < 0]+[0])[::-1]
    x_pos = [0] + [xx for xx in x if xx >= 0]

    # 左先を考える
    left = [x_neg[i]*2 + x_pos[K-i] for i in range(len(x_neg))
            if 0 <= K-i and K-i < len(x_pos)]
    if len(left) > 0:
        ansleft = min(left)
    else:
        ansleft = INF

    # 右先
    right = [x_pos[i]*2 + x_neg[K-i] for i in range(len(x_pos))
             if 0 <= K-i and K-i < len(x_neg)]
    if len(right) > 0:
        ansright = min(right)
    else:
        ansright = INF
    # print(left)
    # print(right)
    print(min(ansright, ansleft))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)


if __name__ == '__main__':
    main()
