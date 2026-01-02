def examA():
    a, b, c, d = LI()
    ans = "No"
    if abs(a-c)<=d:
        ans = "Yes"
    if abs(a-b)<=d and abs(b-c)<=d:
        ans = "Yes"
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

examA()