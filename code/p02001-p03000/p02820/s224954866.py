def examA():
    S, T = LSI()
    ans = T+S
    print(ans)
    return

def examB():
    A, B, K = LI()
    if A>K:
        A -=K
        print(A,B)
        return
    if A+B>K:
        B -=(K-A)
        A = 0
        print(A,B)
        return
    A = 0; B = 0
    print(A,B)
    return

def examC():
    def is_prime(n):
        if n == 1: return False
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True
    X = I()
    while(True):
        if is_prime(X):
            ans = X
            break
        X +=1
    print(ans)
    return

def examD():
    N, K = LI()
    R, S, P = LI()
    T = SI()
    C = Counter(T)
    sumT = C["r"]*P + C["s"]*R + C["p"]*S
#    print(sumT)
    ans = sumT
    d = defaultdict(bool)
    for i in range(K,N):
        if T[i]==T[i-K] and not d[i-K]:
            if T[i]=="r":ans -=P
            elif T[i]=="s":ans -=R
            else:ans -=S
            d[i] = True
    print(ans)
    return

def examE():
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
inf = float('inf')

if __name__ == '__main__':
    examD()
