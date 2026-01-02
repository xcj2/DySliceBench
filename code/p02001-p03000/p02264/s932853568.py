class Process_Queue:
    class Process:
        def __init__(self, name, r_time, link = None):
            self.name = name
            self.r_time = r_time
            self.link = link

    def __init__(self, q):
        self.e_time = 0
        self.q = q
        self.front = None
        self.rear  = None

    def enqueue(self, name, r_time):
        if self.front == self.rear == None:
            self.front = self.rear = Process_Queue.Process(name, r_time)
        else:
            new_process = Process_Queue.Process(name, r_time)
            self.rear.link = new_process
            self.rear = new_process

    def dequeue(self):
        if self.front == self.rear == None:
            raise Exception("queue underflow")
        elif self.front.r_time > self.q:
            self.enqueue(self.front.name, self.front.r_time - self.q)
            self.front = self.front.link
            self.e_time += self.q
        else:
            p_name = self.front.name
            self.e_time += self.front.r_time
            print(p_name, self.e_time)
            self.front = self.front.link
        if self.front == None:
            self.rear = None

n, q = map(int, input().split())

p_queue = Process_Queue(q)

for i in range(n):
    p = input().split()
    p_queue.enqueue(p[0], int(p[1]))

while not p_queue.front == p_queue.rear == None:
    p_queue.dequeue()