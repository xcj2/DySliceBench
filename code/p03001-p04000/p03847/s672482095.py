
def read_input():
    n = int(input())
    return n


def mymod(x):
    return x % (10**9 + 7)


def submit():
    N = read_input()
    N = list(map(int, list(bin(N)[2:])))

    dp = [[0]*(3) for _ in range(len(N) + 1)]
    dp[len(N)][0] = 1

    for i in range(len(N) - 1, -1, -1):
        for s in range(3):
            for k in range(3):
                new_s = 2 * s + N[len(N) - i - 1] - k
                if new_s < 0:
                    continue
                if new_s > 2:
                    new_s = 2
                dp[i][new_s] += dp[i + 1][s]
            dp[i][0] = mymod(dp[i][0])
            dp[i][1] = mymod(dp[i][1])
            dp[i][2] = mymod(dp[i][2])

    print(mymod((dp[0][0] + dp[0][1] + dp[0][2])))


if __name__ == '__main__':
    submit()
