#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, M: int, V: int, P: int, A: "List[int]"):

    ans = 0

    # 降順
    A.sort(reverse=True)

    acc = [0]+list(accumulate(A))

    for i in range(N):
        # ソート後の冒頭P問は大きいので可
        if i < P:
            ans += 1
            continue
        # M人が投票してもP番目のスコアに届かないなら無駄。
        if A[i]+M < A[P-1]:
            continue

        # 対象iがP問目として選ばれるために
        # 許容可能な投票数と、実際の投票数を比較する。
        cap = 0
        # 始めのP-1問にはM人が投票してよい
        cap += M*(P-1)
        # 後ろのN-i問(i, i+1, ..., N-1)にはM人が投票して良い
        cap += M*(N-i)
        # P問目からi-1問目までは、A[i]+Mを超えない範囲で投票して良い
        # \sum_{j = P-1}^{i-1} A[i]+M-A[j]
        # = (i-P+1)*(A[i]+M) - \sum_{j=P-1}^{i-1}A[j]
        cap += (i-P+1)*(A[i]+M)
        # accは始めに0を加えているので、インデックスが異なるので注意
        # 数列(0-index)のi-1番目までの和はacc[i](0-index)
        cap -= acc[i] - acc[P-1]
        if cap >= M*V:
            ans += 1
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, V, P, A)


if __name__ == '__main__':
    main()
