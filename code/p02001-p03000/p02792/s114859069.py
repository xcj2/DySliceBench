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
    n = input_int()


    cnt = [[0] * 10 for i in range(10)]
    for n in range(1, n + 1):
        cnt[int(str(n)[0])][int(str(n)[-1])] += 1

    ret = 0
    for i in range(10):
        for j in range(10):
            ret += cnt[i][j] * cnt[j][i]

    return ret


if __name__ == "__main__":
    print(main())
