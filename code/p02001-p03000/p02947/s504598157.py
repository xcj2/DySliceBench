from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YNeos='YNeos'
mo=10**9+7
imp='IMPOSSIBLE'
alp=string.ascii_lowercase
num=enumerate(alp)
d=dict()
for i,j in num:
    d[j]=i

n=I()
w=[]
ans=0
di=defaultdict(int)
X=[]
for i in range(n):
    s=''.join(sorted(list(input())))
    di[s]+=1
for i,j in di.items():
    ans+=j*(j-1)//2
    
print(ans)