class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList():
    def __init__(self):
        self.start = Node(val='START', prev=None, next=None)
        self.end = Node(val='END', prev=self.start, next=None)
        self.start.next = self.end

    def insert(self, x):
        new_node = Node(val=x, prev=self.end.prev, next=self.end)
        self.end.prev.next = new_node
        self.end.prev = new_node

    def dump(self):
        node_list = []
        crnode = self.start.next
        while crnode != self.end:
            node_list.append(crnode.val)
            crnode = crnode.next
        print(' '.join(list(map(str, node_list))))

    def extend(self, dll):
        self.end.prev.next = dll.start.next
        dll.start.next.prev = self.end.prev
        self.end = dll.end

n, q = list(map(int, input().split(' ')))
splice = [DoublyLinkedList() for i in range(n)]

for i in range(q):
    op, *val = list(map(int, input().split(' ')))
    if op == 0:
        splice[val[0]].insert(val[1])
    elif op == 1:
        splice[val[0]].dump()
    else:
        splice[val[1]].extend(splice[val[0]])
        splice[val[0]] = DoublyLinkedList()

