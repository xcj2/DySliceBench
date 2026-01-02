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

n,k=MI()
s=SI()
ze=[]
on=[]

if s[0]=="0":
    state="ze"
    sq=1
    on.append(0)
else:
    state="on"
    sq=1
    
for i in range(1,n):
    u=s[i]
    if state=="ze":
        if u=="0":
            sq+=1
        else:
            ze.append(sq)
            sq=1
            state="on"
            
        
    elif state=="on":
        if u=="1":
            sq+=1
        else:
            on.append(sq)
            sq=1
            state="ze"
if state=="on":
    on.append(sq)
elif state=="ze":
    ze.append(sq)
if len(ze)<k:
    print(n)
    sys.exit()
if s[-1]=="0":
    on.append(0)
#print(on)
#print(ze)
u=len(on)

smz=[0 for i in range(u-k)]
smo=[0 for i in range(u-k)]
for i in range(k):
    smz[0]+=ze[i]
for i in range(k+1):
    smo[0]+=on[i]
#print(smo)
#print(smz)
for i in range(u-k-1):
    smz[i+1]=smz[i]-ze[i]+ze[i+k]
for i in range(u-k-1):
    smo[i+1]=smo[i]-on[i]+on[i+k+1]
#print(smo)
#print(smz)
mx=0
for i in range(u-k):
    val=smo[i]+smz[i]
    if val>mx:
        mx=val
print(mx)