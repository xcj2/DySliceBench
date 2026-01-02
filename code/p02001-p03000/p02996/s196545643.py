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
lines = sys.stdin.readlines()

works = [None]*n
_ = 0
for l in lines:
    works[_] = tuple(map(int, l.split(" ")))
    _ += 1

works.sort(key=lambda w:w[1], reverse=True)


time = 9999999999999999999999999
for i,w in enumerate(works):
    time = min(time,w[1]) - w[0]

print("Yes" if time >= 0 else "No")