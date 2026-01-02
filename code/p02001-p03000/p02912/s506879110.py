#!/usr/bin/env python3
import sys
import heapq

def solve(N: int, M: int, A: "List[int]"):

    while True:
        tmp = heapq.heappop(A) * -1
        heapq.heappush(A,tmp // 2 * -1)
        M -= 1
        if M == 0:
            break
    
    print(sum(A) * -1)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = []
    heapq.heapify(A)
    for i in range(N):
        heapq.heappush(A,int(next(tokens)) * -1)

    solve(N, M, A)

if __name__ == '__main__':
    main()
