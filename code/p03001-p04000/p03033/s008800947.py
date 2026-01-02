import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


def compress(a):
    b = sorted(set(a))
    d = {x:i+1 for i,x in enumerate(b)}
    return b,d


import heapq

n,q = readints()

X = []

block = []
free = []
for i in range(n):
    s,t,x = readints()
    X.append(x)
    block.append([s-x,x])
    free.append([t-x,x])

b,d = compress(X)
block = [(x[0],d[x[1]]) for x in block]
free = [(x[0],d[x[1]]) for x in free]
heapq.heapify(block)
heapq.heapify(free)

ans = []

stop = []
heapq.heapify(stop)
deleted = []
heapq.heapify(deleted)

for i in range(q):
    D = readint()
    while block:
        if block[0][0]<=D:
            a = heapq.heappop(block)
            heapq.heappush(stop,a[1])
        else:
            break
    while free:
        if free[0][0]<=D:
            a = heapq.heappop(free)
            heapq.heappush(deleted,a[1])
        else:
            break
    while deleted:
        if stop[0] == deleted[0]:
            heapq.heappop(stop)
            heapq.heappop(deleted)
        else:
            break
    if stop:
        ans.append(stop[0])
    else:
        ans.append(-1)

ans = [b[x-1] if x >=0 else -1 for x in ans]
printrows(ans)
