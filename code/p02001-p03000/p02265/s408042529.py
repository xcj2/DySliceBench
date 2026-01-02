class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.first = Node()
        self.first.prev = self.first
        self.first.next = self.first

    def insert(self, key):
        x = Node(key)
        x.next = self.first.next
        self.first.next.prev = x
        self.first.next = x
        x.prev = self.first

    def search(self, key):
        cur = self.first.next
        while cur != self.first and cur.key != key:
            cur = cur.next

        return cur

    def delete(self, key):
        self.delete_node(self.search(key))

    def delete_node(self, node):
        if node == self.first:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def delete_first(self):
        self.delete_node(self.first.next)

    def delete_last(self):
        self.delete_node(self.first.prev)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline # faster input

    linklist = DoublyLinkedList()

    n = int(input())

    for _ in range(n):
        inputs = input().rstrip()
        if inputs[0] == 'i':
            linklist.insert(inputs[7:])
        elif inputs[6] == 'F':
            linklist.delete_first()
        elif inputs[6] == 'L':
            linklist.delete_last()
        else:
            linklist.delete(inputs[7:])

    result = []
    cur = linklist.first.next
    while cur != linklist.first:
        result.append(cur.key)
        cur = cur.next

    print(' '.join(result))

