# stack.py
class Cell:
    def __init__(self, value, name):
        self.name = name
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def Enqueue(self, d,name):
        new = Cell(d,name)
        if self.front is None:
            self.front = new
            self.rear = self.front
        else:
            self.rear.next = new
            self.rear = new

    def Dequeue(self):
        if self.front is None:
            print('Queue Under Flow!')
            return
        else:
            res = self.front
            nex = self.front.next
            del self.front
            self.front = nex
            return res

    def is_empty(self):
        return self.front==None


n,q = map(int,input().split())
que = Queue()
for i in range(n):
    name,val = input().split()
    que.Enqueue(int(val),name)

t = 0
while not que.is_empty():
    a = que.Dequeue()
    if a.value>q:
        que.Enqueue(a.value-q,a.name)
        t+=q
    else:
        t+=a.value
        print(a.name,t)

