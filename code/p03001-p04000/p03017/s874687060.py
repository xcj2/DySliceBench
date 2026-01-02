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
    b = LI()
    ans = []
    for j in range(n):
        for i in range(len(b))[::-1]:
            if b[i] == i+1:
                x = b.pop(i)
                ans.append(x)
                break
    if b:
        print(-1)
    else:
        print(*ans[::-1],sep = "\n")
    return

#B
def B():
    n,a,b,c,d = LI()
    s = S()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    k = b
    while b < d:
        if s[b+1] == ".":
            b += 1
        else:
            if s[b+2] == "#":
                print("No")
                return
            b += 2
    b = k
    if c < d:
        while a < c:
            if s[a+1] == ".":
                a += 1
            else:
                if s[a+2] == "#":
                    print("No")
                    return
                a += 2
        print("Yes")
    else:
        for i in range(b-1,d):
            if s[i:i+3].count(".") == 3:
                print("Yes")
                return
        print("No")
    return

#C
def C():
    n = I()

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
    B()
