#!/usr/bin/env python3
import sys
import heapq
INF = float("inf")


def solve(N: int, M: int, A: "List[int]"):
    h = []
    tot = 0
    for a in A:
        heapq.heappush(h, (-a, 0))
        tot += a
    # print(tot)
    for i in range(M):
        p, kaisu = heapq.heappop(h)
        tot -= -p
        p = -p // 2
        tot += p
        heapq.heappush(h, (-p, kaisu+1))
        # print(tot)
    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()
