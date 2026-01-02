import math
from functools import reduce

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

s = input()

left = int(s[0:2])
right = int(s[2:4])

if left <= 12 and left != 0:
    if right <= 12 and right != 0:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if right <= 12 and right != 0:
        print("YYMM")
    else:
        print("NA")