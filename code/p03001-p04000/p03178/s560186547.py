

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    _ _ 

    dp[i][j][one_of_previous_number_is_lower] = count of remainder j up to i-th digit, 0 <= j < D

    dp[i][(j+digit)%D][True] += dp[i-1][j][True] + dp[i-1][j][False] digit < K[i]
    dp[i][(j+digit)%D][False] += dp[i-1][j][False]        digit == K[i]
    """
    K = list(map(int, input().strip()))
    D = read_int()
    dp = [[[0, 0] for _ in range(D)]
           for _ in range(len(K)+1)]
    dp[0][0][0] = 1
    modulo = 10**9+7
    for i in range(len(K)):
        for j in range(D):
            for digit in range(10):
                dp[i+1][(j+digit)%D][True] += dp[i][j][True]
                if digit < K[i]:
                    dp[i+1][(j+digit)%D][True] += dp[i][j][False]
                if digit == K[i]:
                    dp[i+1][(j+digit)%D][False] += dp[i][j][False]
                dp[i+1][(j+digit)%D][False] %= modulo
                dp[i+1][(j+digit)%D][True] %= modulo
    return (dp[-1][0][0]+dp[-1][0][1]-1)%modulo


if __name__ == '__main__':
    print(solve())
