class heap():
    def __init__(self, maxcom=True):
        if maxcom:
            self.compare = lambda x, y: x > y
        else:
            self.compare = lambda x, y: x < y

    def heappush(self, x, heap):
        heap.append(x)
        length = len(heap)
        pointer = length
        while True:
            if pointer == 1:
                break
            if self.compare(heap[pointer - 1], heap[(pointer >> 1) - 1]):
                heap[pointer - 1], heap[(pointer >> 1) - 1] = heap[(pointer >> 1) - 1], heap[pointer - 1]
                pointer = pointer >> 1
            else:
                break

    def heapreplace(self, function, heap):
        heap[0] = function(heap[0])
        pointer = 1
        length = len(heap)
        while True:
            if (pointer << 1) > length:
                break
            elif (pointer << 1) + 1 > length :
                if self.compare(heap[(pointer << 1) - 1], heap[pointer - 1]):
                    heap[(pointer << 1) - 1], heap[pointer - 1] = heap[pointer - 1], heap[(pointer << 1) - 1]
                else:
                    break
            else:
                if self.compare(heap[(pointer << 1) - 1], heap[pointer << 1]):
                    next_pointer = pointer << 1
                else:
                    next_pointer = (pointer << 1) + 1
                if self.compare(heap[next_pointer - 1], heap[pointer - 1]):
                    heap[next_pointer - 1], heap[pointer - 1] = heap[pointer - 1], heap[next_pointer - 1]
                    pointer=next_pointer
                else:
                    break


n, m = map(int, input().split())
a = map(int, input().split())
heapq = []
heapc=heap(True)
for i in a:
    heapc.heappush(i,heapq)
for _ in range(m):
    heapc.heapreplace(lambda x:x>>1,heapq)
print(sum(heapq))