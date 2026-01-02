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

def keta(n):
    a = 0
    while (n > 0):
        a += 1
        n = n//10
    return a

n = int(input())

ans=0
for x in range(1,n+1):
    if keta(x) % 2 == 1:
        ans += 1

print(ans)
