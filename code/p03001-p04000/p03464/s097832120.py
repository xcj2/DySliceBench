def examA():
    N = I()
    A = LI()
    if A[-1]!=2:
        print(-1)
        return
    l = 2; r = 2
    for a in A[::-1]:
        ner = (r//a+1)*a-1
        nel = ((l-1)//a+1)*a
        r = ner; l = nel
        if r<l:
            print(-1)
            return
    print(l,r)
    return

def examB():
    N, M = LI()

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

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examA()

"""

"""