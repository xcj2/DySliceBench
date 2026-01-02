#!/usr/bin/env python3
import sys
import functools
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, K: int):

    def NN(a):
        return K//a

    @functools.lru_cache(maxsize=None)
    def f(a):
        ans = pow(NN(a), N, MOD)
        for i in range(2, K+1):
            if i*a > K:
                break
            ans -= f(i*a)
            ans %= MOD
        return ans % MOD

    ans = 0
    for i in range(1, K+1):
        # print(i*f(i))
        ans += i*f(i)
        ans %= MOD
    print(ans)

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
