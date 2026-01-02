def examA():
    L = LI(); L.sort()
    ans = L[0]*L[1]//2
    print(ans)
    return

def examB():
    def fun(s):
        if s%2==0:
            return s//2
        else:
            return s*3+1
    S = I()
    d = defaultdict(bool)
    d[S] = True; cur = 1
    while(True):
        cur +=1
        S = fun(S)
        if d[S]:
            break
        d[S] = True
    print(cur)
    return

def examC():
    N = I()
    H = LI()
    cur = 0
    ans =0
    for i in range(N):
        if cur<H[i]:
            ans += H[i]-cur
        cur = H[i]
    print(ans)
    return

def examD():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,ALPHABET, _ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 1e-9
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examC()
