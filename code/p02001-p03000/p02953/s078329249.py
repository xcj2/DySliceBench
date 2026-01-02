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

next = 999999999999
for i in range(n-1,-1, -1):
    now = hhh[i]
    if now > next:
        if (now - next) >= 2:
            print("No")
            exit()
        else:  
            next = now-1
    elif now == next:
        next = now
    else:
        next = now
print("Yes")
