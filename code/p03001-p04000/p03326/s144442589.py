def knapsack_weight(i,single=True):
    """
    重さが小さい時のナップサックDP
    :param single: True = 重複なし
    """
    """ dp[weight <= W] = 重さ上限を固定した時の最大価値 """
    dp_min = -float("inf")  # 総和価値の最小値
    dp = [dp_min] * (W + 1)

    for item in range(N):
        if single:
            S = range(W, weight_list[item] - 1, -1)
        else:
            S = range(weight_list[item], W + 1)
        for weight in S:
            if weight==1:
                dp[weight] = max2(price_list[i][item], dp[weight])
            else:
                dp[weight] = max2(dp[weight], dp[weight - weight_list[item]] + price_list[i][item])
    return dp[W]

import sys
input = sys.stdin.readline

def max2(x, y): return x if x > y else y
def min2(x, y): return x if x < y else y

N, W = map(int, input().split())                                # N: 品物の種類 W: 重量制限                       # N: 品物の種類 W: 重量制限 K: 個数制限

price_list = [[] for _ in range(8)]
weight_list = []
for _ in range(N):
    """ price と weight が逆転して入力されている場合有り """
    x,y,z = map(int, input().split())
    price_list[0].append(x+y+z)
    price_list[1].append(-x+y+z)
    price_list[2].append(x-y+z)
    price_list[3].append(-x-y+z)
    price_list[4].append(x+y-z)
    price_list[5].append(-x+y-z)
    price_list[6].append(x-y-z)
    price_list[7].append(-x-y-z)
weight_list = [1]*N
res = 0
for i in range(8):
    res = max(knapsack_weight(i,single=True),res)
print(res)