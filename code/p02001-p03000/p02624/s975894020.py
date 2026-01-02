def examA():
    N = I()
    ans = N + N**2 + N**3
    print(ans)
    return

def examB():
    S = SI()
    T = SI()
    ans = 0
    for s,t in zip(S,T):
        if s!=t:
            ans += 1
    print(ans)
    return

def examC():
    N, M, K = LI()
    A = LI()
    B = LI()
    SA = 0
    b = 0
    SB = 0
    for i in range(M):
        if SB+B[i]>K:
            break
        SB += B[i]
        b += 1
    #print(b,SB)
    ans = 0
    ans = max(ans,b)
    for i in range(N):
        SA += A[i]
        if SA+SB>K:
            while(b>=0):
                if SA+SB<=K:
                    break
                SB -= B[b-1]
                b -= 1
        if b==-1:
            break
        #print(i,b,SA,SB)

        ans = max(ans,b+i+1)
    print(ans)
    return

def examD():
    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]
    N = I()
    P = primes(N)
    #print(P)
    D = [1]*(N+1)
    for p in P:
        for i in range(1,1+N//p):
            cnt = 1
            cur = i
            while(cur%p==0):
                cnt += 1
                cur //= p
            D[p*i] *= (1+cnt)

    ans = 0
    for i in range(1,N+1):
        ans += i*D[i]
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

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""