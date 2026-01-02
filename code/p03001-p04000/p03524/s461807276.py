def examB():
    S = SI()
    d = defaultdict(int)
    for s in S:
        d[s] +=1
    ans = "YES"
    if abs(d["a"]-d["b"])>1 or abs(d["b"]-d["c"])>1 or abs(d["c"]-d["a"])>1:
        ans = "NO"
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
