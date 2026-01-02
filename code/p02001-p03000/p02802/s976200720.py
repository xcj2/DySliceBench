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
    n, m = input_to_int_map()
    ps = [input().split() for i in range(m)]

    success_cnts = [0] * (n + 1)
    wrong_cnts = [0] * (n + 1)

    for p, s in ps:
        if success_cnts[int(p)] > 0:
            continue

        if s == "AC":
            success_cnts[int(p)] += 1
        elif s == "WA":
            wrong_cnts[int(p)] += 1

    success_cnt = 0
    wrong_cnt = 0
    for i, success in enumerate(success_cnts):
        if success > 0:
            success_cnt += 1
            wrong_cnt += wrong_cnts[i]

    print(" ".join([str(success_cnt), str(wrong_cnt)]))


if __name__ == "__main__":
    main()
