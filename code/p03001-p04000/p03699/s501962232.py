#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, s: "List[int]"):
    mx = 10000
    dp = [False] * (mx + 1)
    dp[0] = True
    for v in s:
        for i in range(mx, -1, -1):
            if dp[i] and i + v <= mx:
                dp[i + v] = True
    ret = 0
    for i in range(mx, -1, -1):
        if dp[i] and i % 10 > 0:
            ret = i
            break
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, s)

if __name__ == '__main__':
    main()
