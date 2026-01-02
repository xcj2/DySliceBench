def examD():
    N = I()
    AB = [LI() for _ in range(N-1)]
    V = [[] for _ in range(N)]
    for a,b in AB:
        V[a-1].append(b-1)
        V[b-1].append(a-1)
    ans = []
    root = 0
    #親とdfsの順序記録
    parent = [0] * (N)
    order = []
    stack = [root]
    while stack:
        x = stack.pop()
        order.append(x)
        for y in V[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            stack.append(y)
#    print(parent); print(order)
    #辺の色...子の色
    color = [-1]*(N)

    for i in order:
        NG = color[i]
        cur = 1
        for j in V[i]:
            if j == parent[i]:
                continue
            if cur==NG:
                cur +=1
            color[j] = cur
            cur +=1
#    print(color)
    append = ans.append
    for a,b in AB:
        if parent[a-1]==b-1:
            #子の色を塗る
            append(color[a-1])
        else:
            append(color[b-1])
    print(max(ans))
    for v in ans:
        print(v)

def examE():
    N, K = LI()

    return

def examF():
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()