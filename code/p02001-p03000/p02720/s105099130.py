#!/usr/bin/env python3

import sys

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return

def is_luun(i):
    last_digit = i % 10
    i //= 10
    while i > 0:
        if abs((i % 10) - last_digit) > 1:
            return False
        last_digit = i % 10
        i //= 10
    return True

next_luun_memo = {}

def next_luun(n):
    if n in next_luun_memo:
        dprint("memoed: %d -> %d" % (n, next_luun_memo[n]))
        return next_luun_memo[n]
    if n < 10:
        dprint("here")
        next_luun_memo[n] = n + 1
        return n + 1
    first = n % 10
    tenth = (n // 10) % 10
    if first < 9 and abs(first + 1 - tenth) <= 1:
        next_luun_memo[n] = n + 1
        return n + 1

    ans_tenth = next_luun(n // 10)
    dprint("ans_tenth: %d" % ans_tenth)
    ans_first = min(abs(ans_tenth % 10 - 1), ans_tenth % 10)
    dprint("ans_first: %d" % ans_first)
    ans = ans_tenth * 10 + ans_first
    next_luun_memo[n] = ans
    return ans


def main():
    k = read(int)

    i = 1
    luun = 1
    while i < k:
        dprint("%dth luun: %d" % (i, luun))
        luun = next_luun(luun)
        i += 1
    dprint("%dth luun: %d" % (i, luun))
    print(luun)

if __name__ == "__main__":
    main()