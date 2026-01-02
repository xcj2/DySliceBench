#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def comb(n, k):
    if n == 0 or k == 0:
        return 1
    ret = 1
    for i in range(k):
        ret *= (n - i)
        ret //= (i + 1)
    return ret

def rec(S, K):
    #print(S, K)
    N = len(S)
    if N == 0 or K == 0 or N < K:
        return 0
    h = int(S[0])
    c = comb(N - 1, K - 1)
    ret = (9 - h) * c * (9 ** (K - 1))
    if S[0] == '0':
        ret += rec(S[1:], K)
    else:
        ret += rec(S[1:], K - 1)
    #print(S, K, ret)
    return ret

def solve(S: str, K: int):
    N = len(S)
    if N < K:
        print(0)
        return 0
    ret = comb(N, K) * (9 ** K)
    ret -= rec(S, K)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = str(next(tokens)) 
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
