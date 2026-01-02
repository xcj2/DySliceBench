# -*- coding: utf-8 -*-

import sys
import os
import math

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def interval(a, m):
    cnt = 0
    x = 1
    while True:
        x = (a * x) % m
        cnt += 1
        if x == 1:
            return cnt

for s in sys.stdin:
    a1, m1, a2, m2, a3, m3 = map(int, s.split())
    if sum([a1, m1, a2, m2, a3, m3]) == 0:
        break

    x_num = interval(a1, m1)
    y_num = interval(a2, m2)
    z_num = interval(a3, m3)

    a = lcm(x_num, y_num)
    b = lcm(a, z_num)
    print(b)