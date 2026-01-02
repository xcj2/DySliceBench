import sys

def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.current_node = Node(None, None, None)
        self.front_node = self.current_node
        self.end_node = self.current_node

    def insert(self, value):
        current_node = self.current_node
        prev_node = current_node.prev_node
        if prev_node == None:
            newNode = Node(value, None, current_node)
            current_node.prev_node = newNode
            self.current_node = newNode
            self.front_node = newNode
        else:
            newNode = Node(value, prev_node, current_node)
            prev_node.next_node = newNode
            current_node.prev_node = newNode
            self.current_node = newNode

    def remove(self):
        prev_node = self.current_node.prev_node
        next_node = self.current_node.next_node
        if prev_node == None:
            next_node.prev_node = None
            self.front_node = next_node
            self.current_node = next_node
        else:
            next_node.prev_node = prev_node
            prev_node.next_node = next_node
            self.current_node = next_node

    def move(self, diff):
        if diff > 0:
            for _ in range(diff):
                self.current_node = self.current_node.next_node
        elif diff < 0:
            for _ in range(-diff):
                self.current_node = self.current_node.prev_node

    def print(self):
        node = self.front_node
        while node != self.end_node:
            print(node.value)
            node = node.next_node

input()
a = LinkedList()
while True:
    line = input()
    if not line:
        break
    if line[0] == '0':
        a.insert(int(line[2:]))
    elif line[0] == '1':
        a.move(int(line[2:]))
    else:
        a.remove()

a.print()

