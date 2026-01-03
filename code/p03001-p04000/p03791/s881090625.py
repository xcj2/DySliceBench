#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, x: "List[int]"):

    # hint[i]はi番目の要素より前のスペースの数
    hint = [(x[i]-1) - i for i in range(N)]
    # print(hint)
    ans = 1
    count = 1
    curr = 0

    # j回数える
    for j in range(N):
        # 前からゴール可能な数の個数を数える
        while True:
            # スペースの数 hint[curr]+j 個
            if curr >= N:
                break
            if count >= N-j:
                break
            if count-(hint[curr]+j) == 2:
                break
            count += 1
            curr += 1
        # print(count)
        ans *= count
        ans %= MOD
        count -= 1
    print(ans % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x)


if __name__ == '__main__':
    main()
