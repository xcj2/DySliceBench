#!/usr/bin/env python3
import sys
import heapq
input = lambda: sys.stdin.readline().strip()

def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    heapq.heapify(A)
    I = sorted(list(range(M)), key=lambda i: -C[i])
    for i in I:
        while A[0] < C[i] and B[i] > 0:
            heapq.heappop(A)
            heapq.heappush(A, C[i])
            B[i] -= 1
    print(sum(A))
    

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
