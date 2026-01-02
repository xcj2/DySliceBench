import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()
a_array = na()

dp = [[0] * (N+1) for _ in range(N+1)]

for s in range(N-1, -1, -1):
    turn = 1 if s % 2 == 0 else -1
    for l in range(s+1):
        r = s - l
        # print(l,r,turn)
        if turn == 1:
            dp[l][r] = max(dp[l][r+1] + a_array[-(r+1)] * turn,
                           dp[l+1][r] + a_array[l] * turn)
        else:
            dp[l][r] = min(dp[l][r+1] + a_array[-(r+1)] * turn,
                           dp[l+1][r] + a_array[l] * turn)
print(dp[0][0])
