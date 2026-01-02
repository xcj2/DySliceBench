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

def prime_factorize(n):
    a = []
    for i in range(1,n+1):
        while i % 2 == 0:
            a.append(2)
            i //= 2
        f = 3
        while f * f <= i:
            if i % f == 0:
                a.append(f)
                i //= f
            else:
                f += 2
        if i != 1:
            a.append(i)
    return a

n=I()
#print(prime_factorize(6))
c=Counter(prime_factorize(n))
st=[74,24,14,4,2]
nums=[]
for y in st:
    count=0
    for x in c.keys():
        if c[x]>=y:
            count+=1
    nums.append(count)
#print(nums)
ans=nums[0]+nums[1]*max(0,(nums[4]-1))+nums[2]*max(0,(nums[3]-1))+nums[3]*max(0,(nums[3]-1))//2*max(0,(nums[4]-2))
print(ans)     