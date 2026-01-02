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
    h, w, k = map(int, input().split())
    ch = []
    for _ in range(h):
        ch.append(next_line())

    # print(ch)

    res = 0
    for i in range(1 << h):
        for j in range(1 << w):
            count = 0
            for l in range(h):
                for m in range(w):
                    if ch[l][m] == "#" and (i & (1 << l) == 0) and (j & (1 << m) == 0):
                        count += 1
            if count == k:
                res += 1
    print(res)


if __name__ == '__main__':
    main()
