# -*- coding:utf-8 -*-
import sys


class Cell(object):
    __slots__ = ["value", "pre", "next"]

    def __init__(self, value=None, pre=None, _next=None):
        if pre is None and _next is None:
            self.value = None
            self.pre = self
            self.next = self
        else:
            self.value = value
            self.pre = pre
            self.next = _next


class MyList(object):
    def __init__(self):
        self._nil = Cell()

    def insert(self, value):
        self._nil.next = Cell(value, self._nil, self._nil.next)
        self._nil.next.next.pre = self._nil.next

    def delete(self, value):
        self._delete_to(self._search(value))

    def delete_first(self):
        self._delete_to(self._nil.next)

    def delete_last(self):
        self._delete_to(self._nil.pre)

    def toList(self):
        gen = self._val_generator()
        return [val for val in gen()]

    def _val_generator(self):
        def gen():
            current = self._nil.next
            while current is not self._nil:
                yield current.value
                current = current.next
        return gen

    def _delete_to(self, cell):
        if cell is not self._nil:
            cell.next.pre = cell.pre
            cell.pre.next = cell.next

    def _search(self, value):
        current = self._nil.next
        while current is not self._nil and current.value != value:
            current = current.next
        return current


def doubly_inked_list(commands):
    lst = MyList()
    for command in commands:
        if command[0] == "insert":
            lst.insert(command[1])
        elif command[0] == "delete":
            lst.delete(command[1])
        elif command[0] == "deleteFirst":
            lst.delete_first()
        elif command[0] == "deleteLast":
            lst.delete_last()
        else:
            raise ValueError
    return lst.toList()


if __name__ == "__main__":
    commands = [val.split() for val in sys.stdin.read().splitlines()]
    pop = commands.pop(0)
    print(" ".join(doubly_inked_list(commands)))