import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,l = get_nums_l()

if (l <= 0 and (l+n-1) >= 0):
    print(sum(range(l, l+n)))
elif (l+n-1) < 0:
    print(sum(range(l, l+n-1)))
else:
    print(sum(range(l+1, l+n)))