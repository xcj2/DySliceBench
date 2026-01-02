#da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1,w):
        da[0][i] = da[0][i-1]+a[0][i]
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da

#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(da,p,q,x,y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]

def examD():
    N, K = LI()
    #y=0,x=0上で、原点とおなじグループかどうか
    colorXY = [[0] * (2*K) for _ in range(2*K)]
    for _ in range(N):
        #原点の色を白(0)とする
        x, y, c = LSI()
        x, y = int(x), int(y)
        if c=="B":
            y +=K
        colorXY[x%(2*K)][y%(2*K)] +=1
    ans = 0
    ansC = N
    da = da_generate(2*K, 2*K, colorXY)
    for i in range(K):
        for j in range(K):
            cur = da_calc(da,0,0,K-i-1,K-j-1) + da_calc(da,K-i,K-j,2*K-i-1,2*K-j-1)\
                + da_calc(da,0,2*K-j,K-i-1,2*K-1) + da_calc(da,2*K-i,0,2*K-1,K-j-1)\
                + da_calc(da,2*K-i,2*K-j,2*K-1,2*K-1)
            ans = max(ans,cur)
            ansC = min(ansC,cur)
    print(max(ans,N-ansC))

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
