class Node:
    def __init__(self, v):
        self.v = v
        self.p = None
        self.n = None

class LinkedList:
    def __init__(self, v):
        self.head = Node(v)
        self.tail = self.head
        self.d = 1

    def reverse(self):
        self.d = self.d * -1

    def insertTail(self, v):
        node = Node(v)
        if self.d == 1:
            self.tail.n = node
            node.p = self.tail
            self.tail = node
        else:
            self.head.p = node
            node.n = self.head
            self.head = node

    def insertHead(self, v):
        self.reverse()
        self.insertTail(v)
        self.reverse()

    def toString(self):
        res = ""
        if self.d == 1:
            pos = self.head
            while pos != None:
                res = res + pos.v
                pos = pos.n
        else:
            pos = self.tail
            while pos != None:
                res = res + pos.v
                pos = pos.p
        return res

S = input()
Q = int(input())

l = LinkedList(S[0])
for i in range(1,len(S)):
    l.insertTail(S[i])

for _ in range(Q):
    query = input()
    if query[0] == "1":
        l.reverse()
    else:
        T,F,C = query.split()
        if F=="1":
            l.insertHead(C)
        else:
            l.insertTail(C)
print(l.toString())
