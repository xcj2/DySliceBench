

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    dp[lower][i][j] - if number of ways such that one of the digit is lower and contains j non-zero digits
    """
    N = input()
    length = len(N)
    K = read_int()
    dp = [
        [[0 for _ in range(K+1)] for _ in range(length+1)]
        for _ in range(2)
    ]
    dp[False][0][0] = 1
    for i in range(1, length+1):
        dp[True][i][0] = 1
        for j in range(1, K+1):
            dp[True][i][j] = 9*dp[True][i-1][j-1]+dp[True][i-1][j]
            if int(N[i-1]) > 0:
                dp[True][i][j] += dp[False][i-1][j-1]*(int(N[i-1])-1)+dp[False][i-1][j]
                dp[False][i][j] = dp[False][i-1][j-1]
            else:
                dp[False][i][j] = dp[False][i-1][j]
    return dp[True][length][K]+dp[False][length][K]


if __name__ == '__main__':
    print(solve())
