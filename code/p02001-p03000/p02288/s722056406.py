class Heap:
    def __init__(self, nodes):
        self._nodes = nodes
        self.size = len(nodes)

    def max_heapify(self):
        def _max_heapify(i):
            left = (i+1) * 2 - 1
            right = (i+1) * 2
            if left < self.size and self._nodes[left] > self._nodes[i]:
                largest = left
            else:
                largest = i

            if right < self.size and self._nodes[right] > self._nodes[largest]:
                largest = right

            if largest > i:
                self._nodes[i], self._nodes[largest] = \
                        self._nodes[largest], self._nodes[i]
                _max_heapify(largest)

        for i in reversed(range(self.size//2)):
            _max_heapify(i)

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        if self.cur >= self.size:
            raise StopIteration
        node = self._nodes[self.cur]
        self.cur += 1

        return node

    @classmethod
    def create(cls, li):
        heap = cls(li[:])
        heap.max_heapify()
        return heap


def run():
    _ = int(input())

    nodes = [int(i) for i in input().split()]
    heap = Heap.create(nodes)

    s = ''
    for node in heap:
        s += ' {}'.format(node)

    print(s)


if __name__ == '__main__':
    run()

