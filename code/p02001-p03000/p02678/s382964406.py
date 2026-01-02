import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import queue


n,m = readints()
path  =[[] for i in range(n)]

for i in range(m):
    a,b = readints()
    a-=1
    b-=1
    path[a].append(b)
    path[b].append(a)
d = [[] for i in range(n)]
d[0].append(0)

q = queue.Queue()
q.put(0)
visited = [-1]*n
visited[0]=0

ans = [0]*n

while not q.empty():
    p = q.get()
    for x in path[p]:
        if visited[x]==-1:
            visited[x]=visited[p]+1
            d[visited[x]].append(x)
            q.put(x)
            ans[x]=p+1

print('Yes')
printrows(ans[1:])


