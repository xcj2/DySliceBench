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
aaa = get_nums_l()

sum_ = sum(aaa)

x = 0
for i in range(1, n, 2):
    x += aaa[i] * 2

ans = [0] * n
ans[0] = sum_ - x

for i in range(1,n):
    ans[i] = (aaa[i-1] - ans[i-1]//2) * 2

print(*ans)