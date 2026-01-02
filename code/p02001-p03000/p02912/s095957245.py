from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)
      
N,M=map(int,input().split())
L = list(map(lambda s:int(s) * -1,input().split()))
#print(L)
pq = PriorityQueue(L)
import math
for _ in range(M):
  m = pq.pop()
  #print(m)
  pq.push(math.ceil(m / 2))
ANS=0
for _ in range(N):
  k = pq.pop()
  #print(k)
  ANS += k
print(ANS * -1)
  
