#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, X: "List[int]"):
    ans = INF
    for i in range(1, 101):
        cost = sum([(i-X[j])**2 for j in range(N)])
        ans = min(ans, cost)

    print(ans)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()
