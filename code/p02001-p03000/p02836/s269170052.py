def examB():
    S = SI(); N =len(S)
    ans = N//2
    for i in range(N//2):
        if S[i]==S[N-1-i]:
            ans -=1
    print(ans)
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examB()
