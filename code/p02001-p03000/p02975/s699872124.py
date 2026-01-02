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

#A
def A():
    n = I()
    a = LI()
    if sum(a) == 0:
        print("Yes")
        return
    if n%3 != 0:
        print("No")
        return
    d = defaultdict(lambda : 0)
    for i in a:
        d[i] += 1
    if len(list(d.items())) == 2:
        if d[0] == n//3:
            print("Yes")
            return
        else:
            print("No")
            return
    k = 0
    for i,j in d.items():
        k ^= i
        if j != n//3:
            print("No")
            return
    if not k:
        print("Yes")
        return
    print("No")
    return

#B
def B():
    n,m = LI()
    ans = []
    d = [0]*(n+1)
    for i in range(m):
        a,b = LI()
        ans.append([a,b])
        d[a] ^= 1
    for i in range(m):
        a,b = ans[i]
        if d[a]:
            ans[i] = [b,a]
            d[a] ^= 1
            d[b] ^= 1
    if sum(d):
        print(-1)
    else:
        for i in ans:
            print(*i)
    return

#C
def C():
    n = I()
    p = [(1<<i) for i in range(100)]
    if n in p:
        print("No")
        quit()
    if n+1 in p:
        print("Yes")
        for i in range(1,2*n):
            print(i,i+1)
        quit()
    ans = []
    for i in range(1,3):
        ans.append((i,i+1))
    ans.append((3,n+1))
    for i in range(1,3):
        ans.append((i+n,i+n+1))
    u = 1
    d = 1
    for i in range(2,n//2+n%2):
        ans.append((u,2*i))
        ans.append((d,2*i+1))
        ans.append((2*i,2*i+n+1))
        ans.append((2*i+1,2*i+n))
        u = 2*i+n+1
        d = 2*i+n

    if n%2:
        print("Yes")
        for i,j in ans:
            print(i,j)
    else:
        ans.append((n-1,n))
        for i in range(n):
            if p[i]&n:
                break
        ans.append((p[i+1]-2,2*n))
        print("Yes")
        for i,j in ans:
            print(i,j)
    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    A()
