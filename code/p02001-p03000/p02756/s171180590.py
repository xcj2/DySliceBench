class Node:
    def __init__(self, char: str):
        self.before = None
        self.char = char
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.before = node
            self.head = node

    def add_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.before = self.tail
            self.tail.next = node
            self.tail = node

    def show(self, is_reversed: bool):
        ret = []
        node = self.tail if is_reversed else self.head
        while not node is None:
            c = ''.join(list(node.char)[::-1]) if is_reversed else node.char
            ret.append(c)
            node = node.before if is_reversed else node.next
        print(''.join(ret))

S = input()
Q = int(input())
ll = Linked_List()
ll.add_head(Node(S))
is_reversed = False

for _ in range(Q):
    query = input()
    if query[0] == '1':
        is_reversed = False if is_reversed else True
    else:
        t, f, c = query.split()
        if is_reversed:
            c = ''.join(list(c)[::-1])
        if f == '1':
            if is_reversed:
                ll.add_tail(Node(c))
            else:
                ll.add_head(Node(c))
        else:
            if is_reversed:
                ll.add_head(Node(c))
            else:
                ll.add_tail(Node(c))

ll.show(is_reversed)
