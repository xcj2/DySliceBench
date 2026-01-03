import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N,M = mint()
student = [0]*N
point = [0]*M
for i in range(N):
    x,y = mint()
    student[i] = (x,y)
for j in range(M):
    x,y = mint()
    point[j] = (x,y)
    
ans = [0]*N
for i in range(N):
    x1,y1 = student[i]
    tmp = INF
    k = 0
    for j in range(M):
        x2,y2 = point[j]
        if abs(x1-x2)+abs(y1-y2)<tmp:
            tmp = abs(x1-x2)+abs(y1-y2)
            k = j+1
    ans[i] = str(k)

lprint(ans)