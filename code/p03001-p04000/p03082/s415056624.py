#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, X: int, S: "List[int]"):
    fact = [0] * (N + 1)
    fact[1] = 1
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i

    memo = [[-1] * (X + 1) for _ in range(N + 1)]
    S.sort(reverse=True)
    def rec(idx, x, d=0):
        #suf = ''.join(['  ' for _ in range(d)])
        #print(suf, idx, x)
        if memo[idx][x] >= 0:
            return memo[idx][x]
        if idx == N - 1:
            memo[idx][x] = x % S[idx]
            return memo[idx][x]
        ret = 0

        ret += rec(idx + 1, x, d + 1) * (N - idx - 1)
        ret += rec(idx + 1, x % S[idx], d + 1)

        #for i in range(idx + 1, N):
        #    ret += rec(i, x, d + 1) * (N - idx - 1)
        #    ret += rec(i, x % S[idx], d + 1)
        #print(suf, idx, x, ' =>', ret)
        memo[idx][x] = ret
        return ret

    ret = rec(0, X)
    print(ret % MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    S = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, X, S)

if __name__ == '__main__':
    main()
