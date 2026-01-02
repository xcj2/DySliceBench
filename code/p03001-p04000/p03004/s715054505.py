def examA():
    import numpy as np
    def powDetMod(n,arr,k,MOD=-1):
        repeat = 60
        local_doubling = [[] for _ in range(repeat+1)]
        local_doubling[0] = arr
        for i in range(repeat):
            local_doubling[i+1] = np.dot(local_doubling[i],local_doubling[i])
            if MOD>0:
                for h in range(n):
                    for w in range(n):
                        local_doubling[i+1][h][w] %= MOD
        now = [[1 if i==j else 0 for i in range(n)]for j in range(n)]
        for i in range(repeat+1):
            if k&(1<<i)>0:
                now = np.dot(now,local_doubling[i])
                if MOD > 0:
                    for h in range(n):
                        for w in range(n):
                            now[h][w] %= MOD
        return now
    L, A, B, M = LI()
    C = [0]*18
    cnt = L
    for i in range(18):
        if (pow(10,(i+1))-1-A)<0:
            continue
        C[i] = 1 + (pow(10,(i+1))-1-A)//B
        if (pow(10,i)-1-A)>=0:
            C[i] -= 1 + (pow(10,i)-1-A)//B
        if C[i]>=cnt:
            C[i] = cnt
            break
        cnt -= C[i]
    #print(C)
    X =  np.array([0,A,B])
    for i in range(18):
        now = [[pow(10,i+1,M),0,0],[1,1,0],[0,1,1]]
        now = np.array(now)
        arr = powDetMod(3,now,C[i],M)
        X = np.dot(X,arr)%M

    ans = X[0]%M
    print(ans)
    return

def examB():
    N = I()
    R = [inf,-inf]
    L = [inf,-inf]
    U = [inf,-inf]
    D = [inf,-inf]
    X = [inf,-inf]
    Y = [inf,-inf]
    for _ in range(N):
        x,y,s = LSI()
        x,y = int(x),int(y)
        if s=="R":
            if x<R[0]: R[0] = x
            if x>R[1]: R[1] = x
            if y<Y[0]: Y[0] = y
            if y>Y[1]: Y[1] = y
        elif s=="L":
            if x<L[0]: L[0] = x
            if x>L[1]: L[1] = x
            if y<Y[0]: Y[0] = y
            if y>Y[1]: Y[1] = y
        elif s=="U":
            if y<U[0]: U[0] = y
            if y>U[1]: U[1] = y
            if x<X[0]: X[0] = x
            if x>X[1]: X[1] = x
        elif s=="D":
            if y<D[0]: D[0] = y
            if y>D[1]: D[1] = y
            if x<X[0]: X[0] = x
            if x>X[1]: X[1] = x
    def calc_area(t):
        x = max(R[1]+t,L[1]-t,X[1])-min(R[0]+t,L[0]-t,X[0])
        y = max(U[1]+t,D[1]-t,Y[1])-min(U[0]+t,D[0]-t,Y[0])
        if x<=0 or y<=0:
            return 0
        return x*y
    ans = calc_area(0)
    for i in [0,1]:
        for j in [0,1]:
            if R[i] <= X[j]:
                T = (X[j] - R[i])
                ans = min(ans, calc_area(T))
            if L[i] >= X[j]:
                T = (L[i] - X[j])
                ans = min(ans, calc_area(T))
            if R[i] <= L[j]:
                T = dec((L[j] - R[i]) / 2)
                ans = min(ans, calc_area(T))

            if U[i] <= Y[j]:
                T = (Y[j] - U[i])
                ans = min(ans, calc_area(T))
            if D[i] >= Y[j]:
                T = (D[i] - Y[j])
                ans = min(ans, calc_area(T))
            if U[i] <= D[j]:
                T = dec((D[j] - U[i]) / 2)
                ans = min(ans, calc_area(T))

    print(ans)
    return

from decimal import Decimal as dec
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
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examB()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""