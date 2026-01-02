#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b

def sort_str(t):
    l = sorted(t)
    text = ''
    for i in range(len(t)):
        text += l[i]
    return text

def sum_stair(n):
    num = 0
    for i in range(1, n + 1):
        num += i
    return num

def main():
    N = int(input())
    s = [sort_str(input()) for _ in range(N)]

    t = {}
    for i in s:
        t[i] = 0
    for i in s:
        t[i] += 1
    ans = 0
    for i in t.values():
        ans += sum_stair(i - 1)
    print(ans)

if __name__ == '__main__':
    main()
