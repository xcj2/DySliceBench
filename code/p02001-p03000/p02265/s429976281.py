from collections import deque
import sys
input = sys.stdin.readline


class DoublyLinkedList:
    def __init__(self):
        self.doubly_linked_list = deque()

    def insert(self, item):
        self.doubly_linked_list.appendleft(item)

    def delete(self, item):
        if item in self.doubly_linked_list:
            self.doubly_linked_list.remove(item)

    def delete_first(self):
        if self.doubly_linked_list:
            self.doubly_linked_list.popleft()

    def delete_last(self):
        if self.doubly_linked_list:
            self.doubly_linked_list.pop()


doubly_linked_list = DoublyLinkedList()


def command_controller(command, n):
    global doubly_linked_list

    if command == 'insert':
        doubly_linked_list.insert(n)
    if command == 'deleteFirst':
        doubly_linked_list.delete_first()
    if command == 'deleteLast':
        doubly_linked_list.delete_last()
    if command == 'delete':
        doubly_linked_list.delete(n)


n = int(input())
for _ in range(n):
    command = list(input().split())
    command_controller(command[0], command[-1])
print(*doubly_linked_list.doubly_linked_list)

