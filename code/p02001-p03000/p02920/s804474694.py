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

N = I()
S = III()

S.sort()
a = [Heapq([],True) for _ in range(N+1)]
count = [0]*(N+1)

s = S.pop()
a[N].push(s)
count[N] = 1

while S:
    flag = False
    temp = S.pop()
    for i in range(1,N+1)[::-1]:
        if count[i]:
            if temp<a[i].top():
                x = a[i].pop()
                count[i] -= 1
                a[i-1].push(x)
                a[i-1].push(temp)
                count[i-1] += 2
                flag = True
                break
    if not flag:
        print('No')
        exit()

print('Yes')