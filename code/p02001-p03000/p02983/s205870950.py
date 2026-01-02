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

l,r = get_nums_l()
d = r-l

lm = l % 2019
rm = r % 2019


nums = [0] * 2019
for imod in range(2019):
    if (imod+(2019-lm))%2019 <= d:
        nums[imod] += 1 + (d - (imod+(2019-lm))%2019)//2019

min_ = 999999999999999999999
for a in range(2019):
    for b in range(2019):
        if a==b and nums[a] < 2:
            continue
        if nums[a] < 1 or nums[b] < 1:
            continue
        mo = a*b%2019
        if min_ > mo:
            min_ = mo
print(min_)

# m3   = 3 - l % 3
# m673 = 673 - l % 673

# if (m3==3 or m3 <= d) and (m673==673 or m673 <= d):
#     print(0)
# else:
#     print((l*(l+1)) % 2019)