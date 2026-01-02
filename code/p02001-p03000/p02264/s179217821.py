class Queue:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.front = 0
        self.tail = 0 
    
    def initialize(self):
        self.front = self.tail = 0
    
    def isempty(self):
        return self.front == self.tail
    
    def isfull(self):
        return (self.tail + 1)%len(self.data) == self.front
    
    def enqueue(self, x):
        if self.isfull():
            raise Exception('overflow')
        else:
            self.data[self.tail] = x
            self.tail = (self.tail + 1)%len(self.data)
    
    def dequeue(self):
        if self.isempty():
            raise Exception('underflow')
        else:
            x = self.data[self.front]
            self.front = (self.front + 1) %len(self.data)
            return x

T = 0
size, time = list(map(int, input().split()))
# print(isinstance(time, int))
queue = Queue(size+2)
for i in range(size):
    ele = tuple(input().split())
    queue.enqueue(ele)

while not queue.isempty():
    task, t = queue.dequeue()
    t = int(t)
    if t <= time:
        T += t
        print(task, T)
    else:
        t -= time
        T += time
        queue.enqueue((task,t))
