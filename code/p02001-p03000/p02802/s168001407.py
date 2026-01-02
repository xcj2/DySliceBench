def examA():
    C = SI()
    ans = chr(ord(C)+1)
    print(ans)
    return

def examB():
    N,K,M = LI()
    A = LI()
    ans = N*M-sum(A)
    if ans>K:
        ans = -1
    elif ans<0:
        ans = 0
    print(ans)
    return

def examC():
    N, M = LI()
    ansT = 0; ansP = 0
    d = defaultdict(bool)
    WA = [0]*(N+1)
    for i in range(M):
        S, P = LSI()
        S = int(S)
        if P=="WA":
            WA[S] +=1
        elif P=="AC":
            if d[S]:
                continue
            else:
                d[S] = True
                ansT +=1
                ansP +=WA[S]
    print(ansT,ansP)
    return

def examE():
    return

def examF():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
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
