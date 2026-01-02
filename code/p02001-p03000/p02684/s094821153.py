def examA():
    S = SI()
    T = SI()
    if S==T[:len(S)]:
        if len(S)+1==len(T):
            print("Yes")
            return
    print("No")
    return

def examB():
    A, B, C, K = LI()
    ans = 0
    if A>=K:
        ans = K
    else:
        ans += A
        K -= A
        if K>B:
            K -= B
            ans -= K
    print(ans)
    return

def examC():
    N, M, X = LI()
    C = [LI()for _ in range(N)]
    loop = 2**N
    ans = inf
    for l in range(loop):
        cur = 0
        A = [0]*M
        for j in range(N):
            if (1<<j)&l>0:
                cur += C[j][0]
                for k in range(M):
                    A[k] += C[j][k+1]
        flag = True
        for i in range(M):
            if A[i]<X:
                flag = False
                break
        if flag:
            ans = min(ans,cur)
    if ans==inf:
        print(-1)
        return
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    locat_doubling = [[0]*N for _ in range(100)]
    for i in range(N):
        locat_doubling[0][i] = i
        locat_doubling[1][i] = A[i]-1
    for k in range(2,100):
        for i in range(N):
            locat_doubling[k][i] = locat_doubling[k-1][locat_doubling[k-1][i]]
    #print(locat_doubling)
    ans = [i for i in range(N)]
    for k in range(100):
        for i in range(N):
            if K&(1<<k)>0:
                ans[i] = locat_doubling[k+1][ans[i]]
    print(ans[0]+1)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""