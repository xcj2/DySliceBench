#!/usr/bin/env python3
import sys
from collections import deque
import heapq

sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, K: int, V: "List[int]"):
    # 捨てるられるのはK-(A+B)
    # A, Bを全探索
    n = min(N,K)

    ans = 0
    for i in range(n+1):
        for j in range(n-i+1):
            s = V[:i] + V[::-1][:j]
            # print(i, j, V[:i], V[::-1][:j], s)
            s.sort(reverse=True)
            for k in range(max(0, K-(i+j))):
                t = s.copy()
                if(len(s) >= 1 and s[-1] < 0):
                    s.pop()

                    
            ans = max(ans, sum(s))

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
