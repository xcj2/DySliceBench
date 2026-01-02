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

s = input()

a,b = "",""

a = s[0]

if a != s[1]:
    b = s[1]

    if a in s[2:] and b in s[2:]:
        print("Yes")
    else:
        print("No")
else:
    if a != s[2] and s[2] == s[3]:
        print("Yes")
    else:
        print("No")