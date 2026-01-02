def examA():
    N, A, B = LI()
    ans = inf
    if abs(A-B)%2==0:
        ans = abs(A-B)//2
    cur = min((A+B-1)//2,(2*N-A-B+1)//2)
    ans = min(ans,cur)
    print(ans)
    return

def examB():
    return

def examC():
    return

def examD():
    return

def examE():
    return

def examF():
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
    examA()
