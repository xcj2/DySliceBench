#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


S = ST()
Q = I()

switch = True
prefix = ""
suffix = ""
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        if switch:
            switch = False
        else:
            switch = True
    else:
        if switch:
            if query[1] == "1":
                prefix = query[2] + prefix
            else:
                suffix = suffix + query[2]
        else:
            if query[1] == "1":
                suffix = suffix + query[2]
            else:
                prefix = query[2] + prefix

ans = prefix + S + suffix
if switch:
    print(ans)
else:
    print(ans[::-1])
