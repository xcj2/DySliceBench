def main():
    examC()

def examA():
    S = SI()
    if S[-1]=="s":
        ans = S+"es"
    else:
        ans = S+"s"
    print(ans)
    return

def examB():
    N = I()
    D = [LI()for _ in range(N)]
    current = 0
    for d1,d2 in D:
        if d1==d2:
            current += 1
        else:
            current = 0
        if current==3:
            print("Yes")
            return
    print("No")
    return

def examC():
    N = I()
    cnt = 0
    for i in range(1,N):
        for j in range(1,1+N//i-(N%i==0)):
            cnt += 1
    ans = cnt
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
global mod,mod2,inf,alphabet,alphabet_convert,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 1<<31
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    main()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""