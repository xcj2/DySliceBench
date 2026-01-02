def examA():
    S = SI()
    F = "FESTIVAL"
    ans = S[:-(len(F))]
    print(ans)
    return

def examB():
    N = I()
    d = defaultdict(int)
    D = LI()
    for t in D:
        d[t] +=1
    M = I()
    T = LI()
    for t in T:
        if d[t]==0:
            print("NO")
            return
        d[t] -=1
    print("YES")
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
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