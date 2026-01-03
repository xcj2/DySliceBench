import functools

import os
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def inp():
    return int(input())


def inpf():
    return float(input())


def inps():
    return input()


def inl():
    return list(map(int, input().split()))


def inlf():
    return list(map(float, input().split()))


def inls():
    return input().split()


def inpm(line):
    return [inp() for _ in range(line)]


def inpfm(line):
    return [inpf() for _ in range(line)]


def inpsm(line):
    return [inps() for _ in range(line)]


def inlm(line):
    return [inl() for _ in range(line)]


def inlfm(line):
    return [inlf() for _ in range(line)]


def inlsm(line):
    return [inls() for _ in range(line)]


def Yesif(cond):
    print('Yes' if cond else 'No')


def YESIF(cond):
    print('YES' if cond else 'NO')


def yesif(cond):
    print('yes' if cond else 'no')



print('vowel' if input() in 'aiueo' else 'consonant')
