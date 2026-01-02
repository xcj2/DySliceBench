# -*- coding: utf-8 -*-
"""
C - All Green
https://beta.atcoder.jp/contests/abc104/tasks/abc104_c

"""
import sys
from sys import stdin
input = stdin.readline


from itertools import combinations
from math import ceil

def solve(D, G, scores):
    def pick_max(comb):
        a = [i*100 for i in range(D, 0, -1)]
        for c in comb:
            a.remove(c)
        return a[0] if a else None


    ans = float('inf')
    points = [100 * p for p in range(1, D+1)]

    for d in range(D+1):
        for comb in combinations(points, d):
            score = 0
            pick = 0
            for p in comb:
                score += (p * scores[p][0]) + scores[p][1]
                pick += scores[p][0]
            if score < G:
                ad = pick_max(comb)
                if ad:
                    n = ceil((G - score) / ad)
                    if n >= scores[ad][0]:
                        pick = float('inf')
                    else:
                        pick += n
                else:
                    pick = float('inf')
            ans = min(ans, pick)
    return ans


def main(args):
    D, G = map(int, input().split())

    scores = {}
    for i in range(1, D+1):
        p, c = map(int, input().split())
        scores[i*100] = [p, c]
    ans = solve(D, G, scores)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
