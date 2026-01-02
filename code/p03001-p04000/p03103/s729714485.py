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

n,m = get_nums_l()
lines = sys.stdin.readlines()

shops = [None] * n
for i,line in enumerate(lines):
    shops[i] = tuple(map(int, line.split(" ")))

shops.sort(key=lambda s:s[0])

ans = 0
i = 0
count = 0
while count < m:
    nokori = max(0, m - count)
    kau = min(nokori, shops[i][1])
    count += kau
    ans += kau * shops[i][0]
    i += 1

print(ans)