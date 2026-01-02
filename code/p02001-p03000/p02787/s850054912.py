def knapsack_weight(single=True):
    """
    重さが小さい時のナップサックDP
    :param single: True = 重複なし
    """
    """ dp[weight <= W] = 重さを固定した時の最小価値 """
    weight_max = max(weight_list)
    price_max = max(price_list)
    W2 = W + weight_max
    dp_max = float("inf")  # 総和価値の最大値
    dp = [dp_max] * W2
    dp[0] = 0               # 重さ 0 の時は価値 0

    for item in range(N):
        if single:
            S = range(W2, weight_list[item] - 1, -1)
        else:
            S = range(weight_list[item], W2)
        for weight in S:
            dp[weight] = min2(dp[weight], dp[weight - weight_list[item]] + price_list[item])
    return min(dp[w] for w in range(W, W2))

#######################################################################################################
import sys
input = sys.stdin.readline


def max2(x, y):
    """ pythonの組み込み関数 max は2変数に対しては遅い！！ """
    if x > y:
        return x
    else:
        return y

def min2(x, y):
    """ pythonの組み込み関数 min は2変数に対しては遅い！！ """
    if x < y:
        return x
    else:
        return y


W, N = map(int, input().split())                                # N: 品物の種類 W: 重量制限

price_list = []
weight_list = []
for _ in range(N):
    """ price と weight が逆転して入力されている場合有り """
    weight, price = map(int, input().split())
    price_list.append(price)
    weight_list.append(weight)


print(knapsack_weight(single=False))


############################################################################################
