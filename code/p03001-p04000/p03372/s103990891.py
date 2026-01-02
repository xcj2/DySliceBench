#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, C: int, x: "List[int]", v: "List[int]"):

    # 時計回りターンなし
    nt_cost = x
    nt_benefit = accumulate(v)
    nt_callory = [b-c for c, b in zip(nt_cost, nt_benefit)]
    nt_callory_acc = list(accumulate([0]+nt_callory, max))

    # 反時計回りターンなし
    rnt_cost = [C-v for v in reversed(x)]
    rnt_benefit = accumulate(reversed(v))
    rnt_callory = [b-c for c, b in zip(rnt_cost, rnt_benefit)]
    rnt_callory_acc = list(accumulate([0]+rnt_callory, max))

    # 時計回り
    m = max(nt_callory_acc[-1], rnt_callory_acc[-1])
    for i in range(N-1):
        callory = nt_callory[i]-nt_cost[i]+rnt_callory_acc[N-i-1]
        m = max(m, callory)

    # 反時計回り
    for i in range(N-1):
        callory = rnt_callory[i]-rnt_cost[i]+nt_callory_acc[N-i-1]
        m = max(m, callory)

    print(max(0, m))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, C, x, v)


if __name__ == '__main__':
    main()
