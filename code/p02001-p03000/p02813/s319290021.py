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
    examC()
