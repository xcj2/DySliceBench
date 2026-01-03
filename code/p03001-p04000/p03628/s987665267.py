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
    N = I()
    S = [SI() for _ in range(2)]
    ans = 1
    flag = 0
    i = 0
    while(i<N):
        if S[0][i]==S[1][i]:
            if flag==1:
                ans *= 2
            elif flag==0:
                ans *= 3
            flag = 1
        else:
            if flag==0:
                ans *= 6
            elif flag==1:
                ans *= 2
            elif flag==2:
                ans *= 3
            flag = 2
        i += flag
        ans %= mod
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
    examD()

"""

"""