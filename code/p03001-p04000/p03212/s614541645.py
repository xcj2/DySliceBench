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

c = ["!", "3", "5", "7"]
def shichigosan_numbers():
    x = 0
    while True:
        x += 1
        s = ""
        y = x
        while y > 0:
            s = c[y%4] + s
            y = y // 4
        if "!" not in s and "3" in s and "5" in s and "7" in s: 
            yield int(s)

ans = 0
for x in shichigosan_numbers():
    if x <= n:
        ans += 1
    else: 
        print(ans)
        exit()