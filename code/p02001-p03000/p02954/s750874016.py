import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
#inf = 10**17
#mod = 10**9 + 7

S=input().rstrip()
i=0
n=len(S)
count=0
pa=[]
pb=[]
for i in range(n-1):
    if S[i]=="R" and S[i+1]=="L":
        count+=1
        pa.append(i)
    elif S[i]=="L" and S[i+1]=="R":
        pb.append(i+1)
Rs=[]
Ls=[]
Rs.append(pa[0]+1)
for i in range(count-1):
    Rs.append(pa[i+1]-pb[i]+1)
    Ls.append(pb[i]-pa[i]-1)
Ls.append(n-1-pa[-1])
ans=[0]*n
for i in range(count):
    ans[pa[i]]=floor(Ls[i]/2)+ceil(Rs[i]/2)
    ans[pa[i]+1]=floor(Rs[i]/2)+ceil(Ls[i]/2)
for an in ans:
    print(an,end=" ")
#answer=" ".join(map(str,ans))