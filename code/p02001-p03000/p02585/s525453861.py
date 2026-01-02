from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, k = MAP()
p = LIST()
c = LIST()

for i in range(n):
    p[i] -= 1

ans = -inf
for i in range(n):
    visit = [inf]*n
    reg_score = [-inf]*n

    now = i
    count = 0
    score = 0
    while visit[now] == inf:
        visit[now] = count
        reg_score[now] = score
        count += 1
        now = p[now]
        score += c[now]

    x = visit[now]
    y = count - visit[now]
    X = reg_score[now]
    Y = score - reg_score[now]

    for j in range(n):
        if visit[j] == inf:
            continue
        if j != i and k >= visit[j]:
            tmp0 = reg_score[j]
            if ( k - x ) % y >= visit[j]:
                tmp1 = (k - x)//y * Y + reg_score[j]
            else:
                tmp1 = ((k - x)//y - 1) * Y + reg_score[j]
            ans = max(ans, tmp0, tmp1)
        elif (k-x)//y>0:
            tmp0 = Y + reg_score[j]
            if ( k - x ) % y >= visit[j]:
                tmp1 = (k - x)//y * Y + reg_score[j]
            else:
                tmp1 = ((k - x)//y - 1) * Y + reg_score[j]
            ans = max(ans, tmp0, tmp1)

print(ans)