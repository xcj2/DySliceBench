from __future__ import print_function

import sys
from functools import reduce

input = sys.stdin.readline


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return


def solve02():
    n = int(input().strip())
    L = []
    Xmin, Ymin, Xmax, Ymax = (sys.maxsize, sys.maxsize, -100, -100)

    for i in range(n):
        a, b = map(int, input().strip().split())
        L.append((a, b))
        Xmin, Ymin, Xmax, Ymax = (min(Xmin, a), min(Ymin, b), max(Xmax, a), max(Ymax, b))
    A, B, C, D = ((Xmin, Ymax), (Xmin, Ymin), (Xmax, Ymin), (Xmax, Ymax))

    # 対角線ACについて
    d_MinDistFromA = sys.maxsize    # 点Aからの距離が最小であるような，その最小の距離の値を求める
    d_MinDistFromC = sys.maxsize    # 点Cからの距離が最小であるような，その最小の距離の値を求める
    # 対角線BDについて
    d_MinDistFromB = sys.maxsize    # 点Bからの距離が最小であるような，その最小の距離の値を求める
    d_MinDistFromD = sys.maxsize    # 点Dからの距離が最小であるような，その最小の距離の値を求める

    for a, b in L:
        d_MinDistFromA = min(d_MinDistFromA, abs(a - Xmin) + abs(b - Ymax))
        d_MinDistFromC = min(d_MinDistFromC, abs(a - Xmax) + abs(b - Ymin))
        d_MinDistFromB = min(d_MinDistFromB, abs(a - Xmin) + abs(b - Ymin))
        d_MinDistFromD = min(d_MinDistFromD, abs(a - Xmax) + abs(b - Ymax))

    # 出力
    ans1 = abs(A[0] - C[0]) + abs(A[1] - C[1]) - (d_MinDistFromA + d_MinDistFromC)
    ans2 = abs(B[0] - D[0]) + abs(B[1] - D[1]) - (d_MinDistFromB + d_MinDistFromD)
    print(max(ans1, ans2))


def main():
    solve02()


if __name__ == '__main__':
    main()