#!/usr/bin/env python3
import sys
import heapq
from collections import deque


def solve(N: int, M: int, work: "List[List[int]]"):
    wq = deque(work)
    paytree = []
    ans = 0

    for day in range(M + 1):
        while len(wq) > 0 and wq[0][0] <= day:
            heapq.heappush(paytree, wq.popleft()[1] * (-1))
        if len(paytree) > 0:
            ans -= heapq.heappop(paytree)

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    work = [] # type: "List[List[int]]"
    for _ in range(N):
        work.append([int(next(tokens)), int(next(tokens))])
    solve(N, M, sorted(work))

if __name__ == '__main__':
    main()
