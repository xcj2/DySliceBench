from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

class HeapQueue:
    def __init__(self,flag): # flag == True 最小値pop / False 最大値pop
        if flag: self.inv = 1
        else: self.inv = -1
        self.hq = []
        heapq.heapify(self.hq)

    def push(self,x):
        heapq.heappush(self.hq,self.inv*x)

    def pop(self):
        return self.inv * heapq.heappop(self.hq)

    def is_empty(self):
        if self.hq:
            return False
        else:
            return True


N,M = inpl()
que = HeapQueue(False)
ABs = [inpl() for _ in range(N)]
ABs.sort()
ABs.append([M+5,0])

itr = 0
ans = 0
for d in range(1,M+1):
    while True:
        A,B = ABs[itr]
        if A > d:
            break
        else:
            que.push(B)
            itr += 1
    if not que.is_empty():
        ans += que.pop()

print(ans)
