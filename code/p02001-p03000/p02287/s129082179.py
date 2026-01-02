
class Heap:
    def __init__(self):
        self._nodes = []

    @classmethod
    def create(cls, li):
        heap = cls()
        heap._nodes = li
        return heap

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        if self.cur >= len(self._nodes):
            raise StopIteration
        self.cur += 1

        node = self._nodes[self.cur-1]
        if self.cur//2 - 1 >= 0:
            parent = self._nodes[self.cur//2 - 1]
        else:
            parent = None

        if self.cur*2 - 1 < len(self._nodes):
            left = self._nodes[self.cur*2 - 1]
        else:
            left = None

        if self.cur*2 < len(self._nodes):
            right = self._nodes[self.cur*2]
        else:
            right = None

        return (node, parent, left, right)


def run():
    _ = int(input())

    nodes = [int(i) for i in input().split()]
    heap = Heap.create(nodes)

    for (i, node) in enumerate(heap):
        n, p, nl, nr = node
        s = "node {}: key = {}, ".format(i+1, n)
        if p is not None:
            s += "parent key = {}, ".format(p)
        if nl is not None:
            s += "left key = {}, ".format(nl)
        if nr is not None:
            s += "right key = {}, ".format(nr)

        print(s)


if __name__ == '__main__':
    run()

