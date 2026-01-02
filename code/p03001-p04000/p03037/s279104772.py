import math
from functools import reduce
from collections import deque

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,m = get_nums_l()

l_max = 0
r_min = n
for i in range(m):
    l,r = get_nums_l()
    if l_max < l:
        l_max = l
    if r_min > r:
        r_min = r

print(max(r_min - l_max + 1, 0))