# coding: utf-8
# hello worldと表示する
#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

s=SI()
a=int(s[0])
b=int(s[1])
c=int(s[2])
d=int(s[3])
def porm(x):
    if x==1:
        return "+"
    else:
        return "-"
def vec(x):
    if x==1:
        return 1
    else:
        return -1
for i in range(8):
    j=(i>>0) %2
    k=(i>>1) %2
    l=(i>>2) %2
    if a+b*vec(j)+c*vec(k)+d*vec(l)==7:
        print(a,end="")
        print(porm(j),end="")
        print(b,end="")
        print(porm(k),end="")
        print(c,end="")
        print(porm(l),end="")
        print(d,end="")
        print("=7")
        sys.exit()