import sys

class MyNode:
    __slots__ = ['prev', 'next', 'val']

    def __init__(self, x):
        self.prev = None
        self.next = None
        self.val = x

class MyLinkList:
    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = None
        self.tail = None

    def generate(self):
        _node = self.head
        while True:
            if _node is None:
                break
            yield _node.val
            _node = _node.next

    def insert(self, x):
        node = MyNode(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def delete(self, x):
        if self.head.val == x:
            return self.deleteFirst()

        node = self.head.next
        while node.next is not None:
            if node.val == x:
                node.prev.next = node.next
                node.next.prev = node.prev
                # node.prev = None
                # node.next = None
                return True

            node = node.next

        if self.tail.val == x:
            return self.deleteLast()

        return False

    def deleteFirst(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return True

        self.head = self.head.next
        # self.head.prev.next = None
        self.head.prev = None

        return True

    def deleteLast(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return True

        self.tail = self.tail.prev
        # self.tail.next.prev = None
        self.tail.next = None

        return True

def _main():
    link_list = MyLinkList()

    n = int(input())
    
    for i in range(n):
        line = sys.stdin.readline()

        if line[0] == 'i':
            link_list.insert(line[7:-1])
        else:
            if line[6] == 'F':
                link_list.deleteFirst()
            elif line[6] == 'L':
                link_list.deleteLast()
            else:
                link_list.delete(line[7:-1])

    lst = [x for x in link_list.generate()]
    print(" ".join(lst))

if __name__ == '__main__':
    _main()
