#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(K: int):
    dp = [[-1] * (K + 1) for _ in range(K + 1)]
    def gcd(a, b):
        if dp[a][b] >= 0:
            return dp[a][b]
        else:
            ret = a if b == 0 else gcd(b, a % b)
        dp[a][b] = ret
        return ret
    ret = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            for k in range(1, K + 1):
                tmp = gcd(i, j)
                ret += gcd(tmp, k)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
