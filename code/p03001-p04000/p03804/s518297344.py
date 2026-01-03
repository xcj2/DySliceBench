import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,sqrt
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

n,m=MI()
picla=[]
picsm=[]
for i in range(n):
    picla.append(input().rstrip())
for i in range(m):
    picsm.append(input().rstrip())
for i in range(n-m+1):
    for j in range(n-m+1):
        count=0
        for k in range(m):
            '''print(picla[i+k][j:j+m],end=" ")
            print(picsm[k])'''
            if picla[i+k][j:j+m]==picsm[k]:
                count+=1
        if count==m:
            print("Yes")
            sys.exit()
print("No")
