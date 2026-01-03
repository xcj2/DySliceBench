def examA():
    N, A, B = LI()
    if N==1:
        if A==B:
            print(1)
        else:
            print(0)
        return
    ans = (N-2)*max(B-A,0) + 1
    if B<A:
        ans = 0
    print(ans)
    return

def examB():
    S = SI()
    N = len(S)
    cnt = 0
    for i,s in enumerate(S):
        cnt += N-1
        if s=="U":
            cnt += i
        else:
            cnt += (N-i-1)
    ans = cnt
    print(ans)
    return

def examC():
    N, M, q = LI()
    S = [SI()for _ in range(N)]
    Q = [LI()for _ in range(q)]
    S1 = [[0]*(M+1) for _ in range(N+1)]
    S2 = [[0]*(M+1) for _ in range(N+1)]
    S3 = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        now = 0
        for j in range(M):
            now += int(S[i][j])
            S1[i+1][j+1] = S1[i][j+1]+now
    for i in range(N):
        now = 0
        for j in range(M-1):
            if S[i][j]=="1" and S[i][j+1]=="1":
                now += 1
            S2[i+1][j+1] += S2[i][j+1]+now
    for i in range(M):
        now = 0
        for j in range(N-1):
            if S[j][i]=="1" and S[j+1][i]=="1":
                now += 1
            S3[j+1][i+1] += S3[j+1][i]+now
    ans = [0]*q
    #print(S2)
    #print(S3)
    for i in range(q):
        x1, y1, x2, y2 = Q[i]
        #print(x1,y1,x2,y2)
        x1 -= 1; y1 -= 1
        cur = S1[x2][y2] - S1[x1][y2] - S1[x2][y1] + S1[x1][y1]
        cur -= S2[x2][y2-1] - S2[x1][y2-1] - S2[x2][y1] + S2[x1][y1]
        cur -= S3[x2-1][y2] - S3[x1][y2] - S3[x2-1][y1] + S3[x1][y1]
        ans[i] = cur
    for v in ans:
        print(v)
    return

def examD():
    A = I()
    B = I()

    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

def test():

    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
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
    examC()

"""
3 4 4 
1101 
0110 
1101 
1 1 3 4 
1 1 3 1 
2 2 3 4 
1 2 2 4 
"""