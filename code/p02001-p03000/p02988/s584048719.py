#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(n: int, p: "List[int]"):
    ans = 0
    for i in range(1, n-1):
        if sorted([p[i-1], p[i], p[i+1]])[1] == p[i]:
            ans += 1

    print(ans)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, p)

if __name__ == '__main__':
    main()
