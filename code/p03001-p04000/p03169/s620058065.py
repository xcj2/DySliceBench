import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()
a_array = na()
cnt = [0] * 3
for a in a_array:
    cnt[a-1] += 1

dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

for sushi in range(1, N+1):
    for k in range(sushi+1):
        for j in range(0, sushi-k+1):
            i = sushi-k-j
            if i != 0:
                dp[i][j][k] += dp[i-1][j][k] * i / sushi
            if j != 0:
                dp[i][j][k] += dp[i+1][j-1][k] * j / sushi
            if k != 0:
                dp[i][j][k] += dp[i][j+1][k-1] * k / sushi
            dp[i][j][k] += N / sushi

print(dp[cnt[0]][cnt[1]][cnt[2]])
