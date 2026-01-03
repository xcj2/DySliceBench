def examA():
    Alpha = [chr(i) for i in range(97, 97+26)]
    S = SI(); N = len(S)
    ans = -1
    for i in range(N):
        for s in Alpha:
            cur = [s for s in S]
            for l in range(i):
                for k in range(N-1):
                    if cur[k+1]==s:
                        cur[k]=s
 #           print(cur)
            if len(Counter(cur[:N-i]))==1:
                ans = i
                break
        if ans>=0:
            break
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
    examA()
