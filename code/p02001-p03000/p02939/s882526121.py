def examA():
    S = SI(); N = len(S)
    prev = S[0]; cur = ""
    k = 0; ans = 1
    while(k<N-1):
        k +=1
        cur += S[k]
        if cur==prev:
            continue
        prev = cur
        cur = ""
        ans +=1
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
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examA()
