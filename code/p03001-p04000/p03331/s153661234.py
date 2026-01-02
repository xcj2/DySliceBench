#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    ans = INF
    for a in range(1,N):
        b = N-a
        ans = min(
            ans, 
            sum(map(int, list(str(a))))
            +sum(map(int, list(str(b))))
        )
    
    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
