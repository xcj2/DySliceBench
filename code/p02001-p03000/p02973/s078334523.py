#!/usr/bin/env python3
import sys
from collections import deque
from bisect import bisect_left

def solve(N: int, A: "List[int]"):
    deq = deque([-1])

    for i in range(N):
        index = bisect_left(deq,A[i])
        if index == 0:
            deq.appendleft(A[i])
        else:
            deq[index-1] = A[i]
    print(len(deq))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
