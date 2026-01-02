S = input()
Q = int(input())


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, initial_string=None):
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        self.should_reverse = False
        for s in initial_string:
            self.insert_last(s)

    def _insert_first(self, value=None):
        prev_next = self.first.next
        self.first.next = Node(value, self.first, prev_next)
        prev_next.prev = self.first.next

    def _insert_last(self, value=None):
        prev_prev = self.last.prev
        self.last.prev = Node(value, prev_prev, self.last)
        prev_prev.next = self.last.prev

    def insert_first(self, value=None):
        if self.should_reverse:
            self._insert_last(value)
        else:
            self._insert_first(value)

    def insert_last(self, value=None):
        if self.should_reverse:
            self._insert_first(value)
        else:
            self._insert_last(value)

    def set_reverse(self):
        self.should_reverse = not self.should_reverse

    def _print(self):
        node = self.first.next
        while node is not None:
            if node.value is not None:
                print(node, end="")
            node = node.next
        print("")

    def _print_reverse(self):
        node = self.last.prev
        while node is not None:
            if node.value is not None:
                print(node, end="")
            node = node.prev
        print("")

    def print_list(self):
        if self.should_reverse:
            self._print_reverse()
        else:
            self._print()


def formation():
    global S, Q

    linked_list = LinkedList(S)

    for _ in range(Q):
        t_str = input()

        if t_str[0] == '1':
            linked_list.set_reverse()
        else:
            split = t_str.split(' ')
            f = split[1]
            c = split[2]
            if f == '1':
                linked_list.insert_first(c)
            else:
                linked_list.insert_last(c)

    linked_list.print_list()


formation()
