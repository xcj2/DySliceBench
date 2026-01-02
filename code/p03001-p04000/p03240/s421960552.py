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

n=I()
lis=[]
for i in range(n):
    lis.append(LI())
lis.sort(key=lambda x:x[2],reverse=True)
x1,y1,h1,x2,y2,h2=lis[0][0],lis[0][1],lis[0][2],lis[1][0],lis[1][1],lis[1][2]
cand=[]
    
for i in range(101):
    for j in range(101):
        H=h1+abs(i-x1)+abs(j-y1)
        cand.append([i,j,H])
#print(cand)

candx=[]
for j in range(len(cand)):
    H=cand[j][2]
    count=0
    #print(H)
    for i in range(1,n):
        if max(H-abs(cand[j][0]-lis[i][0])-abs(cand[j][1]-lis[i][1]),0)==lis[i][2]:
            count+=1
    #print(count)
    if count==n-1:
        candx.append([cand[j][0],cand[j][1],H])
print(*candx[0])
'''for li in candx:
    flag=True
    for i in range(n):
        if lis[i][2]<0:
            if -abs(li[0]-lis[i][0])-abs(li[1]-lis[i][1])+li[2]>=0:
                flag=False
    if flag==True:
        print(*li)
        sys.exit()'''