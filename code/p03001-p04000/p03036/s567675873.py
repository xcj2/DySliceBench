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

r,d,x_2000 = get_nums_l()

now = x_2000
for i in range(10):
    new_a = now * r - d
    print(new_a)
    now = new_a