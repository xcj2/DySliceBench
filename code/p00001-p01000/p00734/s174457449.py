from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

while True:
    n,m = inpl()
    if n == 0:
        break
    else:
        aa = [inp() for _ in range(n)]
        bb = [inp() for _ in range(m)]
        Sa = sum(aa)
        Sb = sum(bb)
        for a in aa:
            for b in bb:
                if Sa-a+b == Sb+a-b:
                    print(a,b)
                    break
            else:
                continue
            break
        else:
            print(-1)

