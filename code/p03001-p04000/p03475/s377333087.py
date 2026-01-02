#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):

    def hasha(curr, ith):
        if curr > S[ith]:
            return S[ith] + F[ith]*(-(-(curr-S[ith])//F[ith]))
        else:
            return S[ith]

    ans = []
    for i in range(N-1):        # 開始駅
        buf = 0
        for j in range(i, N-1):  # 現在駅
            buf = hasha(buf, j) + C[j]
        ans.append(buf)
    print(*ans, sep="\n")
    print("0")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N-1)  # type: "List[int]"
    S = [int()] * (N-1)  # type: "List[int]"
    F = [int()] * (N-1)  # type: "List[int]"
    for i in range(N-1):
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
        F[i] = int(next(tokens))
    solve(N, C, S, F)


if __name__ == '__main__':
    main()
