
class Node:

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class HashMap:

    def __init__(self, _size=None):
        if _size is not None:
            assert _size > 0
        self._size = _size
        self._setsize(2)
        self.count = 0
        self.nodes = [None] * self.size

    def __getitem__(self, key):
        node = self.nodes[self.hash(key)]
        while node is not None and node.key != key:
            node = node.next
        if node is not None:
            return node.value
        else:
            raise IndexError('key {} not found in map'.format(key))

    def __setitem__(self, key, value):
        i = self.hash(key)
        node = self.nodes[i]
        if node is None:
            self.nodes[i] = Node(key, value)
            self.count += 1
        else:
            while node.next is not None and node.key != key:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)
                self.count += 1

        if self.count == self.size:
            self._resize(self.k + 1)

    def __delitem__(self, key):
        i = self.hash(key)
        node = self.nodes[i]
        if node is None:
            raise IndexError('key {} not found in map'.format(key))
        elif node.key == key:
            self.nodes[i] = node.next
            self.count -= 1
            return

        while node.next is not None and node.next.key != key:
            node = node.next
        if node.next is not None:
            node.next = node.next.next
            self.count -= 1
        else:
            raise IndexError('key {} not found in map'.format(key))

    def items(self):
        for node in self.nodes:
            n = node
            while n is not None:
                yield n.key, n.value
                n = n.next

    def __len__(self):
        return self.count

    def hash(self, key):
        return hash(key) % self.size

    def _setsize(self, k):
        if self._size is None:
            self.k = k
            self.size = 2 ** k - 1
        else:
            self.k = 0
            self.size = self._size

    def _resize(self, k):
        if self._size is not None:
            return
        nodes = self.nodes

        self._setsize(k)
        self.nodes = [None] * self.size
        self.count = 0
        for node in nodes:
            n = node
            while n is not None:
                self.__setitem__(n.key, n.value)
                n = n.next


def run():
    q = int(input())
    m = HashMap()

    for _ in range(q):
        command, *args = input().split()
        if command == '0':
            key = args[0]
            value = int(args[1])
            m[key] = value
        elif command == '1':
            key = args[0]
            try:
                print(m[key])
            except IndexError:
                print(0)
        elif command == '2':
            key = args[0]
            try:
                del m[key]
            except IndexError:
                pass
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

