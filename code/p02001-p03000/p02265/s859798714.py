class Cell:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start = Cell(None)
        self.start.next = None
        self.start.prev = None

    def InsCell(self, x):
        new = Cell(x)
        if self.start.next != None:
            new.next = self.start.next
            self.start.next.prev = new
        else:
            self.start.prev = new
            new.next = self.start
        self.start.next = new
        new.prev = self.start

    def DelCell(self, x):
        tmp = self.start
        while tmp.x != x:
            if tmp.next == self.start:
                return
            tmp = tmp.next
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        tmp = None

    def DelFisrtCell(self):
        tmp = self.start.next
        if tmp.next == self.start:
            self.start.next = None
            self.start.prev = None
        else:
            self.start.next = tmp.next
            tmp.next.prev = self.start
        tmp = None

    def DelLastCell(self):
        tmp = self.start.prev
        if tmp.prev == self.start:
            self.start.next = None
            self.start.prev = None
        else:
            self.start.prev = tmp.prev
            tmp.prev.next = self.start
        tmp = None

    def PrintCell(self):
        ans = []
        tmp = self.start.next
        if tmp == None:
            print("")
        else:
            while tmp != self.start:
                ans.append(tmp.x)
                tmp = tmp.next
            print(" ".join(ans))

import sys
input = sys.stdin.readline

n = int(input())
l = DoublyLinkedList()

for _ in range(n):
    c = input().split()
    if c[0] == "insert":
        l.InsCell(c[1])
    elif c[0] == "delete":
        l.DelCell(c[1])
    elif c[0] == "deleteFirst":
        l.DelFisrtCell()
    elif c[0] == "deleteLast":
        l.DelLastCell()

l.PrintCell()

