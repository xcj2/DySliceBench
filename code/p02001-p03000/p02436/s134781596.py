
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        if value is None:
            raise ValueError('enqueue None')
        node = Node(value)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = node

    def front(self):
        if self.first is None:
            return None
        return self.first.value

    def dequeue(self):
        if self.first is None:
            return None
        value = self.first.value
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        return value


def run():
    n, nq = [int(x) for x in input().split()]
    qs = [Queue() for _ in range(n)]

    for _ in range(nq):
        line = input()
        if line.startswith('0'):
            command, target, value = [int(x) for x in line.split()]
            qs[target].enqueue(value)
        elif line.startswith('1'):
            command, target = [int(x) for x in line.split()]
            value = qs[target].front()
            if value is not None:
                print(value)
        elif line.startswith('2'):
            command, target = [int(x) for x in line.split()]
            qs[target].dequeue()
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

