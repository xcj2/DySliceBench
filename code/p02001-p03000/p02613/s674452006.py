#!/usr/bin/env python3


def next_line():
    return input()


def next_int():
    return int(input())


def next_int_array_one_line():
    return list(map(int, input().split()))


def next_int_array_multi_lines(size):
    return [int(input()) for _ in range(size)]


def next_str_array(size):
    return [input() for _ in range(size)]


def main():
    n = next_int()
    str = ["AC", "WA", "TLE", "RE"]
    awtr = [0] * 4
    for _ in range(n):
        s = next_line()
        if s == "AC":
            awtr[0] += 1
        elif s == "WA":
            awtr[1] += 1
        elif s == "TLE":
            awtr[2] += 1
        else:
            awtr[3] += 1
    for i in range(4):
        print(str[i] + " x ", end="")
        print(awtr[i])


if __name__ == '__main__':
    main()
