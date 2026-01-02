def examA():
    AB = LI(); AB.sort()
    ans = 0
    if AB[1]==1:
        ans += 400000
    for i in range(2):
        if AB[i]==1:
            ans +=300000
        elif AB[i]==2:
            ans +=200000
        elif AB[i]==3:
            ans +=100000
    print(ans)


def examB():
    return

def examC():
    return

def examD():
    return

def examE():
    return

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examA()
