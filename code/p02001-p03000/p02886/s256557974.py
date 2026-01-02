#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, d: "List[int]"):
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            # print(i, j@)
            ans += d[i]*d[j]

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, d)

if __name__ == '__main__':
    main()
