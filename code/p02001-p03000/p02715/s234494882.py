#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, K: int):
    ret = 0
    counts = [0] * (K + 1)
    for i in range(1, K + 1)[::-1]:
        c = K // i
        cnt = pow(c, N, MOD)
        j = 2
        while i * j <= K:
            cnt -= counts[i * j]
            j += 1
        ret += cnt * i
        ret %= MOD
        counts[i] = cnt
    #print(counts)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
