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

n,a,b,c = get_nums_l()
lengths = list(map(int,sys.stdin.readlines()))

ans = 999999999999999

for x in range(4 ** n):
    lll = [0] * 4
    gattai=0
    for i in range(n):
        tmp = x >> (i*2)
        tmp %= 4
        
        if tmp != 0 and lll[tmp] > 0:
            gattai += 1
        lll[tmp] += lengths[i]

    if min(lll[1:]) == 0:
        continue

    mp = gattai*10 + abs(a-lll[1]) + abs(b-lll[2]) + abs(c-lll[3])
    ans = min(ans, mp)

print(ans)