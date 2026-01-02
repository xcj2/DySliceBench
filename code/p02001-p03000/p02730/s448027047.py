def examA():
    N, M = LI()
    ans = N*(N-1)//2 + M*(M-1)//2
    print(ans)
    return

def examB():
    def judge(A):
        #print(A)
        n = len(A)
        for i in range(n//2):
            if A[i]!=A[n-i-1]:
                return False
        return True
    S = SI()
    N = len(S)
    if not judge(S):
        print("No")
        return
    if judge(S[:(N-1)//2]) and judge(S[(N+1)//2:]):
        print("Yes")
    else:
        print("No")
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

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examB()

"""

"""