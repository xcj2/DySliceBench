import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n=I()
s=input().rstrip()
alphasm=[chr(i) for i in range(97, 97+26)]
num=[]
for i in range(n):
    count=0
    k=list(s[0:i])
    l=list(s[i:n])
    for char in alphasm:
        if (char in k) and (char in l):
            count+=1
    num.append(count)
print(max(num))