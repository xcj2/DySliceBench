from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def calc(p,x):
    return p*(100+x)//100


while True:
    x,y,s = inpl()
    if x == 0 and y == 0 and s == 0:
        break
    else:
        ans = 0
        for a in range(1,s):
            ap = calc(a,x)
            for b in range(1,s):
                bp = calc(b,x)
                if ap + bp != s:
                    continue
                else:
                    tmp = calc(a,y) + calc(b,y)
                    ans = max(ans,tmp)
        print(ans)

