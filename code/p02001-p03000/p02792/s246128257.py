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

keta = int(math.log10(n)) + 1

memo = [ [None] * 10 for _ in range(10)]

ans = 0
for a in range(1, n+1):
    x = int(str(a)[0])
    y = a % 10

    if x == 0 or y == 0:
        continue

    if memo[x][y] is not None:
        ans += memo[x][y]
        # print(a, ans)
        continue
    
    patterns = 0
    for b in range(x, n+1, 10):
        x2 = int(str(b)[0])
        y2 = b % 10
        if x == y2 and y == x2:
            patterns += 1
    memo[x][y] = patterns
    ans += patterns
    # print(a, ans)

    # patterns = 0
    # # 1桁
    # if x == y and n <= x:
    #     patterns += 1
    
    # for k in range(keta-1):

print(ans)