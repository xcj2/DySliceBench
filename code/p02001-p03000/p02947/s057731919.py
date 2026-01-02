#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    counter = cl.Counter()
    for i in range(N):
        s = input()
        S = []

        for char in s:
            S.append(char)
        S.sort()
        
        s = "".join(S)
        counter.update({s:1})
    ans = 0

    for item, count in counter.items():
        ans += count * (count - 1) / 2
    print(int(ans))

main()
