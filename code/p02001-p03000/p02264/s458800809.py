class MyQueue:
    def __init__(self, max):
        self.MAX = max
        self.queue = [0] * self.MAX
        self.head = self.tail = 0
        
    def is_empty(self):
        return self.head == self.tail
        
    def is_full(self):
        return self.head == self.tail+1%self.MAX
        
    def enqueue(self, elm):
        if self.is_full():
            raise ValueError()
        
        self.queue[self.tail] = elm
        
        if self.tail+1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError()
        
        elm = self.queue[self.head]
        
        if self.head+1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        
        return elm

N, qt = [int(n) for n in input().split()]
queue = MyQueue(N+10)

for n in range(N):
    name, time = input().split()
    queue.enqueue([name, int(time)])

time = 0
while not queue.is_empty():
    prc = queue.dequeue()
    if prc[1] > qt:
        prc[1] -= qt
        queue.enqueue(prc)
        time += qt
    else:
        time += prc[1]
        print(prc[0], time)


        

