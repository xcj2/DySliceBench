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
