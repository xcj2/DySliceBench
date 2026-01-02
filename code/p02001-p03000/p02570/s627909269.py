"""
task statement
==============

高橋君は青木君と待ち合わせをしています。
待ち合わせ場所は高橋君の家から D メートル離れた地点であり、待ち合わせの時刻は T 分後です。
高橋君は今から家を出発し、分速 S メートルで待ち合わせ場所までまっすぐ移動します。
待ち合わせに間に合うでしょうか？

io_style
-------
D T S
"""
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    d, t, s = input_int_list()
    if d / s <= t:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
