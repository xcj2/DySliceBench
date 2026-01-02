import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
#入力
#解答
#出力
#Priority-queue
class PriorityQueue:

    def __init__(self,heap):
        self.heap = heap
        heapify(self.heap)
    
    def push(self,item):
        heappush(self.heap,item)
    
    def pop(self):
        return heappop(self.heap)
    
    def pushpop(self,item):
        return heappushpop(self.heap,item)
    
    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)

n,m = map(int,input().split())
A = sorted(list(map(int,input().split())))
heap = []
q = PriorityQueue(heap)
for i in range(n):
    q.push(-A[i])

for i in range(m):
    a = q.pop()
    a *= -1
    a //=2
    a *= -1
    q.push(a)
print(-1*sum(heap))