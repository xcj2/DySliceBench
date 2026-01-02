# -*- coding: utf-8 -*-

# 入力を整数に変換して受け取る
def input_int():
    return int(input())


# マイナス1した値を返却
def int1(x):
    return int(x) - 1


# 半角スペース区切り入力をIntに変換してMapで受け取る
def input_to_int_map():
    return map(int, input().split())


# 半角スペース区切り入力をIntに変換して受け取る
def input_to_int_tuple():
    return tuple(map(int, input().split()))


# 半角スペース区切り入力をIntに変換してマイナス1した値を受け取る
def input_to_int_tuple_minus1():
    return tuple(map(int1, input().split()))


def main():
    h, n = input_to_int_map()
    ab = [input_to_int_tuple() for i in range(n)]

    x = max(a for a, b in ab)

    dp = [0] * (h + x)
    for i in range(1, h + 1):

        dp[i] = min(dp[i - a] + b for a, b in ab)

    return dp[h]


if __name__ == "__main__":
    print(main())
