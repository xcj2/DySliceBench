import heapq

class PriorytyQueue(object):

    def __init__(self, arr, target='min'):
        self.arr = arr
        self.target = target
        self._heapify()
    
    def _heapify(self):
        if self.target == 'max':
            self.arr = list(map(lambda x:x*(-1), self.arr))
        heapq.heapify(self.arr)
    
    def push(self, x):
        if self.target == 'max':
            x *= -1
        heapq.heappush(self.arr, x)

    def pop(self):
        res = heapq.heappop(self.arr)
        if self.target == 'max':
            return res*(-1)
        else:
            return res
    
    def get_arr(self):
        if self.target == 'max':
            return list(map(lambda x:x*(-1), self.arr))
        else:
            return self.arr
    
    def is_empty(self):
        return len(self.arr) == 0

from collections import defaultdict

N, M = map(int, input().split())
jobs = defaultdict(list)
for i in range(N):
    a, b = map(int, input().split())
    if a > M:
        continue
    jobs[a].append(b)

if __name__ == "__main__":

    ans = 0
    pq = PriorytyQueue([], target='max')
    for d in range(1, M+1):
        if d in jobs.keys():
            moneys = jobs[d]
            for money in moneys:
                pq.push(money)
        if not(pq.is_empty()):
            ans += pq.pop()
    print(ans)