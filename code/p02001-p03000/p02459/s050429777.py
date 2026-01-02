
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class HashMap:

    def __init__(self):
        self.k = 2
        self.size = self.k * self.k - 1
        self.count = 0
        self.nodes = [None] * self.size

    def __getitem__(self, key):
        node = self.nodes[self.hash(key)]
        while node is not None and node.key != key:
            node = node.next
        if node is not None:
            return node.value
        else:
            return None

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

    def __len__(self):
        return self.count

    def hash(self, key):
        return hash(key) % self.size

    def _resize(self, k):
        nodes = self.nodes

        self.size = 2 ** k - 1
        self.k = k
        self.nodes = [None] * self.size
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
            print(m[key])
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

