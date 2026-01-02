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

s = input()

win = 0
lose = 0
for c in s:
    if c == "o":
        win += 1
    else:
        lose += 1

nokori = 15 - win - lose

print("YES" if win+nokori >= 8 else "NO")