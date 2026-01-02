import sys


class DoubleLinkedList:
    class Node:
        def __init__(self, value=None, prev=None, _next=None):
            self.value = value
            self.prev = prev
            self.next = _next

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, v):
        head = self.head
        node = self.Node(v, head, head.next)
        head.next.prev = node
        head.next = node

    def delete(self, node):
        if node in (self.head, self.tail):
            return
        else:
            node.prev.next, node.next.prev = node.next, node.prev

    def delete_first(self):
        self.delete(self.head.next)

    def delete_last(self):
        self.delete(self.tail.prev)

    def delete_first_value(self, v):
        node = self.find(v, self.head)
        if node is not None:
            self.delete(node)

    def find(self, v, cur=None):
        if cur is None:
            cur = self.head

        while cur != self.tail:
            cur = cur.next
            if cur.value == v:
                return cur

        return None

    def __str__(self):
        cur = self.head.next
        vs = ''
        while cur != self.tail:
            vs += cur.value
            cur = cur.next
            if cur != self.tail:
                vs += ' '

        return vs


def run():
    steps = int(input())  # flake8: noqa
    dl = DoubleLinkedList()

    for command in sys.stdin:
        if command.startswith('insert'):
            dl.insert(command[7:-1])
        elif command.startswith('deleteFirst'):
            dl.delete_first()
        elif command.startswith('deleteLast'):
            dl.delete_last()
        elif command.startswith('delete'):
            dl.delete_first_value(command[7:-1])
        else:
            raise ValueError()

    print(dl)


if __name__ == '__main__':
    run()

