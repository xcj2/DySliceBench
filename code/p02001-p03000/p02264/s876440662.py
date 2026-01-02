# coding: utf-8
# Your code here!

class Queue:
    def __init__(self, n):
       
        self.head = 0
        self.tail = 0
        self.MAX = 100005
        self.queue = [Process()] * self.MAX 
        self.qtime = 0
        
    def isEmpty(self):
        return self.head == self.tail
        
    def isFull(self):
        return ( self.queue[self.tail].name != "" ) and (self.head == (self.tail + 1) % self.MAX ) 

    def enqueue(self, x):
        if self.isFull():
            print("error: overflow")
        self.queue[self.tail] = x
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1
        
    def dequeue(self):
        if self.isEmpty():
            print("error: underflow")
            return
        
        x = self.queue[self.head]
        
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x
        
class Process:
    def __init__(self, name = "", time = 0):
        self.name = name
        self.time = time
        
        


tmpList = list(input().split())
N = int(tmpList[0])
qTime = int(tmpList[1])
Q = Queue(N)
Q.qtime = qTime
for i in range(N):
    tmpList = list(input().split())
    tmpProcess = Process(tmpList[0], int(tmpList[1]))
    #Q.queue[i] = tmpProcess
    Q.enqueue(tmpProcess)

cnt = 0
    
while Q.isEmpty() == False:
    process = Q.dequeue()
    
    if process.time > qTime:
        process.time -= qTime
        Q.enqueue(process)
        cnt += qTime
    else:
        cnt += process.time
        print(process.name ,cnt)

"""
    print(Q.head, Q.tail)
    if Q.queue[Q.head].time > qTime:
        Q.queue[Q.head].time -= qTime
    else:
        print(Q.queue[Q.head].name)
        Q.dequeue()
""" 
            








