def examA():
    N = I()
    S = [""]*N; T = [""]*N
    for i in range(N):
        S[i],T[i] = LSI()
        T[i] = int(T[i])
    X = SI()
    ans = 0
    flag = False
    for i in range(N):
        if flag:
            ans +=T[i]
        if S[i]==X:
            flag = True
    print(ans)
    return

def examB():
    return

def examC():
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
    examA()
