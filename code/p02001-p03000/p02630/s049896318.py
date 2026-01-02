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
    ar = next_int_array_one_line()
    num = [0] * 100001
    for a in ar:
        num[a] += 1
    q = next_int()
    res = 0
    for i in range(len(num)):
        res += num[i] * i

    for i in range(q):
        b, c = map(int, input().split())
        res += (c-b) * num[b]
        num[c] += num[b]
        num[b] = 0
        print(res)


if __name__ == '__main__':
    main()
