def examC():
    N = I()
    A = LI()
    d0 = defaultdict(int); d0[0] = 0
    d1 = defaultdict(int); d1[0] = 0
    for i in range(N):
        if i%2==0:
            d0[A[i]] +=1
        else:
            d1[A[i]] +=1
    n0 = sorted(d0.items(),key=lambda x:x[1])
    n1 = sorted(d1.items(),key=lambda x:x[1])
#    print(n0); print(n1)
    if n0[-1][0]!=n1[-1][0]:
        ans = N - n0[-1][1] - n1[-1][1]
    else:
        ans = N - max(n0[-1][1]+n1[-2][1],n0[-2][1]+n1[-1][1])
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
global mod,mod2,inf,alphabet,ALPHABET
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examC()
