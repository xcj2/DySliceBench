def examC():
    N, A, B, C = LI()
    L = [I() for _ in range(N)]
    loop = 4**N; ans = 10**9
    for i in range(loop):
        cur = 0
        curA = 0; curB = 0; curC = 0
        for j in range(N):
            judge = (i//(4**j))%4
            if judge==1:
                if curA>0:
                    cur +=10
                curA += L[j]
            elif judge==2:
                if curB>0:
                    cur +=10
                curB += L[j]
            elif judge==3:
                if curC>0:
                    cur +=10
                curC += L[j]
        if curA==0 or curB==0 or curC==0:
            continue
        cur += abs(curA-A)
        cur += abs(curB-B)
        cur += abs(curC-C)
        ans = min(cur,ans)
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

if __name__ == '__main__':
    examC()
