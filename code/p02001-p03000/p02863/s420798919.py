def knapsack_weight(single=True):
    """
    重さが小さい時のナップサックDP
    :param single: True = 重複なし
    """
    """ dp[weight <= W] = 重さ上限を固定した時の最大価値 """
    dp_min = 0  # 総和価値の最小値
    dp = [dp_min] * (W + 1)

    for item in range(N):
        if single:
            S = range(W, weight_list[item] - 1, -1)
        else:
            S = range(weight_list[item], W + 1)
        for weight in S:
            if weight - weight_list[item] < T:
                dp[weight] = max2(dp[weight], dp[weight - weight_list[item]] + price_list[item])
    return max(dp[T:])

import sys
input = sys.stdin.readline


def max2(x, y):
    return x if x > y else y

def min2(x, y):
    return x if x < y else y


N, T = map(int, input().split())                                # N: 品物の種類 W: 重量制限

price_list = []
weight_list = []
data = []
for _ in range(N):
    weight, price = map(int, input().split())
    data.append((weight, price))
data.sort()
for weight, price in data:
    price_list.append(price)
    weight_list.append(weight)

max_weight = max(weight_list)

W = T + max_weight - 1

print(knapsack_weight(single=True))