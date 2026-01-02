def examA():
    S = SI()
    N = len(S)
    if N<26:
        d = defaultdict(bool)
        for s in S:
            d[s] = True
        for a in alphabet:
            if not d[a]:
                ans = S + a
                print(ans)
                return
    keep = []
    for i in range(N-1)[::-1]:
        keep.append(S[i+1])
        if S[i]<S[i+1]:
            break
    #print(keep)
    n = len(keep)
    c = "zz"
    for s in keep:
        if s>S[(N-n-1)]:
            c = min(c,s)
    if c=="zz":
        print(-1)
        return
    ans = S[:(N-n-1)] + c
    print(ans)
    return

def examB():
    N = I()
    ans = [2*(i+1) for i in range(N)]
    if N%2==0:
        for i in range(4998):
            ans[-3-i] = 3+i*6

    print(" ".join(map(str,ans)))
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
    examA()

"""

"""