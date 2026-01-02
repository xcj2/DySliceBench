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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b
#print(lcm(lcm(1000000,999999),999998))
#print(999998//2*999999)


#print(1000000*999999*999998%mod)
n=I()
lis=LI()
promod=1
LCM=1
for i in range(n):
    LCM=lcm(lis[i],LCM)
#print(LCM)

for i in range(n):
    promod=(promod*(lis[i]%mod))%mod
smmod=0
for i in range(n):
    smmod=(smmod+promod*pow(lis[i],mod-2,mod))%mod
#print(smmod)
x=(promod*pow(LCM%mod,mod-2,mod))%mod
ans=(smmod*pow(x,mod-2,mod))%mod
print(ans)
    
    
