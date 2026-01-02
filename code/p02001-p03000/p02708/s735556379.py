#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, K: int):
    sums = [0] * (N + 2)
    for i in range(1, N + 2):
        sums[i] = sums[i - 1] + i
        sums[i] %= MOD

    cum = [0] * (N + 3)
    for i in range(N + 2):
        if i == 0:
            tmp = N + 1
        else:
            #tmp = (i + 1) * N - sums[i]
            #tmp = (i + 1) * N - sums[i]
            tmp = sums[N] - sums[max(0, N - i)]
            tmp -= sums[i - 1] - 1
        tmp %= MOD
        cum[i + 1] = cum[i] + tmp
        cum[i + 1] %= MOD
    #print(cum)
    ret = cum[N + 2] - cum[K]
    ret %= MOD
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
