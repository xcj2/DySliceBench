import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n=I()
As=list(map(int,input().rstrip().split(" ")))
#A=list(reversed(As))
#print(As)
ans=[0 for i in range(n)]
for i in range(n//2,n):
    ans[i]=As[i]
#print(ans)
for j in range(n//2):
    k=n//2-j-1
    ball=0
    for l in range(2,n//(k+1)+1):
        ball+=ans[(k+1)*l-1]
        if ball%2==As[k]:
            ans[k]=0
        else:
            ans[k]=1
print(sum(ans))
for i in range(n):
    if ans[i]==1:
        print(i+1,end=" ")