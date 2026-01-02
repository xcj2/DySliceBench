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

s = input()
n = len(s)
ans = [0] * n

base = 0
while True:
    firstL = s.find("L", base)
    ans[firstL] += (firstL-base)//2 + 1
    ans[firstL-1] += (firstL-base-1)//2 + 1

    nextR = s.find("R", firstL+1)
    end = False
    if nextR == -1:
        nextR = n
        end = True
    ans[firstL] += (nextR - firstL - 1) // 2
    ans[firstL-1] += (nextR - firstL) // 2

    if end:
        break

    base = nextR

print(" ".join(map(str,ans)))
