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

def is_panlindrome(s):
    dprint("s: %s" % (s))
    if list(s) == list(reversed(s)):
        return True
    return False

def judge(s):
    if not is_panlindrome(s):
        return False
    if not is_panlindrome(s[0:(len(s) - 1)//2]):
        return False
    if not is_panlindrome(s[(len(s) + 3) // 2 - 1: len(s)]):
        return False
    return True


def main():
    s = read(str)
    j = judge(s)
    if j:
        print("Yes")
    else:
        print("No")

    pass


if __name__ == "__main__":
    main()