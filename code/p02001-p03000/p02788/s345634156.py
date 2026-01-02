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

n,d,a = get_nums_l()
lines = sys.stdin.readlines()
monsters = [ tuple(map(int, s.split(" "))) for s in lines ]
monsters.sort(key=lambda m: m[0])

ans = (monsters[0][1] + a - 1)//a
areas = [(monsters[0][0] + 2*d, ans*a)]
sum_ = ans*a
area_cursol = 0
for i in range(1, len(monsters)):
    m = monsters[i]
    x = m[0]
    h = m[1]


    while area_cursol < len(areas) and x > areas[area_cursol][0]:
        sum_ -= areas[area_cursol][1]
        area_cursol += 1

    if sum_ < h:
        # ボムつかう
        nokori = h-sum_
        kaisuu = (nokori+a-1)//a
        sum_ += kaisuu*a
        areas.append((x+2*d, kaisuu*a))
        ans += kaisuu

print(ans)