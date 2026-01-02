import sys

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertzero(self,value):
        new  = Node(value)
        p = self.head
        self.head = new
        new.next = p
        if p is None:
            self.tail = new
        else:
            p.prev = new

    def deletefirst(self):
        if self.head is None:
            return
        p = self.head
        if p.next is None:
            self.head = None
            self.tail = None
        else:
            q = p.next
            q.prev = None
            self.head = q

    def deletelast(self):
        if self.tail is None:
            return
        p = self.tail
        q = p.prev
        if q is None:
            self.head =None
            self.tail =None
        else:
            q.next = None
            self.tail = q

    def delete(self,value):
        p = self.head
        while p is not None:
            if p.value == value:
                if p.prev is None:
                    self.deletefirst()
                    return
                elif p.next is None:
                    self.deletelast()
                    return
                else:
                    p.next.prev = p.prev
                    p.prev.next = p.next
                    return
            else:
                p = p.next

    def show(self):
        p = self.head
        #print("L:",end="")  
        l = []
        c = 0
        while p is not None:
            l.append(p.value)
            p=p.next
        print(" ".join(l))

    def rshow(self):
        p = self.tail
        c = 0
        while p is not None:
            if c > 0:
                print(" ",end="")
            else:
                c +=1
            print(p.value,end="")
            p = p.prev
        print()

def main():

    list  = LinkList()
    num = int(input())

    for _ in range(num):
        #a = input().split()                                                                                                                   
        line = sys.stdin.readline()
        a = line.rstrip().split()
        if a[0][0] == "i":
            list.insertzero(a[1])
        elif len(a[0]) == 6:
            list.delete(a[1])
        elif len(a[0]) == 11:
            list.deletefirst()
        elif len(a[0]) == 10:
            list.deletelast()
        else:
            pass

    list.show()

if __name__ == '__main__':
    main()


