#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]"):
    sv = sum(a)/N
    p = 0
    s = INF
    for i in range(N):
        if abs(sv - a[i]) < s:
            p = i
            s = abs(sv - a[i])
        
    print(p)
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
