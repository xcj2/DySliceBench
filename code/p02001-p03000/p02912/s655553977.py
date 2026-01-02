from heapq import heapify, heappush, heappop
class HeapQue(object):
    def __init__(self, iterable, max_heap=False):
        self.sign = -1 if max_heap else 1
        sequence = [number * self.sign for number in iterable]
        heapify(sequence)
        self.heapque = sequence

    def push(self, item):
        heappush(self.heapque, item * self.sign)

    def pop(self):
        return heappop(self.heapque) * self.sign

    def dump(self):
        return [heappop(self.heapque) * self.sign for _ in range(len(self.heapque))]

N, M = map(int, input().split())
heap = HeapQue(map(int, input().split()), max_heap=True)
for _ in range(M):
    heap.push(heap.pop() >> 1)
print(sum(heap.dump()))
