def examA():
    H, W = LI()
    S = [LSI() for _ in range(H)]
    Alpha = [chr(ord('A') + i) for i in range(26)]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="snuke":
                ans = str(Alpha[j]) + str(i+1)
    print(ans)
    return

def examB():
    N = I()
    ans = []
    cur = int((N*2-1)**0.5)+1
    ansC = (cur+1)*cur//2
    neg = ansC-N
    if neg>cur:
        cur -=1
        ansC = (cur + 1) * cur // 2
        neg = ansC - N
    for i in range(1,cur+1):
        if i!=neg:
            ans.append(i)
    for v in ans:
        print(v)
#    print(cur,neg)
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
    examB()
