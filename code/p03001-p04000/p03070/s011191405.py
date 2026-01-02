#!/usr/bin/env python3
import sys
from collections import defaultdict
INF = float("inf")
MOD = 998244353  # type: int


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % MOD
    elif y % 2 == 0:
        return power(x, y//2)**2 % MOD
    else:
        return power(x, y//2)**2 * x % MOD


def solve(N: int, a: "List[int]"):

    S = sum(a)
    # dp = [defaultdict(int) for _ in range(N)]
    dp = [[0]*(S+1) for _ in range(N)]
    # dp2 = [defaultdict(int) for _ in range(N)]
    dp2 = [[0]*(S+1) for _ in range(N)]
    dp[0][0] = 2
    dp[0][a[0]] = 1
    dp2[0][0] = 1
    dp2[0][a[0]] = 1
    for i in range(1, N):     # i+1番目の数字まで使ったとき
        # for key in dp[i-1]:
        for key in range(S+1):
            dp[i][key] = 2*dp[i-1][key]+dp[i-1][key-a[i]]
            dp[i][key] %= MOD
            dp2[i][key] = dp2[i-1][key] + dp2[i-1][key-a[i]]
            dp2[i][key] %= MOD

    # ans = power(3, N) - sum([dp[N-1][i] for i in range(-(-S//2), S+1)])*3
    ans = power(3, N) - sum(dp[N-1][-(-S//2):])*3
    ans %= MOD
    if S % 2 == 0:              #
        ans += 3*dp2[N-1][-(-S//2)]
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
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
