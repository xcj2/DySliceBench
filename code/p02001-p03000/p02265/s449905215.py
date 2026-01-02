# coding: utf-8

from collections import deque

class DoublyLinkedList(object):

    def __init__(self):
        self.queue = deque()
    
    def __call__(self, orders):
        for order in orders:
            order = order.split()

            if order[0] == 'insert':
                self.insert(order[1])
            elif order[0] == 'delete':
                self.delete(order[1])
            elif order[0] == 'deleteFirst':
                self.delete_first()
            elif order[0] == 'deleteLast':
                self.delete_last()
        print(' '.join(self.queue))

    def insert(self, x):
        self.queue.appendleft(x)
    
    def delete(self, x):
        try:
            self.queue.remove(x)
        except:
            pass
    
    def delete_last(self):
        self.queue.pop()
    
    def delete_first(self):
        self.queue.popleft()
    

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(input())
    doubly_linked_list(orders)
