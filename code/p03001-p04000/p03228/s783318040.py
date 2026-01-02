def examA():
    S = SI()
    if len(S)==3:
        ans = S[::-1]
    else:
        ans = S
    print(ans)
    return

def examB():
    A, B, K = LI()
    for i in range(K):
        if i%2==0:
            B +=A//2
            A //=2
        else:
            A +=B//2
            B //=2
    print(A,B)
    return

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

if __name__ == '__main__':
    examB()
