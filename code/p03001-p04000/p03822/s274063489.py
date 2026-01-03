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

n = readint()
parent = [-1] + [readint()-1 for i in range(n-1)]
child = [0]*n
leaf = [1]*n
for x in parent[1:]:
    leaf[x] = 0
    child[x] += 1

score = [0]*n
leaf = [(score[i],i) for i in range(n) if leaf[i]==1]
heapq.heapify(leaf)

while leaf:
    s,c = heapq.heappop(leaf)
    p = parent[c]
    score[p] = max(score[p],s)+1
    child[p]-=1
    if child[p]==0:
        if p!=0:
            heapq.heappush(leaf,(score[p],p))

print(score[0])

