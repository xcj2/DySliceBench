import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import bisect
from itertools import accumulate


n,m,k = readints()

a = readints()
b = readints()

c = [0] + list(accumulate(a))
d = [0] + list(accumulate(b))

ans = 0
for i in range(n+1):
    if c[i]>k:
        continue
    else:
        ans = max(ans,i+bisect.bisect_right(d,k-c[i])-1)

print(ans)






