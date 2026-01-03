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

n,k=MI()
lis=LI()
n=str(n)
cand=[]
flag=True
for i in range(10):
    if not i in lis:
        cand.append(i)
mx=""
for i in range(len(n)):
    mx+=str(cand[-1])
if int(n)>int(mx):
    flag=False
stri=""
if flag==False:
    if 0 in cand:
        v=str(cand[1])
        stri+=v
        for i in range(len(n)):
            stri+="0"
        
    else:
        v=str(cand[0])
        for i in range(len(n)+1):
            stri+=v
    print(stri)
else:
    for i in range(int(n),10000):
        y=str(i)
        cou=0
        for j in range(len(y)):
            if int(y[j]) in cand:
                cou+=1
        #print(cou)
        if cou==len(y):
            print(y)
            sys.exit()

    