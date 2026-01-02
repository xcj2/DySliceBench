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

n = int(input())
reviews = []
for i in range(n):
    s,p = input().split(" ")
    p = int(p)
    reviews.append((i,s,p))

reviews.sort(key=lambda a:a[2], reverse=True)
reviews.sort(key=lambda a:a[1])

for r in reviews:
    print(r[0]+1)