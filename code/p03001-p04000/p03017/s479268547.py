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
    n,a,b,c,d = LI()
    s = input()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if c == d:
        print("No")
    else:
        if c < d:
            k = s[b:d+1]
            for i in range(d-b):
                if k[i] == k[i+1] == "#":
                    print("No")
                    quit()
            k = s[a:c+1]
            for i in range(c-a):
                if k[i] == k[i+1] == "#":
                    print("No")
                    quit()
            print("Yes")
        else:
            k = s[b:d+1]
            for i in range(d-b):
                if k[i] == k[i+1] == "#":
                    print("No")
                    quit()
            k = s[a:c+1]
            for i in range(c-a):
                if k[i] == k[i+1] == "#":
                    print("No")
                    quit()
            k = s[b-1:d+2]
            for i in range(len(k)-2):
                if k[i] == k[i+1] == k[i+2] == ".":
                    print("Yes")
                    quit()
            print("No")
    return

#B
def B():
    s = S()

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
    A()
