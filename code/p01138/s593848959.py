
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def calc(t):
    h,m,s = map(int,t.split(':'))
    return (h*60+m)*60+s


while True:
    n = inp()
    if n == 0:
        break
    else:
        imos = [0]*(60*60*24+5)
        for _ in range(n):
            ts,tt = input().split()
            ts = calc(ts)
            tt = calc(tt)
            imos[ts] += 1
            imos[tt] -= 1

        tmp = 0
        for i in range(60*60*24+5):
            tmp += imos[i]
            imos[i] = tmp
        print(max(imos))

