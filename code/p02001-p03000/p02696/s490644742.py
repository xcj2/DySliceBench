import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

MOD = 10**9+7

a,b,n = get_nums_l()

def f(a,b,x):
    return (a*x)//b - a * (x//b)

def solve(a,b,n):
    m = -999999999999
    mi = 0
    for x in range(n+1):
        y = f(a,b,x)
        if m < y:
            m = y
            mi = x
    return m,mi

print(f(a,b,min(n,b-1)))
