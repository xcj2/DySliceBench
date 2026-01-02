
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import math
n = readint()
c = readstr()

r = c.count('R')
w = c.count('W')
ans = 0
for i in range(r):
    if c[i]=='W':
        ans += 1
for i in range(r+1,n):
    if c[i]=='R':
        ans += 1
print(math.ceil(ans/2))
