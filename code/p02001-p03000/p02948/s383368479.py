#!/usr/bin/env python3
import sys
from operator import itemgetter
from heapq import heappop,heappush

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    kyuujinn = [[] for _ in range(M+1)]
    
    for i in range(N):
        if A[i] <= M:
            kyuujinn[A[i]].append(B[i])

    answer =0
    heapque = []
    for k in kyuujinn:
        if k:
            for kk in k:
                heappush(heapque,-kk)
        
        if heapque:
            work = heappop(heapque)
            answer-= work
    print(answer)
    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
