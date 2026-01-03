# https://atcoder.jp/contests/arc080/tasks/arc080_a
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def get_2(i):
    cnt = 0
    while i % 2 == 0 and i > 0:
        i = i // 2
        cnt += 1
    return cnt


def main():
    n = input_int()
    A = input_int_list()
    odd = 0
    even_4 = 0
    even_2 = 0
    for a in A:
        if a % 4 == 0:
            even_4 += 1
        elif a % 2 == 0:
            even_2 += 1
        else:
            odd += 1
    if even_4 >= odd:
        print("Yes")
    elif odd == 0 and even_2 > 1:
        print("Yes")
    elif odd == 0 and even_4 == 0 and even_2 == 1:
        print("No")
    elif even_4 == odd - 1 and even_2 == 0:
        print("Yes")
    elif even_4 == odd - 1 and even_2 > 0:
        print("No")
    elif even_4 < odd - 1:
        print("No")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
