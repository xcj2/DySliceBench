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
    s = IR(5)
    k = I()
    if max(s)-min(s) > k:
        print(":(")
    else:
        print("Yay!")
    return

#B
def B():
    s = IR(5)
    s.sort(key = lambda x:-x%10)
    ans = 0
    i = 0
    k = 0
    while 1:
        if i%10 == 0:
            ans = i+s[k]
            i += s[k]-1
            k += 1
            if k == 5:break
        i += 1
    print(ans)
    return

#C
def C():
    n = I()
    a = IR(5)
    ans = 5+n//min(a)
    if n%min(a) == 0:ans -= 1
    print(ans)
    return

#D
def D():
    x,y,z,k = LI()
    a = LI()
    b = LI()
    c = LI()

    return

#Solve
if __name__ == "__main__":
    C()
