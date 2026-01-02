#!/usr/bin/env python3
import sys

a = [0, 2,5,5,4,5,6,3,7,6]

def solve(n: int, m: int, A: "List[int]"):
    dp = [-1] * (n + 1)
    dp[0] = 0
    A.sort(reverse=True)
    for c in A:
        for i in range(n + 1):
            if i - a[c] >= 0 and dp[i - a[c]] >= 0:
                dp[i] = max(dp[i], dp[i - a[c]] * 10 + c)
    print(dp[n])
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
