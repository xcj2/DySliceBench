n,q = input().split()
n = int(n)
q = int(q)

queue = []

class process:
    def __init__(self,a,b):
        self.name = a
        self.time = b


for i in range(n):
    a,b = input().split()
    b = int(b)
    queue.append(process(a,b))

def enqueue(proc):
    global queue
    queue.append(proc)

def dequeue():
    global queue
    return queue.pop(0)

def isEnpty():
    global queue
    return len(queue) != 0


def RoundRobinScheduling():
    now_time = 0
    while  isEnpty(): 
        now_process = dequeue()
        if now_process.time - q > 0:
            now_process.time = now_process.time - q
            enqueue(now_process)
            now_time = now_time + q
        else:
            now_time = now_time + now_process.time
            print(now_process.name,end=" ")
            print(now_time)


RoundRobinScheduling()

