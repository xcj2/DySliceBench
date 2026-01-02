import sys
input = sys.stdin.readline


def main():
    
    def knapsack_price(single=True):
        """
        重さが小さい時のナップサックDP
        :param single: True = 重複なし
        """
        """ dp[price <= V] = 価値を固定した時の最小重量 """
        V = sum(price_list)
        dp_max = W + 1
        dp = [dp_max] * (V + 1)
        dp[0] = 0  # 境界条件：　価値0 の時は重さは0

        for item in range(N):
            if single:
                S = reversed(range(price_list[item], V + 1))
            else:
                S = range(price_list[item], V + 1)
            for price in S:
                dp[price] = min2(dp[price], dp[price - price_list[item]] + weight_list[item])
        return max(price for price in range(V + 1) if dp[price] <= W)

    #######################################################################################################


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

    N, W = map(int, input().split())  # N: 品物の種類 W: 重量制限

    price_list = []
    weight_list = []
    for _ in range(N):
        """ price と weight が逆転して入力されている場合有り """
        weight, price = map(int, input().split())
        price_list.append(price)
        weight_list.append(weight)

    print(knapsack_price(single=True))

if __name__ == '__main__':
    main()