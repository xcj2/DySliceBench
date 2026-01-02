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
        return heappop(self.heapque) * self.sign

    def dump(self):
        return [heappop(self.heapque) * self.sign for _ in range(len(self.heapque))]

N, M = map(int, input().split())
q = HeapQue(map(int, input().split()))
pairs = sorted((tuple(map(int, input().split())) for _ in range(M)), key=lambda t: t[1], reverse=True)
for b, c in pairs:
    for _ in range(b):
        x = q.pop()
        if x < c:
            q.push(c)
        else:
            q.push(x)
            print(sum(q.dump()))
            quit()
print(sum(q.dump()))