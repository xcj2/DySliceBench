def examA():
    K, X = LI()
    if K*500>=X:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    return

def examB():
    N = I()
    S = SI()
    ans = 0
    for i in range(N-2):
        if S[i:i+3]=="ABC":
            ans +=1
    print(ans)
    return

def examC():
    N = I()
    P = LI()
    Q = LI()
    Cp = [i for i in itertools.permutations(P,N)]; Cp.sort()
    Cq = [i for i in itertools.permutations(Q, N)]; Cq.sort()
#    print(Cp)
#    print(Cq)
    for k,i in enumerate(Cp):
        flag = True
        for j in range(N):
            if P[j]!=i[j]:
                flag = False
                break
        if flag:
            a = k
            break
    for k,i in enumerate(Cq):
        flag = True
        for j in range(N):
            if Q[j]!=i[j]:
                flag = False
                break
        if flag:
            b = k
            break
    ans = abs(a-b)
    print(ans)
    return

def gcd(x,y):
    if y==0:
        return x
    while(y!=0):
        x, y = y,x%y
    return x
def lcm(x, y):
    return x * y // gcd(x, y)
def examD():
    N, M = LI()
    A = LI()
    flag = 0
    for i in range(1,32):
        if A[0]%(2**i)==0:
            flag +=1
        else:
            break
#    print(flag)
    for a in A:
        cur = 0
        for i in range(1, 32):
            if a % (2 ** i) == 0:
                cur += 1
            else:
                break
        if cur!=flag:
            print(0)
            return
    cur = A[0]
    for i in range(1,N):
        cur = lcm(cur,A[i])
        if cur>2*M:
            print(0)
            return
    ans = 1 + (M-cur//2)//cur
    print(ans)
    return

def examE():
    N = I()
    C = LI()


    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()
