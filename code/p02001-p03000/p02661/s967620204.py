import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

from statistics import median

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

n = int(input())
AB = []
for _ in range(n):
    AB.append(get_nums_l())
A = [ ab[0] for ab in AB ]
B = [ ab[1] for ab in AB ]

if n%2 == 1:
    min_of_med = median(A)
    max_of_med = median(B)
    print(max_of_med - min_of_med + 1)

else:
    A.sort()
    B.sort()
    min_of_med = A[n//2 - 1] + A[n//2]
    max_of_med = B[n//2 - 1] + B[n//2]
    print(max_of_med - min_of_med + 1)
