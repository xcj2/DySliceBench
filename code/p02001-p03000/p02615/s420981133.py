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
    ar = list(reversed(sorted(next_int_array_one_line())))
    # print(ar)
    res = ar[0]
    n -= 2
    use = 1
    while n > 0:
        if n >= 2:
            res += ar[use] * 2
            n -= 2
            use += 1
        else:
            res += ar[use]
            n -= 1
    print(res)


if __name__ == '__main__':
    main()
