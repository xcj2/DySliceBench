def examC():
    N= I()
    A = LI()
    cur = 0
    for i in A:
        while(True):
            if i % 2 == 0:
                i //= 2
                cur += 1
            else:
                break
    print(cur)



import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
