from heapq import heappush, heappop
from collections import deque
import itertools
from itertools import permutations
import sys
import bisect
sys.setrecursionlimit(10**6)
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YNeos='YNeos'
GYN=['Yes','trumpet']
mo=10**9+7
imp='IMPOSSIBLE'

n=I()
a=LI()[::-1]

for i in range(n-1):
    if a[i]<a[i+1]:
        a[i+1]-=1
    if a[i]<a[i+1]:
        print('No')
        exit()
print('Yes')

    
        
