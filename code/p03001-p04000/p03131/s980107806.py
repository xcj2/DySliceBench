def examA():
    N, K = LI()
    if (N+1)//2>=K:
        print("YES")
    else:
        print("NO")
    return

def examB():
    d = [0]*4
    for _ in range(3):
        a, b = LI()
        a -=1; b -=1
        d[a] +=1
        d[b] +=1
    for i in d:
        if i>=3 or i==0:
            print("NO")
            return
    print("YES")
    return

def examC():
    K, A, B = LI()
    if A+1>=B:
        ans = K+1
        print(ans)
        return
    l = 0; r = K+1
    while(r-l>1):
        # 何回換金できるか
        now = (l+r)//2
        cur = K - now +1
        if cur<A:
            r = now
        else:
            l = now
    ans = K - l + (l//2)*(B-A) +1 + l%2
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
    examC()

"""

"""