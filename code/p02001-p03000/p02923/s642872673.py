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

n = int(input())
hhh = get_nums_l()

cant = []

prev = 9999999999999999999
for i,h in enumerate(hhh):
    if prev < h:
        cant.append(i-1)
    prev = h
cant.append(n-1)


prev = -1
max_ = 0
for c in cant:
    move = c - prev - 1
    if max_ < move:
        max_ = move
    prev = c

print(max_)