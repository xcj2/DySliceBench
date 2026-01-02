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

h,w = get_nums_l()

lines = sys.stdin.readlines()

xtable = [ [-1]*w for _ in range(h) ]
ytable = [ [-1]*w for _ in range(h) ]
yoko = [0] * (h*w)
tate = [0] * (h*w)

cur = 0
for y in range(h):
    for x in range(w):

        c = lines[y][x]

        if c == ".":
            yoko[cur] += 1
            xtable[y][x] = cur

            if x == (w-1):
                cur += 1
        else:
            cur += 1

cur = 0
for x in range(w):
    for y in range(h):

        c = lines[y][x]

        if c == ".":
            tate[cur] += 1
            ytable[y][x] = cur

            if y == (h-1):
                cur += 1
        else:
            cur += 1
        
ans = 0
for y in range(h):
    for x in range(w):
        if xtable[y][x] != -1:
            v = yoko[xtable[y][x]] + tate[ytable[y][x]] - 1
            
            if ans < v:
                ans = v

print(ans)