#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    S = input()
    Q = II()
    
    direction = 1
    pre = []
    sur = []

    for i in range(Q):
        query = input()
        if query == '1':
            direction *= -1
        else:
            _, f, c = query.split()
            if direction == 1:
                if f == '1':
                    pre.append(c)
                else:
                    sur.append(c)
            else:
                if f == '1':
                    sur.append(c)
                else:
                    pre.append(c)

    if direction == 1:
        ans = "".join(pre[::-1]) + S + "".join(sur)
    else:
        ans = "".join(sur[::-1]) + "".join(S[::-1]) + "".join(pre)
    print(ans)

main()
