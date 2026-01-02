#!/usr/bin/env python3
import sys
INF = float("inf")
from bisect import bisect_left


def solve(N: int, K: int, A: "List[int]", F: "List[int]"):
    A.sort()
    F.sort(reverse=True)
    h = []
    for a, f in zip(A, F):
        h.append((a*f, a, f))
    h.sort()
    maxtime = h[-1][0]

    def isOK(y):
        i = bisect_left(h, (y+1, -1, -1))
        counter = 0
        # print(h[i:])
        for p, a, f in h[i:]:
            counter += a-y//f
        return counter <= K

    def binary_search(x):
        ng = -1
        ok = len(x)
        while abs(ok - ng) > 1:
            mid = (ok + ng)//2
            # print("mid: {}, in ({}, {})".format(mid, ng, ok))
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ng, ok

    ng, ok = binary_search(range(maxtime))
    print(ok)

    # while k > 0:
    #     p1, a1, f1 = heapq.heappop(h)
    #     p2, a2, f2 = heapq.heappop(h)
    #     p1, p2 = -p1, -p2
    #     sub = min(a1 - math.ceil((p2/f1)-1), k)
    #     a1 -= sub
    #     k -= sub
    #     heapq.heappush(h, (-a1*f1, a1, f1))
    #     heapq.heappush(h, (-a2*f2, a2, f2))
    # # print(h)
    # p, a, f = heapq.heappop(h)
    # print(-p)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    F = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A, F)


if __name__ == '__main__':
    main()
