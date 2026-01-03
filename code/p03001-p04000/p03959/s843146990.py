def examA():
    S = SI()
    ans = "No"
    flag = False
    for s in S:
        if flag:
            if s=="F":
                ans = "Yes"
                break
        else:
            if s=="C":
                flag = True
    print(ans)
    return

def examB():
    K, T = LI()
    A = LI(); A.sort()
    ans = max(0,A[-1]*2-sum(A)-1)
    print(ans)
    return

def examC(mod):
    N = I()
    T = LI(); A = LI()
    H = [0]*N
    ans = 1
    if T[-1] != A[0]:
        ans = 0
    H[0] = T[0]; H[N-1] = A[N-1]
    for i in range(N-1):
        if T[i+1]>T[i]:
            if H[i+1]==0:
                H[i+1] = T[i+1]
            elif H[i+1]!=T[i+1]:
                ans = 0
        else:
            if H[i+1]==0:
                H[i+1] = -T[i+1]
    for i in range(N-1,0,-1):
        if A[i-1]>A[i]:
            if H[i-1]==0:
                H[i-1] = A[i-1]
            elif H[i-1]<0:
                if -H[i-1]<A[i-1]:
                    ans = 0
                else:
                    H[i-1] = A[i-1]
            elif H[i-1]!=A[i-1]:
                ans = 0
#    print(H)
    flag = False; cur = 0
    for i in H:
        if flag:
            if i<0:
                cur +=1
            else:
                ans *=(min(now,i)**cur)%mod
                ans %=mod
                flag = False
                cur = 0; now = i
        else:
            if i<0:
                cur = 1
                flag = True
            else:
                now = i
    print(ans%mod)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC(mod)
