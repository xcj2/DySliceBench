#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
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

alphasm=[chr(i) for i in range(97, 97+26)]
n=I()
lis=[list(SI()) for i in range(n)]
counter=[inf for i in range(26)]
for x in range(26):
    for i in range(n):
        counter[x]=min(counter[x],lis[i].count(alphasm[x]))
        #print(lis[i].count(al))
#print(counter)
for i in range(26):
    for j in range(counter[i]):
        print(alphasm[i],end="")
        