def examC():
    N = I()
    S = [I() for _ in range(N)]
    S1 = []
    for s in S:
        if s%10==0:
            continue
        S1.append(s)
    if S1==[]:
        print(0)
        return
    S1.sort()
    ans = sum(S)
    if ans%10==0:
        ans -= S1[0]
    print(ans)
    return

def examD():
    N, A, B = LI()
    H = [I() for _ in range(N)]
    H.sort()
    l = 0; r = (H[-1]-1)//B + 1
    while(r-l>1):
        now = (l+r)//2
        cur = 0
        for i in H:
            if i-now*B>0:
                cur += ((i-now*B-1)//(A-B) +1)
        if cur>now:
            l = now
        else:
            r = now
    ans = r
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