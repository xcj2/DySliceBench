#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int):
    
    from math import floor, ceil
    ans = []
    for i in range(1, 20000):
        if floor(i*0.08) == A and floor(i*0.1) == B:
            ans.append(i)

    ans.sort()
    # print(ans)
    if len(ans) != 0:
        print(ans[0])
    else:
        print(-1)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
