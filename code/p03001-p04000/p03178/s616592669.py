import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


K = ns()
D = ni()

dp = [0] * D
mod = 10 ** 9 + 7
now_mod = 0

for k in K:
    k = int(k)
    dp_old = dp
    dp = [0] * D
    for kk in range(k):
        dp[(now_mod+kk) % D] += 1
    now_mod = (now_mod + k) % D
    for i, d in enumerate(dp_old):
        for n in range(10):
            dp[(i+n) % D] += d
            dp[(i+n) % D] %= mod
    # print(now_mod, dp)
if now_mod == 0:
    dp[0] += 1
print((dp[0]-1) % mod)
