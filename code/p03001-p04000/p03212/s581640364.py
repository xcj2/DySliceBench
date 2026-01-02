# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import _collections
import string

class cin():
    def int():
        return int(sys.stdin.readline().rstrip())
    def string():
        return sys.stdin.readline().rstrip()
    def mapInt():
        return [int(x) for x in cin.string().split()]
    def stringList(n):
        return [input() for i in range(n)]
    def intListList(n):
        return [cin.mapInt() for i in range(n)]

class Util():
    def roundUp(a,b):
        return -(-a // b)
    def toUpperMultiple(a,x):
        return Util.round_up(a,x) * x
    def toLowerMultiple(a,x):
        return (a // x) * x
class Math():
    def gcd(a,b):
        if b == 0:
            return a
        return Math.gcd(b,a % b)

N = 0
ans = 0
def rec(n):
    global ans
    if n > N:
        return
    m = _collections.defaultdict(int)
    for i in sorted(str(n)):
        m[i] += 1
    if m["3"] > 0 and m["5"] > 0 and m["7"] > 0:
        ans += 1
    rec(n * 10 + 3)
    rec(n * 10 + 5)
    rec(n * 10 + 7)

def main():
    global N
    N = cin.int()
    rec(3)
    rec(5)
    rec(7)
    print(ans)
    return
if __name__ == "__main__":
    main()
