def examB():
    A = SI(); N = len(A)
    d = defaultdict(int)
    for s in A:
        d[s] +=1
#    print(d)
    ans = N*(N-1)//2 +1
    for i in d.values():
        ans -= i*(i-1)//2
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
