def examA():
    S = SI()
    ans = "Good"
    for i in range(len(S)-1):
        if S[i+1]==S[i]:
            ans = "Bad"
    print(ans)
    return

def examB():
    N, L = LI()
    ans = 0
    if L>=0:
        for i in range(N - 1):
            ans += (L + i + 1)
    else:
        for i in range(N):
            ans += (L+i)
        if L+N-1<0:
            ans -=(L+N-1)
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examB()
