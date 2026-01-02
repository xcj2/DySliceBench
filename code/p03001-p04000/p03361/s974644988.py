def examC():
    H, W = LI()
    S = [SI() for _ in range(H)]
    ans = "Yes"
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                if (i>0 and S[i-1][j]==".") or i==0:
                    if (H-1>i and S[i+1][j]==".") or i==H-1:
                        if (j>0 and S[i][j-1]==".") or j==0:
                            if (W-1>j and S[i][j+1]==".") or j==H-1:
                                ans = "No"
    print(ans)


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

examC()