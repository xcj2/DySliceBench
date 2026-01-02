#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def solve(N: int):

    debug = False
    SN = str(N)
    keta = int(math.log10(N)+1)
    count = 0
    for i in range(1, N+1):
        first = str(i)[0]
        last = str(i)[-1]
        if last == "0":         # 考えない
            continue
        # ひとけた
        if first == last:
            count += 1
        # ふたけた
        if int(last+first) <= N:
            count += 1
        if keta < 3:
            continue
        # 3桁以上keta桁未満
        for j in range(3, keta):
            count += 10**(j-2)
        # keta桁
        # Nを超えない数
        if last < SN[0]:
            count += 10**(keta-2)
        elif last == SN[0]:
            # 間の桁について、i桁までまで考える。
            DP = [[0]*2 for _ in range(keta-1)]
            DP[0][False] = 1
            for j in range(1, keta-1):
                DP[j][False] = DP[j-1][False]*1
                DP[j][True] = DP[j-1][True]*10 + DP[j-1][False]*int(SN[j])
            count += DP[-1][True]
            if SN[-1] >= first:
                count += 1
    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
