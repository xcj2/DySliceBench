def examC():
    N = I()
    A = [0]*N; xy = [[] for _ in range(N)]
    for i in range(N):
        A[i] = I()
        for j in range(A[i]):
            s1,s2 = LI()
            xy[i].append([s1,s2])
#    print(xy)
    loop = 2**N; differ = 2**4
    ans = 0
    for i in range(loop):
        uso = [False]*N
        honto = [False]*N
        cur = 0
        for j in range(N+1):
            if i&(2**j)==(2**j):
                cur +=1
#        print(i,cur)
        for j in range(N):
            if i&(2**j)==(2**j):
                for k in xy[j]:
                    if k[1]==0:
                        uso[k[0]-1] = True
                    elif k[1]==1:
                        honto[k[0]-1] = True
#チェック
        for j in range(N):
            if uso[j] and i&(2**j)==(2**j):
                cur = 0
                break
            if honto[j] and i&(2**j)==0:
                cur = 0
                break
        ans = max(ans,cur)
    print(ans)

    return

def examD(mod):
    N = I(); A = LI()
    d = defaultdict(int)
    for i in range(N):
        cur = A[i]
        j = 1
        while(cur>0):
            if cur&1==1:
                d[j] +=1
            j +=1
            cur >>=1
    ans = 0
    for i,j in d.items():
        ans += j*(N-j) * 2**(i-1)
        ans %=mod
    print(ans)
    return

def examE():
    return

def examF():
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
    examC()
