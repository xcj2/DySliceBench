#!/usr/bin/env python3

import sys

DEBUG = False

def read_int_list(sep = " "):
    return [int(s) for s in sys.stdin.readline().rstrip().split(sep)]

def read_int():
    return int(sys.stdin.readline())

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return

def solve(s, t):
    if len(t) > len(s):
        return "UNRESTORABLE"

    ans = None
    for i in range(0, len(s)):
        can_insert = True
        for j in range(0, len(t)):
            pos = i + j
            if pos >= len(s) or (s[pos] != '?' and s[pos] != t[j]):
                can_insert = False
                break
        if not can_insert:
            continue
        inserted = s[0:i] + t + s[i + len(t):]
        inserted = inserted.replace("?", "a")

        if ans is None or inserted < ans:
            ans = inserted

    if ans is None:
        return "UNRESTORABLE"
    return ans


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    print(solve(s, t))
    

if __name__ == "__main__":
    main()