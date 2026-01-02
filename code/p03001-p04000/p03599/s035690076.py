def examC():
    A, B, C, D, E, F = LI()
    water =set()
    for i in range(30):
        for j in range(30):
            if 100 * (i*A+j*B) > F or (i==0 and j==0):
                continue
            water.add(100 * (A*i+B*j))
    sugar = set()
    for i in water:
        j = 0
        while(True):
            if (j * C) * 100 > i * E or i+(j*C)>F:
                break
            k = 0
            while(True):
                if (j*C+k*D)*100>i*E or i+(j*C+k*D)>F:
                    j +=1
                    break
                sugar.add((i+j*C+k*D,j*C+k*D))
                k +=1
    ans = [0,0]; cur = float(-1)
    for i in sugar:
        if cur<i[1]/i[0]:
            ans = [i[0],i[1]]
            cur = i[1]/i[0]
    print(" ".join(map(str,ans)))
#    print(sugar)


import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()