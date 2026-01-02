def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
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
    ans = 0
    print(ans)
    return

def examF():
    def bitdp(l, r):
        n = r.bit_length()
        dp = defaultdict(int)
        dp[0, 0, 0, 0] = 1
        for i, less, greater, start in itertools.product(range(n), (0, 1), (0, 1), (0, 1)):
            R_ = 1 if less else (r>>(n-i-1))&1
            L_ = 0 if greater else (l>>(n-i-1))&1
            for y in range(R_ + 1):
                for x in range(L_, y + 1):
                    less_ = less or y < R_
                    greater_ = greater or L_ < x
                    start_ = start or (y==1 and x==1)

                    if not start and (y==1 and x==0):
                        # xorがあまりを確実に上回る
                        continue

                    dp[i + 1, less_, greater_, start_] += dp[i, less, greater, start]
                    dp[i + 1, less_, greater_, start_] %= mod
                    #print(dp[i + 1, less_, greater_, start_],i+1,less_,greater,start_,start)

        #for i in range(n):
        #    print(dp[i,0,0,0],dp[i,1,0,0],dp[i,0,1,0],dp[i,1,1,0])

        res = sum(dp[n, less, greater, 1] for less, greater in itertools.product((0, 1), (0, 1)))
        return res
    L, R = LI()
    ans = bitdp(L,R) % mod
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
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""