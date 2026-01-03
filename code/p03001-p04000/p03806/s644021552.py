import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def read_into(*A):
    for arr, a in zip(A, read_ints()):
        arr.append(a)


def solve():
    """
    dp[400][400] = 160.000*10 = 1.600.000

    dp[x+a[i]][y+b[i]] = min(dp[x+a[i]][y+b[i]], c[i]+dp[x][y])
    dp[0][0] = 0
    """
    n, ma, mb = read_ints()
    A, B, C = [], [], []
    for _ in range(n):
        read_into(A, B, C)
    dp_upper_A, dp_upper_B = max(A)*n+1, max(B)*n+1
    dp = [
        [[math.inf]*dp_upper_B for _ in range(dp_upper_A)] for _ in range(n+1)
    ]
    dp[0][0][0] = 0
    for i in range(n):
        for x in range(dp_upper_A):
            for y in range(dp_upper_B):
                if dp[i][x][y] == math.inf:
                    continue
                dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])
                dp[i+1][x+A[i]][y+B[i]] = min(dp[i+1][x+A[i]][y+B[i]], C[i]+dp[i][x][y])
    i = 1
    min_cost = math.inf
    while i*ma < dp_upper_A and i*mb < dp_upper_B:
        min_cost = min(min_cost, dp[n][i*ma][i*mb])
        i += 1
    return -1 if min_cost == math.inf else min_cost


if __name__ == '__main__':
    print(solve())
