#float型を許すな
#numpyはpythonで
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

d,g=MI()
lis=[LI() for i in range(d)]
pr=[]
for x in product([0,1],repeat=d):
    #print(x)
    score=0
    pro=0
    for i in range(d):
        if x[i]==1:
            score+=100*(i+1)*lis[i][0]+lis[i][1]
            pro+=lis[i][0]
    if score>=g:
        pr.append(pro)
    else:
        rest=g-score
        #print(rest)
        for i in range(d):
            j=d-i-1
            if x[j]==0:
                pro+=min(ceil(rest/(100*(j+1))),lis[j][0]-1)
                rest-=100*(j+1)*min(ceil(rest/(100*(j+1))),lis[j][0]-1)
            if rest<=0:
                pr.append(pro)
                break
        else:
            continue
        
print(min(pr))
#print(pr)