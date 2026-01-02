#!/usr/bin/env python3
import sys
from collections import deque
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(K: int):

    h = deque([])

    for i in range(1, 10):
        h.append(i)

    for i in range(K-1):
        s = h.popleft()
        for j in range(-1, 2):
            add = (s % 10)+j
            if 0 <= add <= 9:
                h.append(s*10+add)
    print(h.popleft())
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()
