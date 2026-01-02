#Round Robin Schedule
#queue ring buffer
from functools import wraps

def RoundRobinSchedule(process, n, q):
    elasped_time = 0
    head = 0
    tail = 0
    Q = [["a", i] for i in range(n+1)]


    def initialize():
        nonlocal head, tail, Q
        head = 0
        tail = 0


    def isEmpty():
        nonlocal head, tail, Q
        return head == tail


    def isFull():
        nonlocal head, tail, Q
        return head == (tail+1)%(n+1)


    def enqueue(x):
        nonlocal head, tail, Q
        if isFull():
            print("overflow")
            exit()
        Q[tail] = x
        if tail + 1 == n + 1:
            tail = 0
        else:
            tail += 1


    def dequeue():
        nonlocal head, tail, Q
        if isEmpty():
            print("underflow")
            exit()
        x = Q[head]
        if head + 1 == n + 1:
            head = 0
        else:
            head += 1
        return x


    for i in range(n):
        enqueue(process[i])
    while not isEmpty():
        target = dequeue()
        if target[1] <= q:
            elasped_time += target[1]
            print(target[0] + " " + str(elasped_time))
        else:
            elasped_time += q
            enqueue([target[0],target[1] - q])


n,q = [int(i) for i in input().split()]
process = []
for i in range(n):
    a,b = input().split()
    process.append([a,int(b)])
RoundRobinSchedule(process,n,q)
