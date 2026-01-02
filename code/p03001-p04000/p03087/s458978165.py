import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

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

INF = 999999999999999999999999
MOD = 10**9+7

n,q = get_nums_l()
s = input()

ruiseki_ac = [0] * (n+1)

for i in range(n-1):
    x = 0
    if s[i] == "A" and s[i+1] == "C":
        x = 1
    ruiseki_ac[i+1] = ruiseki_ac[i] + x
ruiseki_ac[n] = ruiseki_ac[n-1]

log(ruiseki_ac)

for i in range(q):

    a,b = get_nums_l()
    print(ruiseki_ac[b-1] - ruiseki_ac[a-1])
