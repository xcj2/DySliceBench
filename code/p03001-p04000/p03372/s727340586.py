#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, C: int, x: "List[int]", v: "List[int]"):

    # 時計回りターンなし
    nt_cost = x
    nt_benefit = list(accumulate(v))
    nt_callory = [b-c for c, b in zip(nt_cost, nt_benefit)]
    nt_callory_acc = list(accumulate(nt_callory, max)) + [0]
    # [0]はモンキーパッチ。後に負の参照をした場合に参照させる用
    # print(nt_callory)
    # print(nt_callory_acc)

    # 反時計回りターンなし
    rnt_cost = list((reversed([C-v for v in x])))
    rnt_benefit = list(accumulate(reversed(v)))
    rnt_callory = [b-c for c, b in zip(rnt_cost, rnt_benefit)]
    rnt_callory_acc = list(accumulate(rnt_callory, max)) + [0]
    # print(rnt_callory)
    # print(rnt_callory_acc)

    # 時計回り
    m = -INF
    for i in range(N):
        # i番目でターン
        callory = max(nt_callory[i]-nt_cost[i]+rnt_callory_acc[N-i-2],
                      nt_callory[i])
        # print(i, callory)
        m = max(m, callory)

    # 反時計回り
    for i in range(N):
        # i番目でターン
        callory = max(rnt_callory[i]-rnt_cost[i]+nt_callory_acc[N-i-2],
                      rnt_callory[i])
        # print(i, callory)
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
