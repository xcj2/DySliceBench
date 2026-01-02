from collections import deque, Counter, defaultdict
from itertools import chain, combinations
import json
# import numpy as np
import bisect
import sys
import math
import bisect
from functools import lru_cache
import itertools

sys.setrecursionlimit(10 ** 8)

M = 10 ** 9 + 7
INF = 10 ** 17


def main():
    D = int(input())
    c = [int(a) for a in input().split()]
    s = [
        [int(a) for a in input().split()]
        for _ in range(D)
    ]
    t = [
        int(input())
        for _ in range(D)
    ]
    M = int(input())
    dq = [
        [int(a) for a in input().split()]
        for _ in range(M)
    ]

    def calc_score(t):
        score = 0
        last = [0] * len(c)
        res = []

        for d, ti in enumerate(t):
            sdi = s[d][ti - 1]
            score += sdi
            last[ti - 1] = d + 1
            for i, ci in enumerate(c):
                score -= ci * ((d + 1) - last[i])
            res.append(score)
        return res

    def calc_score_diff(t, di, qi):
        old_q = t[di - 1]
        last_old_q_date = 0
        for i in range(di - 2, -1, -1):
            if t[i] == old_q:
                last_old_q_date = i + 1
                break
        next_old_q_date = D + 1
        for i in range(di, D):
            if t[i] == old_q:
                next_old_q_date = i + 1
                break

        old_d_last = di - last_old_q_date
        old_d_next = next_old_q_date - di
        old_diff = old_d_next * old_d_last * c[old_q - 1]

        new_q = qi
        last_new_q_date = 0
        for i in range(di - 2, -1, -1):
            if t[i] == new_q:
                last_new_q_date = i + 1
                break
        next_new_q_date = D + 1
        for i in range(di, D):
            if t[i] == new_q:
                next_new_q_date = i + 1
                break

        new_d_last = di - last_new_q_date
        new_d_next = next_new_q_date - di
        new_diff = new_d_next * new_d_last * c[new_q - 1]

        old_score = s[di - 1][old_q - 1]
        new_score = s[di - 1][new_q - 1]
        return new_diff - old_diff + new_score - old_score

    score = calc_score(t)[-1]
    for di, qi in dq:
        diff = calc_score_diff(t, di, qi)
        score += diff
        print(score)
        t[di - 1] = qi


if __name__ == "__main__":
    main()
