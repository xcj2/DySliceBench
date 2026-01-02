from sys import stdin

class Node:
    def __init__(self, value: int):
        self.value = value
        self.previous_node = None
        self.next_node = None


class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
    
    def delete_node(self, node: Node):
        if node.next_node != None:
            node.next_node.previous_node = node.previous_node
        if node.previous_node != None:
            node.previous_node.next_node = node.next_node
        if node == self.first:
            self.first = node.next_node
        if node == self.last:
            self.last = node.previous_node

    def value_generator(self):
        node = self.first
        while node != None:
            yield node.value
            node = node.next_node

    def insert(self, x: int):
        node = Node(x)
        node.next_node = self.first
        if self.first != None:
            self.first.previous_node = node
        self.first = node
        if self.last == None:
            self.last = node

    def delete(self, x: int):
        target_node = self.first
        while target_node != None and target_node.value != x:
            target_node = target_node.next_node
        if target_node != None:
            self.delete_node(target_node)


def main():
    linked_list = LinkedList()
    insert,delete,delete_node = linked_list.insert,linked_list.delete,linked_list.delete_node
    _ = int(stdin.readline())
    for line in (line.split() for line in stdin.readlines()):
        command = line[0]
        if command == "insert":
            insert(int(line[1]))
        elif command == "delete":
            delete(int(line[1]))
        elif command == "deleteFirst":
            delete_node(linked_list.first)
        elif command == "deleteLast":
            delete_node(linked_list.last)
    print(*linked_list.value_generator())


main()
