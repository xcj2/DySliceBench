from collections import deque

class Task:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class RoundRobin:
    def __init__(self):
        self.time = 0
        self.queue = deque()
        self.num_of_task, self.quantum = map(int, input().split())
        
    def enqueue(self, task):
        self.queue.append(task)
    
    def dequeue(self):
        return self.queue.popleft()


rr = RoundRobin()

for _ in range(rr.num_of_task):
    input_task = input().split()
    rr.enqueue(Task(input_task[0], int(input_task[1])))

while len(rr.queue) > 0:
    task = rr.dequeue()
    if task.cost <= rr.quantum:
        rr.time += task.cost
        print("%s %d"%(task.name, rr.time))
    else:
        task.cost -= rr.quantum
        rr.time += rr.quantum
        rr.enqueue(task)

