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

s=SI()
t=SI()
n=len(s)
u=len(t)
mx=-1
for i in range(n-u+1):
    count=0
    for j in range(u):
        #print(s[i+j])
        if s[i+j]==t[j] or s[i+j]=="?":
            count+=1
    if count==u:
        mx=i
#print(mx)
if mx<0:
    print("UNRESTORABLE")
else:
    for i in range(mx):
        if s[i]=="?":
            print("a",end="")
        else:
            print(s[i],end="")
    print(t,end="")
    for i in range(mx+u,n):
        if s[i]=="?":
            print("a",end="")
        else:
            print(s[i],end="")