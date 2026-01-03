def examC():
    N = I(); A = [I() for _ in range(N)]
    AS = sorted(A)
    A0 = A[::2]
    d = defaultdict(bool)
    for i in AS[::2]:
        d[i] = True
    ans = 0
    for i in A0:
        if not d[i]:
            ans +=1
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