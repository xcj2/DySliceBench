#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n,k = LI()
    s = input()
    for i in range(k-1):
        print(s[i],end = "")
    print(s[k-1].lower(),end = "")
    for i in range(k,n):
        print(s[i],end = "")
    print()
    return

#B
def B():
    s = S()
    k = int(s[0])*10+int(s[1])
    l = int(s[2])*10+int(s[3])
    if k == 0:
        if l == 0:
            print("NA")
        elif l < 13:
            print("YYMM")
        else:
            print("NA")
    elif k < 13:
        if l == 0:
            print("MMYY")
        elif l < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if l == 0:
            print("NA")
        elif l < 13:
            print("YYMM")
        else:
            print("NA")

#C
def C():
    n,k = LI()
    ans = 0
    for i in range(1,n+1):
        l = k/i
        ans += 1/n*1/(2 << max(0,math.ceil(math.log(l,2))))
    print(ans*2)
    return

#D
def D():
    n = I()
    v = [[] for i in range(n)]
    for i in range(n-1):
        x,y,w = LI()
        x -= 1
        y -= 1
        v[x].append((y,w))
        v[y].append((x,w))
    ans = [0 for i in range(n)]
    bfs_map = [1 for i in range(n)]
    bfs_map[0] = 0
    q = deque()
    q.append(0)
    while q:
        x = q.popleft()
        for y,w in v[x]:
            if bfs_map[y]:
                if w%2:
                    ans[y] = ans[x]^1
                else:
                    ans[y] = ans[x]
                bfs_map[y] = 0
                q.append(y)
    for i in ans:
        print(i)
    return

#E
def E():
    def root(x):
        if par[x] == x:
            return par[x]
        par[x] = root(par[x])
        return par[x]
    def same(x,y):
        return root(x) == root(y)
    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    n,m = LI()
    par = [i for i in range(n)]
    rank = [0 for i in range(n)]
    for i in range(m):
        x,y,z = LI()
        x -= 1
        y -= 1
        if not same(x,y):
            unite(x,y)
    for i in range(n):
        root(i)
    par = list(set(par))
    print(len(par))
    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    E()
