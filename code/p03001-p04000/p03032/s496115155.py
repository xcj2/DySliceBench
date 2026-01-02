#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import deque
import heapq


def argmost(a, comp, ini):
    m, n = ini, -1
    for i, v in enumerate(a):
        if comp(m, v):
            m, n = v, i
    return m, n


def solve(N: int, K: int, V: "List[int]"):
    M = min(N, K)
    m = -INF
    for A in range(M+1):
        for B in range(M-A+1):
            jueries = V[:A] + V[N-B:]
            # print("before:", jueries)
            heapq.heapify(jueries)
            for i in range(K-A-B):
                if len(jueries) > 0:
                    sute = heapq.heappop(jueries)
                    if sute >= 0:
                        heapq.heappush(jueries, sute)
                        break
            s = sum(jueries)
            # print("after:", jueries, s)
            if m < s:
                m = s
    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, V)


if __name__ == '__main__':
    main()
