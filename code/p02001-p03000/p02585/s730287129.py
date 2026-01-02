def main():
    examC()

def examA():
    S = SI()
    S = ">" + S + "<"
    N = len(S)
    A = [0]*N
    i = 0
    while(i<N-1):
        r = i + 1
        if S[i]==">" and S[i+1]=="<":
            A[i] = 0
            l = i-1
            cur = 0
            while(1<=l):
                cur += 1
                A[l] = max(A[l], cur)
                l -= 1
                if S[l+1]=="<":
                    #print("break",l,A)
                    break
            r = i+1
            cur = 0
            while(r<N-1):
                cur += 1
                A[r] = max(A[r], cur)
                r += 1
                if r==N-1:
                    break
                if S[r]==">":
                    break
        #print(i,A)
        i = r
    #print(A)
    A[0] = 0; A[-1] = 0
    ans = sum(A)
    print(ans)
    return

def examB():
    H, W = LI()
    A = [SI()for _ in range(H)]
    C = defaultdict(int)
    for a in A:
        for s in a:
            C[s] += 1
    B = sorted(C.items())
    # print(B)
    flag_odd = not (H%2==1 and W%2==1)
    upper_2 = (H%2==1) * (W//2) + (W%2==1) * (H//2)
    for s,c in B:
        if c%2==1:
            if flag_odd:
                print("No")
                return
            flag_odd = True
        elif c%4==2:
            upper_2 -= 1
            if upper_2<0:
                print("No")
                return
    print("Yes")
    return

def examC():
    N, K = LI()
    P = LI()
    C = LI()

    if max(C)<0:
        print(max(C))
        return

    loop = [[0,0]for _ in range(N)]

    for i in range(N):
        checked = set()
        now = i
        score = 0
        while(now not in checked):
            checked.add(now)
            now = P[now]-1
            score += C[now]
        n = len(checked)
        for j in checked:
            loop[j] = [n,score]
    # print(loop)
    ans = 0
    for i in range(N):
        n,s = loop[i]
        score = 0
        if s>0:
            score += (K//n - 1) * s
        ans = max(ans,score)
        now = i
        for j in range(n + K%n):
            now = P[now] - 1
            score += C[now]
            ans = max(ans,score)

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

def test():
    i = I()
    li = LI()
    lsi = LSI()
    si = LS()
    print(i)
    print(li)
    print(lsi)
    print(si)
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