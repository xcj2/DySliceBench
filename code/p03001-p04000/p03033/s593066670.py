import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import heapq

n,q = readints()

a = []
for i in range(n):
    s,t,x = readints()
    a.append((s-x,0,x))
    a.append((t-x,1,x))
for i in range(q):
    d = readint()
    a.append((d,2,0))
a.sort()

ans = []

stop = []
deleted = []

for t,j,x in a:
    if j==0:
        heapq.heappush(stop,x)
    elif j==1:
        heapq.heappush(deleted,x)
    else:
        while deleted and stop[0] == deleted[0]:
            heapq.heappop(stop)
            heapq.heappop(deleted)
        if stop:
            ans.append(stop[0])
        else:
            ans.append(-1)

printrows(ans)
