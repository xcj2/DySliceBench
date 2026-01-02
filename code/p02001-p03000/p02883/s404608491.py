import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

import heapq
class Reverse:
    def __init__(self, val):
        self.val = val
        
    def __lt__(self, other):
        return self.val > other.val
        
    def __repr__(self):
        return repr(self.val)
    
class Heapq:
    def __init__(self, arr, desc = False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        if self.desc: return heapq.heappop(self.hq).val
        else: return heapq.heappop(self.hq)
 
    def push(self, a):
        if self.desc: heapq.heappush(self.hq, Reverse(a))
        else: heapq.heappush(self.hq, a)
 
    def top(self):
        if self.desc: return self.hq[0].val
        else: return self.hq[0]

N,K = II()
A = III()
F = III()

A.sort()
F.sort(reverse=True)

ng = -1
ok = 10**12

while (abs(ok-ng) > 1):
    mid = (ok+ng)//2
    num = 0
    for i in range(N):
        a = math.floor(mid/F[i])
        if A[i]>a:
            num += A[i]-a
    if num<=K:
        ok = mid
    else:
        ng = mid

print(ok)