# https://atcoder.jp/contests/agc008/tasks/agc008_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    x, y = input_int_list()
    if x == y:
        print(0)
    elif abs(abs(x) - abs(y)) == 0:
        print(1)
    elif (x == 0 and y > 0) or (y == 0 and x < 0):  # 0 が含まれ符号反転なし
        print(abs(abs(x) - abs(y)))
    elif (x == 0 and y < 0) or (y == 0 and x > 0):  # 0が含まれ符号反転あり
        print(abs(abs(x) - abs(y)) + 1)
    elif (x < 0 and y > 0) or (x > 0 and y < 0):  # +/-混在
        print(abs(abs(x) - abs(y)) + 1)
    elif y < x:  # y のほうが小さい
        print(abs(abs(x) - abs(y)) + 2)
    else:
        print(abs(abs(x) - abs(y)))
    return


if __name__ == "__main__":
    main()
