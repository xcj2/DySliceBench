def examA():
    N = 26
    D = I()
    C = LI()
    S = [LI()for _ in range(N)]
    ans = [0]*D

    for v in ans:
        print(v)
    return

def examB():
    N = 26
    D = I()
    C = LI()
    S = [LI()for _ in range(D)]
    T = [I()for _ in range(D)]
    ans = [0]*D
    used = [0]*N
    for i,t in enumerate(T):
        ans[i] += ans[i-1]
        t -= 1
        ans[i] += S[i][t]
        used[t] = i+1
        for j in range(N):
            ans[i] -= C[j]*(i+1-used[j])
    for v in ans:
        print(v)
    return

def examC():
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
    examB()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""