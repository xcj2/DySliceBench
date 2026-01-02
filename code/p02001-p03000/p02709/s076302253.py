

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = read_ints()
    dp = [
        [0]*(N+1) for _ in range(N+1)
    ]
    AI = sorted(((a, i) for i, a in enumerate(A)), reverse=True)
    for i, (a, ix) in enumerate(AI):
        # dp[x][y] = max(dp[x-1][y]+A[x+y]*x, dp[x][y-1]+A[x+y]*y)
        # add a to the left
        for x in range(i+2):
            y = i+1-x
            if y > 0:
                dp[x][y] = max(dp[x][y], dp[x][y-1]+a*abs(N-y-ix))
            if x > 0:
                dp[x][y] = max(dp[x][y], dp[x-1][y]+a*abs(ix-x+1))
    return max(dp[i][N-i] for i in range(N+1))

if __name__ == '__main__':
    print(solve())
