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
    if N==3:
        print("2 5 63")
        return
    if N%2==0:
        ans = [2, 4, 3, 9]
        now = 4
        cur = 10
    else:
        ans = [2, 4, 3, 9]
        now = 4
        cur = 10
    while(cur<=30000):
        if N-1<=now:
            break
        ans.append(cur)
        ans.append(cur-2)
        cur += 6; now += 2
    cur = 21
    while(cur<=30000):
        if N-1<=now:
            break
        ans.append(cur)
        ans.append(cur-6)
        cur += 12; now += 2
    for i in range(N-now):
        cur = (i+1)*6
        ans.append(cur)
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
    examB()

"""

"""