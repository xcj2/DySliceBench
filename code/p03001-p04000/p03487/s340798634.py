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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
def A():
    a,b = LI()
    print(math.ceil((a+b)/2))

#B
def B():
    s = S()
    t = S()
    s.sort()
    t.sort()
    t = t[::-1]
    l = [s,t]
    l.sort()
    if s == t:
        print("No")
    elif l[0] == s:
        print("Yes")
    else:
        print("No")
#C
def C():
    n = I()
    d = defaultdict(int)
    a = LI()
    for i in a:
        d[i] += 1
    ans = 0
    for i in d.keys():
        if i <= d[i]:
            ans += d[i]-i
        else:
            ans += d[i]
    print(ans)
#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    C()
