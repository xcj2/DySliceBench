#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve(t,n):
    if t == n:
        print(t,n)
        return
    a = list(map(int,list(str(n))))
    s = sum(a)
    m = len(a)
    if s > t:
        print("error")
        return
    nm = m-1
    f = [0]*nm
    d = defaultdict(lambda : 0)
    d[tuple(f)] = 1
    l = [[] for i in range(t+1)]
    q = [(s,f)]
    l[s].append(f)
    ans = s
    while q:
        s,f = heappop(q)
        for i in range(nm):
            if f[i]:
                continue
            nf = [1 if j == i else f[j] for j in range(nm)]
            ns = 0
            ms = a[0]
            for j in range(1,m):
                if nf[j-1]:
                    ms *= 10
                    ms += a[j]
                else:
                    ns += ms
                    ms = a[j]
            ns += ms
            if ns <= t:
                tf = tuple(nf)
                if not d[tf]:
                    d[tf] = 1
                    if ns >= ans:
                        ans = ns
                        l[ns].append(nf)
                    heappush(q,(ns,nf))
    if len(l[ans]) > 1:
        print("rejected")
        return
    s = [ans]
    f = l[ans][0]
    k = a[0]
    for i in range(nm):
        if f[i]:
            k *= 10
            k += a[i+1]
        else:
            s.append(k)
            k = a[i+1]
    s.append(k)
    print(*s)
    return

#Solve
if __name__ == "__main__":
    while 1:
        t,n = LI()
        if t == n == 0:
            break
        solve(t,n)

