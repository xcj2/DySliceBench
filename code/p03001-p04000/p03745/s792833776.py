def examA():
    N = I()
    A = LI()
    ans = 1
    flag = None
    for i in range(N-1):
        cur = A[i+1] - A[i]
        if not flag:
            if cur<0:
                flag = "d"
            elif cur>0:
                flag = "u"
        else:
            if cur<0 and flag=="u":
                flag = None
                ans += 1
            elif cur>0 and flag=="d":
                flag = None
                ans += 1
    print(ans)
    return

def examB():
    ans = 0
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

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examA()

"""

"""