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
    a, b = input_to_int_map()
    import itertools
    _a = "".join(itertools.repeat(str(a), b))
    _b = "".join(itertools.repeat(str(b), a))
    ret = _b
    if _a < _b:
        ret = _a

    return ret


if __name__ == "__main__":
    print(main())
