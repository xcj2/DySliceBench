def examB():
    St = S()
    N = len(St)
    is_evenl = True
    cur = 0
    for i in range((N-1)//2):
        is_evenl = True
        for j in range(i+1):
            if St[j]!=St[i+j+1]:
                is_evenl = False
#                print(j, i + j + 1)
        if is_evenl:
            cur = (i+1)*2
    print(cur)


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

examB()
