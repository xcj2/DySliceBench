def examA():
    N = I()
    ans = (N-1)//2
    print(ans)
    return

def examB():
    N = I()
    D = LI()
    d = Counter(D)
    loop = max(d.keys())
    if D[0]!=0 or d[0]!=1:
        print(0)
        return
#    print(d,loop)
    ans = 1; cur = 1
    for i in range(loop+1):
        if d[i]==0:
            print(0)
            return
        for _ in range(d[i]):
            ans *= cur
            ans %= mod2
        cur = d[i]
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()

"""

"""