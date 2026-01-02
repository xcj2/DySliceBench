from heapq import heapify, heappush, heappop
class HeapQue(object):
    def __init__(self, iterable, max_heap=False):
        self.sign = -1 if max_heap else 1
        sequence = [self.sign * number for number in iterable]
        heapify(sequence)
        self.heapque = sequence

    def push(self, item):
        heappush(self.heapque, item * self.sign)

    def pop(self):
        try:
            return heappop(self.heapque) * self.sign
        except:
            return 0

N, M = map(int, input().split())
jobs = sorted((tuple(map(int, input().split())) for _ in range(N)), key=lambda t: t[0], reverse=True)
q = HeapQue([], max_heap=True)
total = 0
for i in range(1, M + 1):
    while jobs and jobs[-1][0] == i:
        q.push(jobs.pop()[1])
    total += q.pop()
print(total)