#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n, k = LI()
    s = S()
    s[k-1] = s[k-1].lower()
    print("".join(s))

    return

#B
def B():
    s = S()
    a = int("".join(s[:2]))
    b = int("".join(s[2:]))
    if 0 < a <= 12:
        if 0 < b <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    elif a == 0:
        if 0 < b <= 12:
            print("YYMM")
        else:
            print("NA")
    else:
        if 0 < b <= 12:
            print("YYMM")
        else:
            print("NA")
    return

#C
def C():
    n, k = LI()
    ans = 0
    if k == 1:
        print(1)
        return
    nibuiti = [None for i in range(int(math.log2(k) + 1))]
    for num in range(int(math.log2(k) + 1)):
        if num == 0:
            nibuiti[num] = 1 / 2
            continue
        nibuiti[num] = nibuiti[num-1]/2
        
    for i in range(1, n + 1):
        if i >= k:
            ans += 1
            continue
        b = nibuiti[int(math.log2((k - 1) // i))]
        ans += b
    print(ans/n)
    return

#D
def D():
    n = II()
    color = [0 for i in range(n)]
    edge = [[] for i in range(n)]
    for i in range(n - 1):
        v, u, w = LI_()
        edge[v].append((u,w+1))
        edge[u].append((v,w+1))
    check = [True for i in range(n)]
    for i in range(n):
        q = deque()
        q.append(i)
        
        while q:
            a = q.pop()
            if check:
                check[a] = False
                for k,w in edge[a]:
                    if check[k]:
                        q.append(k)
                        if w % 2:
                            color[k] = color[a] ^ 1
                        else:
                            color[k] = color[a]
    for c in color:
        print(c)
    return

#E
def E():
    n, m = LI()
    xyz = LIR_(m)
    par = [i for i in range(n)]
    size = [1] * n
    def root(a):
        if par[a] == a:
            return a
        par[a] = root(par[a])
        return par[a]

    def union(a, b):
        a = root(a)
        b = root(b)
        if size[a] < size[b]: b, a = a, b
        if a == b:
            return
        par[b] = a
        size[b] += size[a]

    for x, y, _ in xyz:
        union(x, y)
    
    for i in range(n):
        root(i)
    print(len(set(par)))



    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
