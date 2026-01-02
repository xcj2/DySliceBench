#!/usr/bin/env python3
import sys
from math import ceil
from itertools import chain

def solve(N: int, K: int, V: "List[int]"):
    # i: num to pick, j: num to pick from left
    ans = -10**10
    for i in range(min(K+1, N+1)):
        max_n = min(K-i, i)
        for j in range(i+1):
            V2 = sorted(chain(V[:j], V[N-(i-j):]))
            k=0
            while True:
                if k>=max_n or V2[k]>=0:
                    break
                k+=1
            ans = max(sum(V2[k:]), ans)
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
