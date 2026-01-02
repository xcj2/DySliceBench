def examA():
    N = I()
    A = LI()
    ans = 0
    for i in range(N-1):
        if A[i+1]==A[i]:
            A[i+1] = 101
            ans +=1
    print(ans)
    return

def gcd(x,y):
    if y==0:
        return x
    while(y!=0):
        x, y = y,x%y
    return x
def examB():
    T = I()
    for i in range(T):
        ans = "Yes"
        A, B, C, D = LI()
        if A<B:
            ans = "No"
        elif D<B:
            ans = "No"
        elif C>=B:
            print(ans)
            continue
        elif B-C>gcd(D,B):
            ans = "No"
        if (A % B) > C:
            ans = "No"
        print(ans)
    return

def examC():
    N = I()
    S = SI()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    loop = 2**N
    for i in range(loop):
        curR = ""; curB = ""
        curR2 = ""; curB2 = ""
        for j in range(N):
            if i&(1<<j)==(1<<j):
                curR +=S[j]
                curR2 +=S[j+N]
            else:
                curB +=S[j]
                curB2 +=S[j+N]
        d1[(curR,curB)] +=1
        d2[(curR2,curB2)] +=1
    ans = 0
    for key,i in d1.items():
        cur = i*d2[(key[1][::-1],key[0][::-1])]
        ans +=cur
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examB()
