#####################################################################################################
##### コイン問題
#####################################################################################################
"""

ベンチマーク
コイン問題 (※ larger = False): http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4696859#1
E - Crested Ibis vs Monster (※ larger = True): https://atcoder.jp/contests/abc153/submissions/15396586

"""


def coin(larger=False, single=False):
    """
    ナップサックに入れる重さが W 丁度になる時の価値の最小値
    :param larger: False = (重さ = W)の時の最小価値
                   True  = (重さ =< W)の時の最小価値
    :param single: False = 重複あり

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

W = int(input())
cost_list = [1]
weight_list = [1]
p = 6
while p<=W:
    cost_list.append(1)
    weight_list.append(p)
    p *= 6
p = 9
while p<=W:
    cost_list.append(1)
    weight_list.append(p)
    p *= 9
N = len(weight_list)

print(coin(larger=False, single=False))
