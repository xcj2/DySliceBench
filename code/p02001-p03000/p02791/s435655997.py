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
    p = input_to_int_tuple()

    cnt = 0
    pre_min = 10 ** 6
    for i in range(n):

        if i == 0 or p[i] <= pre_min:
            cnt += 1

        pre_min = min(pre_min, p[i])

        # temp = True
        # for j in range(i):
        #     if p[i] > p[j]:
        #         temp = False
        #         break
        # if temp:
        #     cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
