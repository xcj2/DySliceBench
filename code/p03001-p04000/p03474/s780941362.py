def examB():
    A, B = LI(); St = S()
    nums = list(map(str, range(10)))
    ans = "Yes"
    if St[A] == "-":
        for s in St[:A] + St[A + 1:]:
            if s not in nums:
                ans = "No"
                break
    else:
        ans = "No"
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
