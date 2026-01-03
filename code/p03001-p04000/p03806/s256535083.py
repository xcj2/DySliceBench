#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M_a: int, M_b: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    M = (max(a+b)+1)*N
    DP = [[INF]*(M) for _ in range(M)]
    for aa, bb, cc in zip(a, b, c):
        DP_next = [DP[i][:] for i in range(M)]
        DP_next[aa][bb] = min(cc, DP_next[aa][bb])
        for i in range(1, M):
            if M <= i + aa:
                break
            for j in range(1, M):
                if M <= j+bb:
                    break
                DP_next[i+aa][j+bb] = min(DP[i][j]+cc, DP_next[i+aa][j+bb])
        DP = DP_next

    m = INF
    for i in range(1, M//M_a):
        anum = M_a*i
        bnum = M_b*i
        if anum >= M or bnum >= M:
            break
        m = min(DP[anum][bnum], m)
    if m == INF:
        print(-1)
    else:
        print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M_a = int(next(tokens))  # type: int
    M_b = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M_a, M_b, a, b, c)


if __name__ == '__main__':
    main()
