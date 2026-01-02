import sys


class Node():
    def __init__(self,  key=None, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList():
    def __init__(self):
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head

    def insert(self, x):
        node = Node(key=x, prev=self.head, next=self.head.next)
        self.head.next.prev = node
        self.head.next = node

    def search(self, x):
        node = self.head.next
        while node is not self.head and node.key != x:
            node = node.next
        return node

    def delete_key(self, x):
        node = self.search(x)
        self._delete(node)

    def _delete(self, node):
        if node is self.head:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

    def deleteFirst(self):
        self._delete(self.head.next)

    def deleteLast(self):
        self._delete(self.head.prev)

    def getKeys(self):
        node = self.head.next
        keys = []
        while node is not self.head:
            keys.append(node.key)
            node = node.next
        return " ".join(keys)


L = DoublyLinkedList()
n = int(input())
for i in sys.stdin:
    if 'insert' in i:
        x = i[7:-1]
        L.insert(x)
    elif 'deleteFirst' in i:
        L.deleteFirst()
    elif 'deleteLast' in i:
        L.deleteLast()
    elif 'delete' in i:
        x = i[7:-1]
        L.delete_key(x)
    else:
        pass
print(L.getKeys())

