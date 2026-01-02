import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val  = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def insert(self, val):
        node = Node(val)
        node.prev = self.sentinel
        node.next = self.sentinel.next
        self.sentinel.next.prev = node
        self.sentinel.next = node

    def delete(self, val):
        self.delete_node(self.search(val))

    def deleteFirst(self):
        self.delete_node(self.sentinel.next)

    def deleteLast(self):
        self.delete_node(self.sentinel.prev)

    def search(self, val):
        cursor = self.sentinel.next
        while cursor != self.sentinel and cursor.val != val:
            cursor = cursor.next
        return cursor

    def delete_node(self, node):
        if node == self.sentinel:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

n = int(input())
linked_list = DoublyLinkedList()
for index in range(n):
    command = input().rstrip()
    if command[0] == 'i':
        linked_list.insert(command[7:])
    elif command[6] == 'F':
        linked_list.deleteFirst()
    elif command[6] == 'L':
        linked_list.deleteLast()
    else:
        linked_list.delete(command[7:])

node = linked_list.sentinel.next
output = []
while node != linked_list.sentinel:
    output.append(node.val)
    node = node.next
print(" ".join(map(str, output)))
