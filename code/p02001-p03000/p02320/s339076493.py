def knapsack_weight_num():
    """
   　各品物の個数に上限がある場合
    """
    """ dp[weight <= W] = 重さ上限を固定した時の最大価値 """
    dp_min = 0  # 総和価値の最小値
    dp = [dp_min] * (W + 1)

    for item in range(N):
        S = range(W, weight_list[item] - 1, -1)
        for weight in S:
            dp[weight] = max2(dp[weight], dp[weight - weight_list[item]] + price_list[item])
    return dp[W]

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



N, W = map(int, input().split())                                # N: 品物の種類 W: 重量制限


price_list = []
weight_list = []

for _ in range(N):
    # weight, price, cnt = map(int, input().split())
    price, weight, cnt = map(int, input().split())              # cnt: 各品物の個数の上限
    c = 1
    while c <= cnt:
        price_list.append(price*c)
        weight_list.append(weight*c)
        cnt -= c
        c <<= 1
    if cnt:
        price_list.append(price*cnt)
        weight_list.append(weight*cnt)


N = len(price_list)                                              # 品物の種類が変わってる

print(knapsack_weight_num())
