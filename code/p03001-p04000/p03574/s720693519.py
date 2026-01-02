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

h,w=MI()
mines=[[0 for i in range(w+2)]for i in range(h+2)]

for i in range(w+2):
    mines[0][i]="."
    mines[h+1][i]="."
for i in range(h+2):
    mines[i][0]="."
    mines[i][w+1]="."
for i in range(h):
    s=list(input().rstrip())
    for j in range(w):
        mines[i+1][j+1]=s[j]
#print(mines)
minum=[[0 for i in range(w+2)]for i in range(h+2)]
for i in range(1,h+1):
    for j in range(1,w+1):
        if mines[i][j]=="#":
            minum[i-1][j]+=1
            minum[i+1][j]+=1
            minum[i][j+1]+=1
            minum[i][j-1]+=1
            minum[i+1][j+1]+=1
            minum[i+1][j-1]+=1
            minum[i-1][j+1]+=1
            minum[i-1][j-1]+=1
#print(minum)
for i in range(1,h+1):
    for j in range(1,w+1):
        if mines[i][j]=="#":
            print("#",end="")
        else:
            print(minum[i][j],end="")
    print()