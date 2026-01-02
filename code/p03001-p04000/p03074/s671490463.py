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
    a,b = LI()
    if a == b:
        print(2*a)
    else:
        print(2*max(a,b)-1)
    return

#B
def B():
    n = I()
    h = LI()
    m = h[0]
    ans = 1
    for i in range(1,n):
        if m <= h[i]:
            ans += 1
            m = h[i]
    print(ans)
    return

#C
def C():
    s = S()
    ans = 0
    n = len(s)
    t = ["1" if i%2 else "0" for i in range(n)]
    for i in range(n):
        if t[i] != s[i]:
            ans += 1
    ans2 = 0
    t = ["0" if i%2 else "1" for i in range(n)]
    for i in range(n):
        if t[i] != s[i]:
            ans2 += 1
    print(min(ans,ans2))
    return

#D
def D():
    n,k = LI()
    s = S()
    f = [0 for i in range(n)]
    if s[0] == "0":
        f[0] = 1
    for i in range(1,n):
        if s[i] ==  "0" and s[i-1] == "1":
            f[i] = 1
    for i in range(n-1):
        f[i+1] += f[i]
    ans = 0
    for l in range(n):
        r = bisect.bisect_right(f,k+f[l]*int(s[l]))
        ans = max(ans, r-l)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    D()
