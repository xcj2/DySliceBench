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

MOD = 1000000007

n,m = get_nums_l()
breaks = map(int, sys.stdin.readlines()) if m>0 else []

dp = [0] * (n+1)

for a in breaks:
    dp[a] = -1

dp[n] = 1

for i in range(n-1, -1, -1):
    if dp[i] == -1:
        continue
    
    x = 0
    if dp[i+1] != -1:
        x += dp[i+1]
    
    if i <= (n-2) and dp[i+2] != -1:
        x += dp[i+2]
    
    dp[i] = x % MOD

print(dp[0])