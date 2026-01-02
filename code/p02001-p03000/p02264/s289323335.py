class Queue:
    def __init__(self):
        self.max = int(1e6)
        self.data = [0] * self.max
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail
    def isFull(self):
        return self.head == (self.tail + 1) % self.max
    def enqueue(self, x):
        try:
            if self.isFull():
                raise Exception('Queue is full')
            self.data[self.tail] = x
            if self.tail + 1 == self.max:
                self.tail = 0
            else:
                self.tail += 1
        except Exception as e:
            print(e)
    def dequeue(self):
        try:
            if self.isEmpty():
                raise Exception('Queue is empty')
            x = self.data[self.head]
            if self.head + 1 == self.max:
                self.head = 0
            else:
                self.head += 1
            return x
        except Exception as e:
            print(e)

class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.endTime = 0

n, q = map(int, input().split())
processes = Queue()
for i in range(n):
    name, time = input().split()
    time = int(time)
    processes.enqueue(Process(name, time))

totalTime = 0
finishedProcesses = 0

while finishedProcesses < n:
    runningProcess = processes.dequeue()
    if runningProcess.time <= q:
        totalTime += runningProcess.time
        runningProcess.time = 0
        runningProcess.endTime = totalTime
        finishedProcesses += 1
        print(runningProcess.name, runningProcess.endTime)
    else:
        totalTime += q
        runningProcess.time -= q
        processes.enqueue(runningProcess)
