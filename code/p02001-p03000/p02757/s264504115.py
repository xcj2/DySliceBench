def examA():
    S = SI()
    if S=="AAA" or S=="BBB":
        print("No")
    else:
        print("Yes")
    return

def examB():
    N, A, B = LI()
    loop = N//(A+B)
    ans = loop*A + min(A,N%(A+B))
    print(ans)
    return

def examC():
    A, B = LI()
    ans = -1
    for i in range(1,20000):
        if i*8//100==A:
            if i*10//100==B:
                ans = i
                break
    print(ans)
    return

def examD():
    S = SI()
    Q = I()
    rev = 0
    L = ""; R = ""
    for _ in range(Q):
        q = LSI()
        if q[0]=="1":
            rev += 1
        else:
            c = int(q[1])
            if (c+rev)%2==1:
                L += q[2]
            else:
                R += q[2]
    ans = ""
    if rev%2==0:
        ans = L[::-1] + S + R
    else:
        ans = R[::-1] + S[::-1] + L
    print(ans)
    return

def examE():
    N, P = LI()
    S = SI()
    A = [0]*(N+1)
    cur = 0
    if P==5:
        ans = 0
        for i in range(N):
            if int(S[N-1-i])%5==0:
                ans += N-i
        print(ans)
        return
    elif P==2:
        ans = 0
        for i in range(N):
            if int(S[N-1-i])%2==0:
                ans += N-i
        print(ans)
        return

    for i in range(N):
        s = int(S[N-1-i])
        cur += s*pow(10,i,P)
        A[i+1] = cur%P
    D = [0]*P
    for a in A:
        D[a] += 1
    ans = 0
    #print(A)
    for d in D:
        ans += d*(d-1)//2

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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examE()

"""

"""