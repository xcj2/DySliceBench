from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def main():
    n,k = inpl()
    xary = []; yary = []
    a = []
    x_append = xary.append
    y_append = yary.append
    a_append = a.append
    for i in range(n):
        x,y = inpl()
        xary.append(x)
        yary.append(y)
        a.append((x,y))
    xary.sort(); yary.sort()
    res = INF
    for xi in range(n-1):
        for xj in range(xi+1,n):
            for yi in range(n-1):
                for yj in range(yi+1,n):
                    cnt = 0
                    l = xary[xi]; r = xary[xj]
                    d = yary[yi]; u = yary[yj]
                    # print(l,r,d,u)
                    for i in range(n):
                        x,y = a[i]
                        if l<=x<=r and d<=y<=u:
                            cnt += 1
                    if cnt >= k:
                        res = min(res, (r-l)*(u-d))
    print(res)
if __name__ == "__main__":
    main()
