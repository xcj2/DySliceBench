import bisect

def main():
    n = int(input())
    a = sorted([int(s) for s in input().split()])
    b = sorted([int(s) for s in input().split()])
    c = sorted([int(s) for s in input().split()])
    print(solve(n, a, b, c))

def solve(n, a, b, c):
    d = [c, b, a]
    dp = []
    dp.append([n - i for i in range(n)])
    dp.append([0 for _ in range(n)])
    dp.append([0 for _ in range(n)])

    for i in range(1, 3):
        for j in reversed(range(n)):
            k = bisect.bisect(d[i-1], d[i][j])
            if k == n:
                continue

            dp[i][j] = dp[i-1][k]
            if j != n - 1:
                dp[i][j] += dp[i][j+1]

    return dp[2][0]


def ilen(it):
    c = 0
    for _ in it:
        c += 1
    return c

main()
