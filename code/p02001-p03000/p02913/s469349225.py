def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
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
    # https://tjkendev.github.io/procon-library/python/string/z-algorithm.html
    def z_algo(S):
        N = len(S)
        A = [0] * N
        i = 1; j = 0
        A[0] = l = len(S)
        while i < l:
            while i + j < l and S[j] == S[i + j]:
                j += 1
            if not j:
                i += 1
                continue
            A[i] = j
            k = 1
            while l - i > k < j - A[k]:
                A[i + k] = A[k]
                k += 1
            i += k; j -= k
        return A
    N = I()
    S = SI()
    ans = 0
    for i in range(N):
        Z = z_algo(S[i:])
        for k,n in enumerate(Z[1:]):
            cur = min(k+1,n)
            ans = max(ans,cur)
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
    examE()

"""

"""