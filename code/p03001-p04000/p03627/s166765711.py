def examC():
    N = I()
    A = LI()
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    a = [0,0]
    for key,i in d.items():
        if i>=4:
            if a[1]<key:
                a = [key,key]
            elif a[0]<key:
                a = [key,a[1]]
        elif i>=2:
            if a[1]<key:
                a = [a[1],key]
            elif a[0]<key:
                a = [key,a[1]]
    ans = a[0]*a[1]
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
    examC()

"""

"""