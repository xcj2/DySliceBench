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

n,m = get_nums_l()

# 与えられたカード小さい順
nums = sorted(get_nums_l())

# 変更操作大きい順
changes = []

for j in range(m):
    b,c = get_nums_l()
    changes.append((b,c))
changes.sort(key=lambda c:c[1], reverse=True)

# 新カード大きい順
nnn = []
for change in changes:
    b,c = change
    nnn.extend([c] * b)

    if len(nnn) >= n:
        break

summ=0
len_nnn = len(nnn)
for i in range(n):
    if i < len_nnn:
        summ += max(nums[i], nnn[i])
    else:
        summ += nums[i]

print(summ)