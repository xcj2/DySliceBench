import math

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()


def point(i, hand):
    if i >= N: return 0
    t = T[i]
    if t == 'r': return P if hand == 2 else 0
    if t == 's': return R if hand == 0 else 0
    if t == 'p': return S if hand == 1 else 0
    return 0


def max_value(head_index):
    l = math.ceil(N / K)
    dp = [[0, 0, 0] for i in range(l)]
    dp[0] = [
      point(head_index, 0),
      point(head_index, 1),
      point(head_index, 2)
    ]
    for i in range(1, l):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + point(head_index + i * K, 0)
        dp[i][1] = max(dp[i - 1][2], dp[i - 1][0]) + point(head_index + i * K, 1)
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + point(head_index + i * K, 2)
    return max(dp[l - 1])


def solve():
    ans = 0

    for i in range(K):
        ans += max_value(i)

    return ans


print(solve())
