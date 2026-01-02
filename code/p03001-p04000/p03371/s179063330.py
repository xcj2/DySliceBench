def ABC106_B():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors
    N = I()
    ans = 0
    for i in range((N+1)//2):
        cur = i*2+1
        if len(make_divisors(cur))==8:
            ans += 1
    print(ans)
    return

def ABC122_B():
    S = SI()
    ans = 0
    cur = 0
    d = {"A","C","G","T"}
    for s in S:
        if s in d:
            cur += 1
        else:
            ans = max(ans,cur)
            cur = 0
    ans = max(ans,cur)
    print(ans)
    return

def paken2019_C():
    N, M = LI()
    A = [LI()for _ in range(N)]
    T = [i for i in range(M)]
    ans = 0
    for t1,t2 in itertools.permutations(T,2):
        cur = 0
        for i in range(N):
            cur += max(A[i][t1],A[i][t2])
        ans = max(ans,cur)
    print(ans)
    return

def ABC95_C():
    A, B, C, X, Y = LI()
    if A+B<=C*2:
        ans = A*X+B*Y
    else:
        if X>Y:
            ans = Y*C*2 + min(A,C*2)*(X-Y)
        else:
            ans = X*C*2 + min(B,C*2)*(Y-X)
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
    ABC95_C()

"""

"""