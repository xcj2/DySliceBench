import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, M = read_ints()
    S = read_ints()
    T = read_ints()
    dp = [
        [0 for _ in range(M+1)] for _ in range(N+1)
    ]
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1
    for j in range(1, M+1):
        dp[0][j] = 1
    modulo = 10**9+7
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = (dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1])%modulo
            if S[i-1] == T[j-1]:
                dp[i][j] = (dp[i][j]+dp[i-1][j-1])%modulo
    return dp[N][M]


if __name__ == '__main__':
    print(solve())
