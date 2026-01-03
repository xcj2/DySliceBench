import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,l=mp()
a=lmp()
c=True
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        c=False
        ind=i
        break
if c:
    print("Impossible")
    exit()
print("Possible")
for i in range(1,ind+1):
    print(i)
for i in range(n-1,ind+1,-1):
    print(i)
print(ind+1)