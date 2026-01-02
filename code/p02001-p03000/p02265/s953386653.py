import sys


class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.nil = Node(None, None, None)
        self.nil.prev = self.nil
        self.nil.next = self.nil


def insert(double_lst, key):
    node = Node(key, double_lst.nil, double_lst.nil.next)
    double_lst.nil.next.prev = node
    double_lst.nil.next = node


def search(double_lst, key):
    cur = double_lst.nil.next

    while cur != double_lst.nil and cur.key != key:
        cur = cur.next

    return cur


def delete_node(double_lst, node):
    if node == double_lst.nil:
            return

    node.prev.next = node.next
    node.next.prev = node.prev


def delete_first(double_lst):
    delete_node(double_lst, double_lst.nil.next)


def delete_last(double_lst):
    delete_node(double_lst, double_lst.nil.prev)


def delete_key(double_lst, key):
    node = search(double_lst, key)
    delete_node(double_lst, node)


def main():
    n = int(input())
    ll = LinkedList()

    for i in range(n):
        order = sys.stdin.readline().split()

        if order[0] == "insert":
            insert(ll, int(order[1]))
        elif order[0] == "delete":
            delete_key(ll, int(order[1]))
        elif order[0] == "deleteFirst":
            delete_first(ll)
        else:
            delete_last(ll)

    cur = ll.nil
    while cur.next != ll.nil:
        cur = cur.next
        if cur.next == ll.nil:
            print(cur.key)
        else:
            print(cur.key, end=" ")


if __name__ == '__main__':
    main()

