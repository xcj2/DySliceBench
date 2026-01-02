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
    s = input()
    ans = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "W":
            ans += i-w
            w += 1
    print(ans)
    return

#B
def B():
    n = I()
    a = LI()
    f = defaultdict(lambda : 0)
    a.sort(key = lambda x:-x)
    ans = 0
    m = 32
    k = [1<<i for i in range(m)]
    for i in a:
        for j in k:
            i_ = j-i
            if i_ <= 0:continue
            if f[i_]:
                f[i_] -= 1
                ans += 1
                break
        else:
            f[i] += 1
    print(ans)
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#Solve
if __name__ == "__main__":
    B()
