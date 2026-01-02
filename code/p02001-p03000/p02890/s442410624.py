import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))

from collections import Counter
from itertools import accumulate
import bisect

n = readint()
a = readints()
b = sorted(Counter(a).values())
exist = len(b)
b = [0]*(n-exist)+b
c = list(accumulate([0]+b))

ans = [n]
for k in range(2,exist+1):
    l = 0
    r = n//k+1
    while r-l>1:
        x = (r+l)//2
        i = bisect.bisect_left(b,x)
        if c[i]+(n-i)*x>=x*k:
            l = x
        else:
            r = x
    ans.append(l)

printrows(ans+[0]*(n-exist))