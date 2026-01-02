class Node:
    __slots__ = ["val", "prev", "next"]

    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList():
    def __init__(self):
        self.end = Node(val="END", prev=None, next=None)
        self.cur = self.end

    def insert(self, x):
        new_node = Node(val=x, prev=self.cur.prev, next=self.cur)

        if self.cur.prev != None:
            self.cur.prev.next = new_node
        self.cur.prev = new_node
        self.cur = new_node

    def move(self, d):
        if d > 0:
            for i in range(d):
                if self.cur.next == None:
                    break
                self.cur = self.cur.next
        elif d < 0:
            for i in range(abs(d)):
                if self.cur.prev == None:
                    break
                self.cur = self.cur.prev
        else:
            raise
    
    def erase(self):
        if self.cur == self.end:
            return

        if self.cur.prev != None:
            self.cur.prev.next = self.cur.next

        self.cur.next.prev = self.cur.prev
        self.cur = self.cur.next

    def print_elements(self):
        node_list = []
        crnode = self.end
        while True:
            if crnode.prev == None:
                break
            node_list.append(crnode.prev.val)
            crnode = crnode.prev
        for i in range(len(node_list)-1, -1, -1):
            print(node_list[i])



def main():

    q = int(input())

    L = DoublyLinkedList()

    for _ in range(q):
    
        command, *list_num = input().split()
    
        if   command == "0":
            # insert(x)
            x = int(list_num[0])
            L.insert(x)
        elif command == "1":
            # move(d)
            d = int(list_num[0])
            L.move(d)
        elif command == "2":
            # erase()
            L.erase()
        else:
            raise


    L.print_elements()


if __name__ == "__main__":
    main()

