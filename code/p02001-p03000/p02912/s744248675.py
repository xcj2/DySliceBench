from heapq import heapify, heappush, heappop
class PriorityQueue():
    def __init__(self, queue=[]):
        self.queue = queue
        heapify(queue)
    def push(self, item):
        heappush(self.queue, item)
    def pop(self):
        return heappop(self.queue)
    def __str__(self):
        return self.queue
    def __len__(self):
        return len(self.queue)
    def __iter__(self):
        return iter(self.queue)
N, M = map(int, input().split())
def int_(num_str):
    return -int(num_str)


Alist = list(map(int_, input().split()))
pq = PriorityQueue(Alist)
for _ in range(M):
    max_val = pq.pop()
    pq.push(-1 * (-1*(max_val))/2)
ans = sum([int(-1 * item) for item in pq])
print(ans)