class Elm:
    def __init__(self, value, ptr_prev, ptr_next):
        self.value = value
        self.prev = ptr_prev
        self.next = ptr_next
#        self.prev = None
#        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nil = Elm("NIL", None, None)
        self.nil.prev = self.nil # tail
        self.nil.next = self.nil # head
        
def insertVal(self, value):
    new_elm = Elm(value, self.nil, self.nil.next)
    new_elm.next.prev = new_elm
    self.nil.next = new_elm

def deleteVal(self, value):
    ptr = self.nil.next
    while ptr.value != value:
        if ptr.next == self.nil:
            return
        ptr = ptr.next
#    if ptr.value == value:
#        ptr.prev.next = ptr.next
#        ptr.next.prev = ptr.prev
    ptr.prev.next = ptr.next
    ptr.next.prev = ptr.prev

def deleteFirst(self):
    self.nil.next = self.nil.next.next
    self.nil.next.prev = self.nil

def deleteLast(self):
    self.nil.prev = self.nil.prev.prev
    self.nil.prev.next = self.nil

def show(self):
    ptr = self.nil.next
    while ptr!=self.nil:
#    while True:
        if ptr.next == self.nil:
            print(ptr.value)
            return
        print(ptr.value, end=" ")
        ptr = ptr.next
        
def selectOps(dll, command):
#    ops = command[0]
    if command[0] == "insert":
        insertVal(dll, command[1])
    elif command[0] == "delete":
        deleteVal(dll, command[1])        
    elif command[0] == "deleteFirst":
        deleteFirst(dll)
#    elif ops == "deleteLast":
    else:
        deleteLast(dll)
#    else:
#        print("Error: invalid oparation")

    
import sys

n = int(input())
l = DoublyLinkedList()

for i in range(n):
    command = sys.stdin.readline().split()
#    command = input().split(" ")
#    selectOps(dll=l, command=command)
    if command[0] == "insert":
        insertVal(l, command[1])
    elif command[0] == "delete":
        deleteVal(l, command[1])        
    elif command[0] == "deleteFirst":
        deleteFirst(l)
#    elif ops == "deleteLast":
    else:
        deleteLast(l)
show(l)

