#!/usr/bin/env python3
import sys, heapq
sys.setrecursionlimit(300000)


def solve(N: int, M: int, A: "List[int]"):
    h = []
    for i in range(N):
        heapq.heappush(h, -A[i])
    for i in range(M):
        tmp = -(heapq.heappop(h))
        tmp //= 2
        heapq.heappush(h, -tmp)
    ret = sum(h)
    ret = -ret
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
