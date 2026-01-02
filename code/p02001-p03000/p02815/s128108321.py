import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()
C_array = na()
C_array.sort()
ans = 0
mod = 10 ** 9 + 7
dp = [C_array[0], 0]
arr2 = [0, 1]
j = 1
for i in range(N):
    j = j * 2 % mod
    arr2.append(j)

# print(dp)
cold = C_array[0]
cusum = 0
for i, c in enumerate(C_array[1:]):
    new00 = (dp[0] + cold * arr2[i + 1] + cusum *
             arr2[i] + c * arr2[i + 1]) % mod
    new01 = (dp[1] + cusum * arr2[i] + c * arr2[i + 1]) % mod
    # print(new00,new01)
    new0 = (new00 + new01) % mod
    new1 = (dp[0] + dp[1]) % mod
    dp = [new0, new1]
    # print(dp)
    cusum = (cold + cusum) % mod
    cold = c
ans = (dp[0] + dp[1]) * arr2[N + 1] % mod
print(ans)
