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
nums = get_nums_l()

check = [False] * n
ans = 0

def need():
    for n in nums:
        if n > 0:
            return True
    return False

while need():
    left = -1
    right = -1
    for i,x in enumerate(nums):
        if x != 0:
            left = i
            break
    
    min_ = nums[left]
    prev = left
    for i in range(left+1, n):
        if nums[i] > 0:
            min_ = min(min_, nums[i])
            prev = i
        else:
            break
    right = prev

    for i in range(left, right+1):
        nums[i] -= min_
    ans += min_

    
print(ans)