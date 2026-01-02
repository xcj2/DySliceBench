#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from bisect import bisect_left

s = str(input())
t = str(input())

d = defaultdict(list)
for i,ch in enumerate(s):
    d[ch].append(i)

i = 0
n = 1
for ch in t:
    temp = d[ch]
    if temp == []:
        print(-1)
        exit()
    place = bisect_left(temp,i)
    if place==len(temp):
        n += 1
        i = temp[0]+1
    else:
        i = temp[place]+1

print((n-1)*len(s)+i)
