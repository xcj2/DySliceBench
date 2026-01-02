#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32
from functools import lru_cache



def solve(N: int, K: int):
    @lru_cache(None)
    def f(n: int, k:int):
        if n < 10:
            if k == 0:
                # n <= 9 and k == 0のときは0個
                return 1
            elif k == 1:
                # n <= 9 and k == 1のときは、1-9の9個
                return n
            else:
                # n <= 9でk == 2以上の時は、解がない
                return 0

        return f(n//10, k-1)*(n%10) + f(n//10-1, k-1) *(9-n%10) + f(n//10, k)


    print(f(N, K))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
