#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]"):
    
    a.sort(reverse=True)

    ans = 0
    for i in range(1, 2*N+1, 2):
        ans += a[i]
    
    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(3 * N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
