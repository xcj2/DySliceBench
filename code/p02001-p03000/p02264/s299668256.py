class Process_Queue:
    class Process:
        def __init__(self, name, r_time, link = None):
            self.name = name
            self.r_time = r_time
            self.link = link

    def __init__(self, q):
        self.size = 0
        self.e_time = 0
        self.q = q
        self.front = None
        self.rear  = None

    def enqueue(self, name, r_time):
        if self.size == 0:
            self.front = self.rear = Process_Queue.Process(name, r_time)
        elif self.size == 100000:
            raise Exception("queue overflow")
        else:
            new_process = Process_Queue.Process(name, r_time)
            self.rear.link = new_process
            self.rear = new_process
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("queue underflow")
        elif self.front.r_time > self.q:
            self.enqueue(self.front.name, self.front.r_time - self.q)
            self.front = self.front.link
            self.e_time += self.q
        elif self.front.r_time <= self.q:
            p_name = self.front.name
            self.e_time += self.front.r_time
            print(p_name, self.e_time)
            self.front = self.front.link
        self.size -= 1
        if self.size == 0:
            self.rear = None
                
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == 100000


n, q = map(int, input().split())

p_queue = Process_Queue(q)

for i in range(n):
    p = input().split()
    p_queue.enqueue(p[0], int(p[1]))

while not p_queue.isEmpty():
    p_queue.dequeue()