#!/usr/bin/env python3
import sys
# from functools import total_ordering
import heapq

from collections import Counter as cl

def solve(N: int, X: int, Y: int):

    def dis(a,b):
        fw = abs(a-b)
        bw1 = abs(X-a)+abs(Y-b)+1
        bw2 = abs(X-b)+abs(Y-a)+1
        bw = min(bw1,bw2)
        return min(fw, bw)
    
    dist_l = [0]*(N-1)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            dist_l[dis(i,j)-1] += 1


    print("\n".join(map(str, dist_l)))




def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)

if __name__ == '__main__':
    main()
