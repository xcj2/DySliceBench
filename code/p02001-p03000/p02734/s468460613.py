# -*- coding: utf-8 -*-
import sys
input = sys.stdin.buffer.readline


def read_int_n():
    return list(map(int, input().split()))


def slv(N, S, A):
    M = 998244353
    ans = 0

    dp = [0] * (S+1)
    for a in A:
        dp[0] += 1
        ndp = [0] * (S+1)
        for j in range(S+1):
            ndp[j] += dp[j]
            ndp[j] %= M
            if j+a <= S:
                ndp[j+a] += dp[j]
                ndp[j+a] %= M
        dp = ndp
        ans += dp[S]
        ans %= M

    return ans


def main():
    N, S = read_int_n()
    A = read_int_n()
    print(slv(N, S, A))


if __name__ == '__main__':
    main()
