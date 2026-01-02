def coin(larger=False, single=False):
    """
    ナップサックに入れる重さが W 丁度になる時の価値の最小値
    :param single: True = 重複なし

    dp[weight <= W+1] = 重さを固定した時の最小価値
    dp[W+1] = 重さがWより大きい時の最小価値
    """
    W2 = W + 1              # dp[W+1] に W より大きい時の全ての場合の情報を持たせる
    dp_max = float("inf")   # 総和価値の最大値
    dp = [dp_max] * (W2 + 1)
    dp[0] = 0               # 重さ 0 の時は価値 0

    for item in range(N):
        if single:
            S = range(W2, weight_list[item] - 1, -1)
        else:
            S = range(W2)
        for weight in S:
            dp[min2(weight + weight_list[item], W2)] = min2(dp[min2(weight + weight_list[item], W2)], dp[weight] + cost_list[item])
    if larger:
        return min(dp[w] for w in range(W, W2+1))
    else:
        return dp[W]

#######################################################################################################
import sys
input = sys.stdin.readline


def max2(x, y):
    return x if x > y else y

def min2(x, y):
    return x if x < y else y

W, N = map(int, input().split())                                # N: 品物の種類 W: 重量制限

# cost_list = []
# weight_list = []
# for _ in range(N):
#     """ cost と weight が逆転して入力されている場合有り """
#     weight, cost = map(int, input().split())
#     cost_list.append(cost)
#     weight_list.append(weight)

cost_list = [1]*N
weight_list = list(map(int, input().split()))

print(coin(single=False))


############################################################################################
