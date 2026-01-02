class Node:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.prev = self.nil
        self.nil.next = self.nil
    
    def insert(self,key):
        new = Node(key)
        new.next = self.nil.next
        self.nil.next.prev = new
        self.nil.next = new
        new.prev = self.nil
    
    def listSearch(self,key):
        cur = self.nil.next
        while cur != self.nil and cur.key != key:
            cur = cur.next
        return cur
    
    def deleteNode(self, t):
        if t == self.nil:
            return
        t.prev.next = t.next
        t.next.prev = t.prev

    def deleteFirst(self):
        self.deleteNode(self.nil.next)

    def deleteLast(self):
        self.deleteNode(self.nil.prev)

    def deleteKey(self, key):
        self.deleteNode(self.listSearch(key))
if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    n = int(input())
    d = DoublyLinkedList()
    for _ in range(n):
        c = input().rstrip()
        if c[0] == "i":
            d.insert(c[7:])
        elif c[6] == "F":
            d.deleteFirst()
        elif c[6] =="L":
            d.deleteLast()
        else:
            d.deleteKey(c[7:])
    ans = []
    cur = d.nil.next
    while cur != d.nil:
        ans.append(cur.key)
        cur = cur.next
    print(" ".join(ans))
