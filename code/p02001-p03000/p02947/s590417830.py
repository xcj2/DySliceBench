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
sss = [ input() for _ in range(n) ]
sss = sorted(map("".join, map(sorted, sss)))

ans = 0
left = 0
while left<n-1:
    for right in range(left+1, n):
        if sss[left] != sss[right]:
            dis = right - left -1
            ans += dis * (dis+1) // 2
            left = right
            break
    if right == n-1:
        break


dis = right - left
ans += dis * (dis+1) // 2


print(ans)