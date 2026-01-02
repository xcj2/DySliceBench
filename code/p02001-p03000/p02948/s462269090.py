import heapq
from collections import defaultdict

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

n, m = map(int, input().split())
jobs = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    jobs[a].append(b)

res = 0
candidates = PriorytyQueue(arr=[],
                           target='max')
for d in range(1, m+1):
    if d in jobs.keys():
        for m in jobs[d]:
            candidates.push(m)
    if not(candidates.is_empty()):
        res += candidates.pop()
print(res)