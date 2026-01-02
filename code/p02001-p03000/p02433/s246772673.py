class Node():
    def __init__(self, prv = None, nxt = None, val = None):
        self.prv = prv
        self.nxt = nxt
        self.val = val

class DoublyLinkedList():
    def __init__(self):
        self.head = Node(prv=None, nxt=None, val="H")
        self.cur_node = self.head
        self.tail = Node(prv=None, nxt=None, val="E")
        
    def insert(self, x):
        if self.cur_node == self.head:
            new_node = Node(prv=None, nxt=None, val=x)

            new_node.prv = self.head
            new_node.nxt = self.tail

            self.head.nxt = new_node
            self.tail.prv = new_node

            self.cur_node = new_node

        elif self.cur_node == self.tail:
            new_node = Node(prv=None, nxt=None, val=x)

            self.tail.prv.nxt = new_node

            new_node.prv = self.tail.prv
            new_node.nxt = self.tail
            
            self.tail.prv = new_node
            self.cur_node = new_node
            
        else:
            new_node = Node(prv=None, nxt=None, val=x)

            if self.cur_node.prv is self.head:
                new_node.prv = self.head
                self.head.nxt = new_node
            else:
                new_node.prv = self.cur_node.prv
                self.cur_node.prv.nxt = new_node
               
            if self.cur_node is not self.tail:
                new_node.nxt = self.cur_node
                self.cur_node.prv = new_node

            self.cur_node = new_node

    def move(self, d):
        if d > 0:
            for _ in range(d):
                if self.cur_node.nxt is not None:
                    self.cur_node = self.cur_node.nxt
        elif d < 0:
            for _ in range(-d):
                self.cur_node = self.cur_node.prv
            
    def erase(self):
        prv = self.cur_node.prv
        nxt = self.cur_node.nxt

        if prv is self.head:
            self.head.nxt = nxt
        else:
            prv.nxt = nxt

        nxt.prv = prv
        self.cur_node = nxt

    def dump(self):
        cur = self.head.nxt

        while True:
            if cur is self.tail :
                break
            
            print(cur.val)
            cur = cur.nxt

def main():
    dll = DoublyLinkedList()
    q = int(input())

    for _ in range(q):
        com, *para = map(int, input().split())

        if   com == 0:
            dll.insert(para[0])

        elif com == 1:
            dll.move(para[0])

        elif com == 2:
            dll.erase()
    dll.dump()
    
main()
