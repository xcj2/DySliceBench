
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, v):
        node = Node(v)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dump(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def splice(self, li):
        if self.head is None:
            self.head = li.head
            self.tail = li.tail
        else:
            self.tail.next = li.head
            self.tail = li.tail
        li.clear()

    def clear(self):
        self.head = None
        self.tail = None


def run():
    n, q = [int(x) for x in input().split()]
    ls = [List() for _ in range(n)]

    for _ in range(q):
        com = [int(x) for x in input().split()]
        c = com[0]
        if c == 0:
            t, v = com[1:]
            ls[t].insert(v)
        elif c == 1:
            t = com[1]
            values = []
            for v in ls[t].dump():
                values.append(str(v))
            print(" ".join(values))
        elif c == 2:
            s, t = com[1:]
            ls[t].splice(ls[s])
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

