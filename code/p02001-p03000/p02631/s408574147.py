def examA():
    S = SI()
    if S in alphabet:
        ans = "a"
    else:
        ans = "A"
    print(ans)
    return

def examB():
    N, K = LI()
    P = LI()
    P.sort()
    ans = sum(P[:K])
    print(ans)
    return

def examC():
    N = I()
    ans = ""
    while(N>0):
        N -= 1
        ans += alphabet[N%26]
        N //= 26
        if N==0:
            break
    print(ans[::-1])
    return

def examD():
    N = I()
    A = LI()
    D = defaultdict(int)
    for a in A:
        D[a] += 1
    S = sum(A)
    q = I()
    ans = [0]*q
    for i in range(q):
        a, b = LI()
        if not a in D:
            ans[i] = S
            continue
        S += (b-a)*D[a]
        D[b] += D[a]
        D[a] = 0
        ans[i] = S

    for v in ans:
        print(v)
    return

def examE():
    N = I()
    A = LI()
    S = 0
    for a in A:
        S ^= a
    #print(S)
    ans = [0]*N
    for i in range(N):
        ans[i] = S^A[i]
    print(" ".join(map(str,ans)))
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
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""