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

h,n = get_nums_l()
lines = sys.stdin.readlines()
magics = [ tuple(map(int, l.split(" "))) for l in lines ]

# 残りHPがiの時に倒すのに必要な最小魔力
dp = [99999999999999] * (h + 10)

dp[0] = 0
for i in range(len(dp)):
    for m in magics:
        next_ = min(i + m[0], h)
        tmp = dp[i] + m[1]
        if dp[next_] > tmp:
            dp[next_] = tmp

print(dp[h])