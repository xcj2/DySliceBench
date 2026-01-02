def warshall_floyd(dp, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def check(dp, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    return False
    return True


def main():
    v, e = map(int, input().split())
    INF = 10 ** 10
    MAX = 2 * (10 ** 7)
    MIN = -2 * (10 ** 7)
    dp = [[INF for i in range(v)] for j in range(v)]
    for i in range(e):
        s, t, d = map(int, input().split())
        dp[s][t] = d
    for i in range(v):
        for j in range(v):
            if i == j:
                dp[i][j] = 0

    warshall_floyd(dp, v)
    if not check(dp, v):
        print("NEGATIVE CYCLE")
    else:
        for i in range(v):
            for j in range(v):
                if j > 0:
                    print(end=' ') 
                if dp[i][j] > MAX * v or dp[i][j] < MIN * v:
                    print("INF", end='')
                else:
                    print(dp[i][j], end='')
            print()


if __name__ == '__main__':
    main()

