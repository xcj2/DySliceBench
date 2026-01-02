import sys

class Node: 
    def __init__(self, x, y = None, z = None): 
        self.data = x 
        self.prev = y 
        self.next = z 

class LinkedList: 
    def __init__(self): 
        self.top = Node(None) 
        self.top.next = self.top
        self.top.prev = self.top
    def insert(self, x):
        a = Node(x)
        self.top.next.prev = a
        a.next = self.top.next
        self.top.next = a
        a.prev = self.top
    def search(self, x):
        nil = self.top
        node = nil.next
        while node != nil and node.data != x:
            node = node.next
        return node
    def _delete(self, node):
        if node != self.top:
            np = node.prev
            nn = node.next
            np.next = nn
            nn.prev = np
    def delete_data(self, x):
        node = self.search(x)
        self._delete(node)
    def deleteFirst(self):
        nil = self.top
        self._delete(nil.next)
    def deleteLast(self):
        nil = self.top
        self._delete(nil.prev)
    def output(self):
        nil = self.top
        node = nil.next
        datalist = []
        while node != nil:
            datalist.append(node.data)
            node = node.next
        print(" ".join(datalist))

n = int(input()) 
L = LinkedList()
nil = L.top
for cmd in sys.stdin:
    cmd = cmd.strip("\n")
    if "insert" in cmd:
        L.insert(cmd[7:])
    elif "deleteFirst" in cmd:
        L.deleteFirst()
    elif "deleteLast" in cmd: 
        L.deleteLast()
    elif "delete " in cmd:
        L.delete_data(cmd[7:])

L.output()
