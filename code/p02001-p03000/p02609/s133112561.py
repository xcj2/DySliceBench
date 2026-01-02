def examA():
    L, R, D = LI()
    ans = R//D - (L-1)//D
    print(ans)
    return

def examB():
    N = I()
    A = LI()
    ans = 0
    for i,a in enumerate(A):
        if i%2==0:
            if a%2==1:
                ans += 1
    print(ans)
    return

def examC():
    N = I()
    ans = [0]*N
    for x in range(1,101):
        for y in range(1,101):
            for z in range(1,101):
                cur = x**2 + y**2 + z**2 + x*y + y*z + x*z
                if cur<N+1:
                    ans[cur-1] += 1

    for v in ans:
        print(v)
    return

def examD():
    def popcnt0(n):
        c = 0
        for i in range(20):
            c += (n >> i) & 1
        return c
    def cnt(num):
        c = 0
        while(num>0):
            #num %= bin(num).count("1")
            num %= popcnt0(num)
            c += 1
        return c
    N = I()
    X = SI()
    S_upper = [0]*N
    S_lower = [0]*N
    start_upper = 0
    start_lower = 0
    bit = 0
    ans = [0]*N
    for s in X:
        if s=="1":
            bit += 1
    if bit==1:
        b = 0
        for i in range(N):
            if X[i]=="1":
                ans[i] = 0
                b = i
            else:
                ans[i] = 1
        if b==N-1:
            for i in range(N-1):
                ans[i] += 1
        else:
            ans[-1] += 1
        for v in ans:
            print(v)
        return
    elif bit==0:
        for v in ans:
            print(1)
        return
    for i in range(N):
        S_upper[i] = pow(2,N-i-1,bit+1)
        S_lower[i] = pow(2,N-i-1,bit-1)
        if X[i]=="1":
            start_upper += S_upper[i]
            start_lower += S_lower[i]
            start_upper %= (bit+1)
            start_lower %= (bit-1)
    for i in range(N):
        if X[i]=="0":
            cur = (start_upper + S_upper[i]) % (bit+1)
            ans[i] = cnt(cur)+1
        else:
            cur = (start_lower - S_lower[i] + 2*(bit -1)) % (bit-1)
            ans[i] = cnt(cur)+1
        #print(cur)

    for v in ans:
        print(v)
    return

def examE():
    T = I()
    ans = [0]*T

    for t in range(T):
        pass


    for v in ans:
        print(v)
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

sys.setrecursionlimit(2*10**6)

if __name__ == '__main__':
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""