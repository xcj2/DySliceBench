import sys


class Node:
    def __init__(self, x):
        self.x = x

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next


class DoublelyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.set_next(self.nil)
        self.nil.set_prev(self.nil)

    def insert(self, x):
        new_elem = Node(x)
        new_elem.set_next(self.nil.next)
        new_elem.set_prev(self.nil)
        self.nil.next.set_prev(new_elem)
        self.nil.set_next(new_elem)

    def list_search(self, x):
        cur = self.nil.next
        while cur != self.nil and cur.x != x:
            cur = cur.next
        return cur

    def _delete(self, node):
        node.prev.set_next(node.next)
        node.next.set_prev(node.prev)

    def delete_first(self):
        self._delete(self.nil.next)

    def delete_last(self):
        self._delete(self.nil.prev)

    def delete(self, x):
        del_node = self.list_search(x)
        if del_node.x is not None:
            self._delete(del_node)


def main():
    d_linked_list = DoublelyLinkedList()
    for i in sys.stdin:
        if 'insert' in i:
            x = i[7:-1]
            d_linked_list.insert(x)
        elif 'deleteFirst' in i:
            d_linked_list.delete_first()
        elif 'deleteLast' in i:
            d_linked_list.delete_last()
        elif 'delete' in i:
            x = i[7:-1]
            d_linked_list.delete(x)
        else:
            pass

    results = []
    cur = d_linked_list.nil.next
    while cur.x is not None:
        results.append(cur.x)
        cur = cur.next

    print(*results)


if __name__ == "__main__":
    main()

