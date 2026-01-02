def examA():
    S, T = LSI()
    ans = T+S
    print(ans)
    return

def examB():
    A, B, K = LI()
    if A>K:
        A -=K
        print(A,B)
        return
    if A+B>K:
        B -=(K-A)
        A = 0
        print(A,B)
        return
    A = 0; B = 0
    print(A,B)
    return

def examC():
    return

def examD():
    return

def examE():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examB()
