from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29
N  = int_raw()
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b,w = ints_raw()
    a = a-1
    b = b-1
    tree[a].append((b,w))
    tree[b].append((a,w))

def main():
    colors = [-1]*N
    colors[0]=1
    qu = deque()
    qu.append((0,0,-1))
    while len(qu)!=0:
        cur = qu.popleft()
        if cur[0]%2 == 0:
            colors[cur[1]]=0
        else:
            colors[cur[1]]=1
        for e in tree[cur[1]]:
            if e[0] ==cur[2]:
                continue
            qu.append([cur[0]+e[1],e[0],cur[1]])
    for c in colors:
        print (c)      
            
main()
