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
lis=LI()
odd=[];eve=[]
for i in range(n):
    if i%2==1:
        eve.append(lis[i])
    else:
        odd.append(lis[i])
if n%2==0:
    eve=list(reversed(eve))
    for s in eve:
        print(s,end=" ")
    for t in odd:
        print(t,end=" ")
else:
    odd=list(reversed(odd))
    for s in odd:
        print(s,end=" ")
    for t in eve:
        print(t,end=" ")
    
        

        
        
    

    
    