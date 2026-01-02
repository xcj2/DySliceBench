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
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n=I()
u=[]
alphasm=[chr(i) for i in range(97, 97+26)]
s=input().rstrip()
for i in range(n):
    s1=list(s[0:i])
    s2=list(s[i:n])
    count=0
    for x in alphasm:
        if (x in s1) and (x in s2):
            count+=1
    u.append(count)
print(max(u))