def main():
    N, W = map(int, input().split())
    wv = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans1 = f(N, W, wv)
    ans2 = simple(N, W, wv)

    # assert ans == ans2

    print(ans2)


def simple(N, W, wv):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i, (w, v) in enumerate(wv, 1):
        for _w in range(1, W + 1):
            bef = dp[i-1][_w]
            dp[i][_w] = bef

            # 入れ替え
            if _w - w >= 0:
                changed = dp[i-1][_w - w] + v
                dp[i][_w] = max(bef, changed)

    ans = dp[N][W]
    return ans


def f(N, W, wv):
    """
    品物100を入れる入れないの 2^100 試せばOKだが、無理

    Nの入れる個数
        0から100
        正確にはN個までの選択なので、N個入れていないときもある
    最終容量     
        0から10^5
        正確にはWまでの重さなので、W以下のときもある
    10^7なら間に合いそう

    追加できるならば、追加してみる
    追加するものと入れ替えを試してみる
        追加の重さを引いたときの価値
        前の価値まま
            の大きい方
    """
    dp = [[-float("inf")] * (W + 1)
          for _ in range(N + 1)]

    # 品物を入れていないならば、価値はない
    # 品物を入れていないならば、重さはないので、価値はない
    # wi, vi >= 1 より
    dp[0] = [0] * (W + 1)
    for i in range(1, N + 1):
        dp[i][0] = 0

    for i, (w, v) in enumerate(wv, 1):
        for _w in range(1, W + 1):
            # まずは1つ前で補完, 価値は品物追加すれば単調増加なのでOK
            bef = dp[i-1][_w]
            dp[i][_w] = bef

            # 追加
            # 品物ループの内側にある重さのループではあるが、
            # このループでは何回も追加しないようになっている
            if _w + w <= W:
                changed = dp[i-1][_w] + v
                bef = dp[i-1][_w + w]
                # 補完と入れ替えを合わせると追加も兼ねている？
                # dp[i][_w + w] = max(bef, changed)

            # 入れ替え
            if _w - w >= 0:
                changed = dp[i-1][_w - w] + v
                bef = dp[i-1][_w]
                dp[i][_w] = max(bef, changed)

    # 補完により必ず[N][W] で最大
    # ans = max(dp[N])
    ans = dp[N][W]

    # from pprint import pprint
    # import sys
    # pprint(dp, stream=sys.stderr)
    return ans


if __name__ == "__main__":
    main()
