import sys

sys.setrecursionlimit(10000)
mod = 1000000007


def mul(a, b):
    return ((a % mod) * (b % mod)) % mod


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y / 2) ** 2 % mod
    else:
        return power(x, y / 2) ** 2 * x % mod


def div(a, b):
    return mul(a, power(b, mod - 2))


# def gcd(a_gcd, b_gcd):
#     while b_gcd != 0:
#         a_gcd, b_gcd = b_gcd, a_gcd % b_gcd
#     return a_gcd
#
#
# def lcm(a_lcm, b_lcm):
#     return a_lcm * b // gcd(a_lcm, b_lcm)
#
#
# def max_sum(N_max_sum, a_max_sum):
#     dp = [0] * (N_max_sum + 1)
#     for i in range(N_max_sum):
#         dp[i + 1] = max(dp[i], dp[i] + a_max_sum[i])
#     return dp[N]
#
#
# def knapsack(N_knapsack, W, weight, value):
#     inf = float("inf")
#     dp = [[-inf for _ in range(W+1)] for j in range(N_knapsack + 1)]
#     for i in range(W+1):
#         dp[0][i] = 0
#
#     for i in range(N_knapsack):
#         for w in range(W+1):
#             if weight[i] <= w:
#                 dp[i+1][w] = max(dp[i][w-weight[i]]+value[i], dp[i][w])
#             else:
#                 dp[i+1][w] = dp[i][w]
#     return dp[N_knapsack][W]
#
#
# class UnionFind:
#     def __init__(self, n):
#         self.par = [i for i in range(n+1)]
#         self.rank = [0] * (n+1)
#
#     # 検索
#     def find(self, x):
#         if self.par[x] == x:
#             return x
#         else:
#             self.par[x] = self.find(self.par[x])
#             return self.par[x]
#
#     # 併合
#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)
#         if self.rank[x] < self.rank[y]:
#             self.par[x] = y
#         else:
#             self.par[y] = x
#             if self.rank[x] == self.rank[y]:
#                 self.rank[x] += 1
#
#     # 同じ集合に属するか判定
#     def same_check(self, x, y):
#         return self.find(x) == self.find(y)


ans = 0
N = int(input())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x = X[i] - X[j]
        y = Y[i] - Y[j]
        ans_loop = 0

        for first in range(N):
            for second in range(N):
                if first == second:
                    continue
                if X[first] == X[second] - x and Y[first] == Y[second] - y:
                    ans_loop += 1
                    break

        ans = max(ans, ans_loop)

print(N-ans)
